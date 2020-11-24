from typing import List, Dict
from src.model import Config
from src.model.analyzers.e2e_analysis.EndToEndAnalyzer import EndToEndAnalyzer
from src.model.analyzers.e2e_analysis.result_types import InputSizeResult
from src.model.analyzers.profile_analysis.ProfileAnalyzer import ProfileAnalyzer
import json
import numpy as np
import math

class ComplexityDatapoints:
    """
    Stores datapoints for trend lines of each complexity
    """
    O_1: []
    O_n: []
    O_n2: []
    O_n3: []
    O_nlogn: []
    O_nn: []
    O_n_fact: []

    def __init__(self, e2e_results: Dict[int, InputSizeResult], runtime_calc: bool):
        x_y_pairs = {}
        for i in e2e_results:
            if runtime_calc:
                x_y_pairs[i] = e2e_results[i].average.total_runtime_ms
            else:
                x_y_pairs[i] = e2e_results[i].average.max_memory_usage_bytes
        O1_Eq = np.polyfit(x_y_pairs.keys(), x_y_pairs.values(), 0)
        On_Eq = np.polyfit(x_y_pairs.keys(), x_y_pairs.values(), 1)
        On2_Eq = np.polyfit(x_y_pairs.keys(), x_y_pairs.values(), 2)
        On3_Eq = np.polyfit(x_y_pairs.keys(), x_y_pairs.values(), 3)
        min_n = min(x_y_pairs.keys())
        Onlogn_Scale = x_y_pairs[min_n]/(min_n*math.log(min_n))
        Onexpn_Scale = x_y_pairs[min_n]/(min_n**min_n)
        Onfact_Scale = x_y_pairs[min_n]/math.factorial(min_n)
        for x in x_y_pairs:
            self.O_1.append(O1_Eq[0])
            self.O_n.append(On_Eq[0]*x+On_Eq[1])
            self.O_n2.append(On2_Eq[0]*x**2+On2_Eq[1]*x+On2_Eq[2])
            self.O_n3.append(On3_Eq[0]*x**3+On3_Eq[1]*x**2+On3_Eq[2]*x+On3_Eq[3])
            self.O_nlogn = Onlogn_Scale*(x*math.log(x))
            self.O_nn = Onexpn_Scale*(x**x)
            self.O_n_fact = Onfact_Scale*(math.factorial(x))

class Speedometer:
    """
    Entry-point for the Speedometer analyses tool.
    Call run() to start analysis
    """

    def run(self, program_file_path: str, config: Config) -> None:
        """
        Runs the analysis on the user-provided python program
        :param program_file_path: path to the program to analyze
        :param config: config object for user-defined configuration
        """

        profiler = ProfileAnalyzer()
        profiler.analyze(program_file_path, config)
        profiler_results = profiler.get_results()

        e2e_analyzer = EndToEndAnalyzer()
        e2e_analyzer.analyze(program_file_path, config)
        e2e_results = e2e_analyzer.get_results()

        self.build_visualization(profiler_results, e2e_results)

    def build_visualization(self, profiler_results, e2e_results) -> None:
        """
        Builds the visualizations with the given results
        :param profiler_results: results from the profile analysis
        :param e2e_results: results from the end to end analysis
        """
        output = {}

        e2e_runtime = []
        e2e_memory = []
        runtime_fit_point = ComplexityDatapoints(e2e_results, True)
        memory_fit_point = ComplexityDatapoints(e2e_results, False)
        for i in e2e_results:
            e2e_runtime.append({
                "n": str(i),
                "total_runtime": e2e_results[i].average.total_runtime_ms,
                "O(1)": runtime_fit_point.O_1,
                "O(n)": runtime_fit_point.O_n,
                "O(n\u00B2)": runtime_fit_point.O_n2,
                "O(n\u00B3)": runtime_fit_point.O_n3,
                "O(nlog(n))": runtime_fit_point.O_nlogn,
                "O(n\u207F)": runtime_fit_point.O_nn,
                "O(n!)": runtime_fit_point.O_n_fact
            })
            e2e_memory.append({
                "n": str(i),
                "total_memory": e2e_results[i].average.max_memory_usage_bytes,
                "O(1)": memory_fit_point.O_1,
                "O(n)": memory_fit_point.O_n,
                "O(n\u00B2)": memory_fit_point.O_n2,
                "O(n\u00B3)": memory_fit_point.O_n3,
                "O(nlog(n))": memory_fit_point.O_nlogn,
                "O(n\u207F)": memory_fit_point.O_nn,
                "O(n!)": memory_fit_point.O_n_fact,
                "memory_usage_by_time": e2e_results[i].average.memory_usage_by_time
            })
        output["e2e"] = {"e2e_runtime": e2e_runtime, "e2e_memory": e2e_memory}

        class_runtime = []
        class_memory = []
        for c in profiler_results["class"]:
            class_runtime.append({
                "name": c.file_name+"/"+c.name,
                "total_runtime": c.total_run_time
            })
        output["class"] = {"class_runtime": class_runtime, "class_memory": class_memory}

        function_runtimes = []
        function_memory = []
        for f in profiler_results["function"]:
            function_runtimes.append({
                "name": f.file_name+"/"+f.name,
                "total_runtime": f.total_run_time
            })
        output["function"] = {"function_runtime": function_runtimes, "function_memory": function_memory}

        line_by_line = []
        for l in profiler_results["line_by_line"]:
            line_by_line.append({
                "fileName": l.file_name,
                "line_num": l.line_num,
                "code": l.line_code,
                "total_runtime": l.total_run_time,
                "total_memory": l.total_memory
            })
        output["line_by_line"] = line_by_line

        with open('output_data.json', 'w') as outfile:
            json.dump(output, outfile)

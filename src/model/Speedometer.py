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
    O_1: dict
    O_logn: dict
    O_n: dict
    O_n2: dict
    O_n3: dict
    O_nlogn: dict
    O_nn: dict
    O_n_fact: dict

    def __init__(self):
        self.O_1 = {}
        self.O_logn = {}
        self.O_n = {}
        self.O_n2 = {}
        self.O_n3 = {}
        self.O_nlogn = {}
        self.O_nn = {}
        self.O_n_fact = {}

    def get_fit_data(self, e2e_results: dict, runtime_calc: bool):
        """
        Sets the key-value pairs for each fit line, n -> O(n)
        :param e2e_results: results from the end to end analysis
        :param runtime_calc: true if looking for runtime, false if looking for memory
        """
        # x_y_pairs is a mapping from n to average total runtime/memory from e2e results
        x_y_pairs = {}
        for i in e2e_results:
            if runtime_calc:
                x_y_pairs[i] = e2e_results[i].average.total_runtime_ms
            else:
                x_y_pairs[i] = e2e_results[i].average.max_memory_usage_bytes

        # TODO


        # below is my previous attempt/code to just make it work for now
        O1_Eq = [1]#np.polyfit(list(x_y_pairs.keys()), list(x_y_pairs.values()), 0)
        On_Eq = [1,0]#np.polyfit(list(x_y_pairs.keys()), list(x_y_pairs.values()), 1)
        On2_Eq = [1,0,0]#np.polyfit(list(x_y_pairs.keys()), list(x_y_pairs.values()), 2)
        On3_Eq = [1,0,0,0]#np.polyfit(list(x_y_pairs.keys()), list(x_y_pairs.values()), 3)
        min_n = min(list(x_y_pairs.keys()))
        Ologn_Scale = 1#x_y_pairs[min_n]/(math.log(min_n))
        Onlogn_Scale = 1#x_y_pairs[min_n]/(min_n*math.log(min_n))
        Onexpn_Scale = 1#x_y_pairs[min_n]/(min_n**min_n)
        Onfact_Scale = 1#x_y_pairs[min_n]/math.factorial(min_n)
        for x in x_y_pairs:
            self.O_1[x] = O1_Eq[0]
            self.O_logn[x] = Ologn_Scale*(math.log(x))
            self.O_n[x] = On_Eq[0]*x+On_Eq[1]
            self.O_n2[x] = On2_Eq[0]*x**2+On2_Eq[1]*x+On2_Eq[2]
            self.O_n3[x] = On3_Eq[0]*x**3+On3_Eq[1]*x**2+On3_Eq[2]*x+On3_Eq[3]
            self.O_nlogn[x] = Onlogn_Scale*(x*math.log(x))
            self.O_nn[x] = Onexpn_Scale*(x**x)
            self.O_n_fact[x] = Onfact_Scale*(math.factorial(x))

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

        self.build_visualization(program_file_path, profiler_results, e2e_results)

    def build_visualization(self, program_file_path, profiler_results, e2e_results) -> dict:
        """
        Builds the visualizations with the given results
        :param profiler_results: results from the profile analysis
        :param e2e_results: results from the end to end analysis
        """
        output = {}
        output["script_name"] = program_file_path

        # create class object, two arrays for runtime and memory containing original file name, avg time/memory per class
        class_runtime = []
        class_memory = []
        for c in profiler_results["class"]:
            class_runtime.append({
                "name": c.filename+"/"+c.name,
                "total_runtime": c.total_run_time,
                "percent_runtime": c.percent_runtime
            })
            class_memory.append({
                "name": c.filename+"/"+c.name,
                "total_memory": c.total_memory,
                "percent_memory": c.percent_memory
            })
        output["class"] = {"class_runtime": class_runtime, "class_memory": class_memory}

        # create function object, two arrays for runtime and memory containing original file name, avg time/memory per function
        # find function that takes longest/uses most memory
        function_runtimes = []
        function_memory = []
        max_fun_runtime = 0.0
        max_fun_memory = 0.0
        max_fun_runtime_name = ""
        max_fun_memory_name = ""
        for f in profiler_results["function"]:
            function_runtimes.append({
                "name": f.filename+"/"+f.name,
                "total_runtime": f.total_run_time,
                "percent_runtime": f.percent_runtime
            })
            if f.total_run_time > max_fun_runtime:
                max_fun_runtime_name = f.name
                max_fun_runtime = f.total_run_time
            function_memory.append({
                "name": f.filename + "/" + f.name,
                "total_memory": f.total_memory,
                "percent_memory": f.percent_memory
            })
            if f.total_memory > max_fun_memory:
                max_fun_memory_name = f.name
                max_fun_memory = f.total_memory
        output["function"] = {"function_runtime": function_runtimes, "function_memory": function_memory}

        # create array of line objects with filename, line#, code content, runtime, and memory usage
        line_by_line = []
        for l in profiler_results["line_by_line"]:
            line_by_line.append({
                "fileName": l.filename,
                "line_num": l.line_num,
                "code": l.line_text,
                "total_runtime": l.total_run_time,
                "total_memory": l.total_memory,
                "percent_runtime": l.percent_runtime,
                "percent_memory": l.percent_memory
            })
        output["line_by_line"] = line_by_line

        e2e_object = {}
        e2e_runtime = []
        e2e_memory = []
        # calculate fit line data for runtime & memory
        runtime_fit_point = ComplexityDatapoints()
        runtime_fit_point.get_fit_data(e2e_results, True)
        memory_fit_point = ComplexityDatapoints()
        memory_fit_point.get_fit_data(e2e_results, False)
        total_runtime_points = []
        total_memory_points = []

        #e2e object contains two arrays for runtime and memory containing the n parameter, avg runtime/memory, and associated fit data
        for i in e2e_results:
            e2e_runtime.append({
                "n": str(i),
                "total_runtime": e2e_results[i].average.total_runtime_ms,
                "O(1)": runtime_fit_point.O_1[i],
                "O(log(n))": runtime_fit_point.O_logn[i],
                "O(n)": runtime_fit_point.O_n[i],
                "O(n\u00B2)": runtime_fit_point.O_n2[i],
                "O(n\u00B3)": runtime_fit_point.O_n3[i],
                "O(nlog(n))": runtime_fit_point.O_nlogn[i],
                "O(n\u207F)": runtime_fit_point.O_nn[i],
                "O(n!)": runtime_fit_point.O_n_fact[i]
            })
            total_runtime_points.append(e2e_results[i].average.total_runtime_ms)
            e2e_memory.append({
                "n": str(i),
                "total_memory": e2e_results[i].average.max_memory_usage_bytes,
                "O(1)": memory_fit_point.O_1[i],
                "O(log(n))": memory_fit_point.O_logn[i],
                "O(n)": memory_fit_point.O_n[i],
                "O(n\u00B2)": memory_fit_point.O_n2[i],
                "O(n\u00B3)": memory_fit_point.O_n3[i],
                "O(nlog(n))": memory_fit_point.O_nlogn[i],
                "O(n\u207F)": memory_fit_point.O_nn[i],
                "O(n!)": memory_fit_point.O_n_fact[i],
                "memory_usage_by_time": e2e_results[i].average.memory_usage_by_time
            })
            total_memory_points.append(e2e_results[i].average.max_memory_usage_bytes)
        # set E2E runtime/memory arrays, highest runtime/memory functions, total function runtime/memory usage, and calculate complexity of program
        e2e_object["e2e_runtime"] = e2e_runtime
        e2e_object["e2e_memory"] = e2e_memory
        e2e_object["e2e_highest_runtime_function"] = max_fun_runtime_name
        e2e_object["e2e_highest_memory_usage_function"] = max_fun_memory_name
        e2e_object["e2e_total_average_time"] = sum(total_runtime_points) / len(e2e_runtime)
        e2e_object["e2e_total_average_memory"] = sum(total_memory_points) / len(e2e_memory)
        e2e_object["e2e_time_complexity"] = self.find_O_fit(runtime_fit_point, total_runtime_points)
        e2e_object["e2e_space_complexity"] = self.find_O_fit(memory_fit_point, total_memory_points)
        output["e2e"] = e2e_object

        with open('client/src/Data/data.json', 'w') as outfile:
            json.dump(output, outfile)
        return output

    def find_O_fit(self, fit_data: ComplexityDatapoints, raw_data: list) -> str:
        """
        Calculate the least squares value between experimental data and the expected fitline
        :param fit_data: collection of all fit data
        :param raw_data: results from the end to end analysis
        """
        min_least_square = self.least_squares(list(fit_data.O_1.values()), raw_data)
        return_str = "1"

        o_n_least_square = self.least_squares(list(fit_data.O_n.values()), raw_data)
        if o_n_least_square < min_least_square:
            min_least_square = o_n_least_square
            return_str = "n"

        o_logn_least_square = self.least_squares(list(fit_data.O_logn.values()), raw_data)
        if o_logn_least_square < min_least_square:
            min_least_square = o_logn_least_square
            return_str = "logn"

        o_n2_least_square = self.least_squares(list(fit_data.O_n2.values()), raw_data)
        if o_n2_least_square < min_least_square:
            min_least_square = o_n2_least_square
            return_str = "n2"

        o_n3_least_square = self.least_squares(list(fit_data.O_n3.values()), raw_data)
        if o_n3_least_square < min_least_square:
            min_least_square = o_n3_least_square
            return_str = "n3"

        o_nlogn_least_square = self.least_squares(list(fit_data.O_nlogn.values()), raw_data)
        if o_nlogn_least_square < min_least_square:
            min_least_square = o_nlogn_least_square
            return_str = "nlogn"

        o_nn_least_square = self.least_squares(list(fit_data.O_nn.values()), raw_data)
        if o_nn_least_square < min_least_square:
            min_least_square = o_nn_least_square
            return_str = "nn"

        o_nfact_least_square = self.least_squares(list(fit_data.O_n_fact.values()), raw_data)
        if o_nfact_least_square < min_least_square:
            min_least_square = o_nfact_least_square
            return_str = "n!"

        return return_str

    def least_squares(self, data_y, fit_y) -> float:
        """
        Calculate the least squares value between experimental data and the expected fitline
        :param data_y: array of data from
        :param fit_y: results from the end to end analysis
        """

        if len(data_y) != len(fit_y):
            raise RuntimeError("Fit data point count does not equal observed data point count.")
        ls_sum = 0.0
        for i in range(len(data_y)):
            ls_sum += (data_y[i] - fit_y[i])**2
        return ls_sum

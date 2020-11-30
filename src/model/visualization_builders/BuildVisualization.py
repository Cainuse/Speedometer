import json
from typing import Dict
import math
import os

from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
from src.model.data_transformers.ClosestFit import find_O_fit
from src.model.data_transformers.ReferenceFits import FitData, get_reference_fits
from src.model.data_transformers.SankeyDataCalculator import get_sankey_data
from src.model.util.Logger import debug

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "client"))
DATA_FILE = os.path.abspath(os.path.join(CLIENT_DIR, "src", "Data", "data.json"))


def build_visualization(program_file_path, profiler_results, e2e_results: Dict[int, InputSizeResult]) -> dict:
    """
    Builds the visualizations with the given results
    :param program_file_path: path to the user's program
    :param profiler_results: results from the profile analysis
    :param e2e_results: results from the end to end analysis
    """
    debug("Starting results_visualization building")
    input_path_split = program_file_path.split("/")
    if len(input_path_split) > 0:
        output = {"script_name": input_path_split[len(input_path_split)-1]}
    else:
        output = {"script_name": program_file_path}

    # create class object, two arrays for runtime and memory containing original file name, avg time/memory per class
    debug("Creating class objects")
    class_runtime = []
    class_memory = []
    for c in profiler_results["class"]:
        class_runtime.append({
            "name": c.filename + "/" + c.name,
            "total_runtime": c.total_run_time,
            "percent_runtime": c.time_percentage_of_total
        })
        class_memory.append({
            "name": c.filename + "/" + c.name,
            "total_memory": c.total_memory,
            "percent_memory": c.memory_percentage_of_total
        })
    output["class"] = {"class_runtime": class_runtime, "class_memory": class_memory}
    debug("Class objects created")

    # create function object, two arrays for runtime and memory containing original file name, avg time/memory per function
    # find function that takes longest/uses most memory
    debug("Creating function objects")
    function_runtimes = []
    function_memory = []
    max_fun_runtime = 0.0
    max_fun_memory = 0.0
    max_fun_runtime_name = ""
    max_fun_memory_name = ""
    for f in profiler_results["function"]:
        function_runtimes.append({
            "name": f.filename + "/" + f.name,
            "total_runtime": f.total_run_time,
            "percent_runtime": f.time_percentage_of_total
        })
        if f.total_run_time > max_fun_runtime:
            max_fun_runtime_name = f.name
            max_fun_runtime = f.total_run_time
        function_memory.append({
            "name": f.filename + "/" + f.name,
            "total_memory": f.total_memory,
            "percent_memory": f.memory_percentage_of_total
        })
        if f.total_memory > max_fun_memory:
            max_fun_memory_name = f.name
            max_fun_memory = f.total_memory
    output["function"] = {"function_runtime": function_runtimes, "function_memory": function_memory}
    debug("Function objects created")

    # create array of line objects with filename, line#, code content, runtime, and memory usage
    debug("Creating line objects")
    line_by_line = []
    line_of_function = []
    current_fun = ""
    for l in profiler_results["line_by_line"]:
        if current_fun == "":
            current_fun = l.filename
        else:
            if current_fun != l.filename:
                line_by_line.append(line_of_function)
                line_of_function = []
        line_of_function.append({
            "fileName": l.filename,
            "line_num": l.line_num,
            "code": l.line_text,
            "total_runtime": l.total_run_time,
            "total_memory": l.total_memory,
            "percent_runtime": l.time_percentage_of_total,
            "percent_memory": l.memory_percentage_of_total
        })
    line_by_line.append(line_of_function)
    output["line_by_line"] = line_by_line
    debug("Line objects created")

    e2e_object = {}
    e2e_runtime = []
    e2e_memory = []
    # calculate fit line data for runtime & memory
    debug("Calculating runtime fit lines")
    fit_data_runtime: FitData = get_reference_fits(e2e_results, True)
    debug("Calculating memory fit lines")
    fit_data_memory: FitData = get_reference_fits(e2e_results, False)
    total_runtime_points = {}
    total_memory_points = {}

    # e2e object contains two arrays for runtime and memory containing the n parameter, avg runtime/memory, and associated fit data
    debug("Creating e2e object")
    for i in e2e_results:
        debug("Parsing e2e - n = {}".format(i))
        # rt_obj = {}

        e2e_runtime.append({
            "n": i,
            "total_runtime": round(math.log(round(e2e_results[i].average.total_runtime_ms, 2) if round(e2e_results[i].average.total_runtime_ms, 2) > 1 else 1), 2),
            "O(1)": round(math.log(round(fit_data_runtime.O_1[i], 2) if round(fit_data_runtime.O_1[i], 2) > 1 else 1), 2),
            "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[i], 2) if round(fit_data_runtime.O_logn[i], 2) > 1 else 1), 2),
            "O(n)": round(math.log(round(fit_data_runtime.O_n[i], 2) if round(fit_data_runtime.O_n[i], 2) > 1 else 1), 2),
            "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[i], 2) if round(fit_data_runtime.O_n2[i], 2) > 1 else 1), 2),
            "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[i], 2) if round(fit_data_runtime.O_n3[i], 2) > 1 else 1), 2),
            "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[i], 2) if round(fit_data_runtime.O_nlogn[i], 2) > 1 else 1), 2),
            "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[i], 2) if round(fit_data_runtime.O_nn[i], 2) > 1 else 1), 2),
            "O(n!)": round(math.log(round(fit_data_runtime.O_n_fact[i], 2) if round(fit_data_runtime.O_n_fact[i], 2) > 1 else 1), 2)
        })
        total_runtime_points[i] = e2e_results[i].average.total_runtime_ms
        e2e_memory.append({
            "n": i,
            "total_memory": round(math.log(round(e2e_results[i].average.max_memory_usage_bytes / 10**6, 2) if round(e2e_results[i].average.max_memory_usage_bytes / 10**6, 2) > 1 else 1), 2),
            "O(1)": round(math.log(round(fit_data_memory.O_1[i] / 10**6, 2) if round(fit_data_memory.O_1[i] / 10**6, 2) > 1 else 1), 2),
            "O(log(n))": round(math.log(round(fit_data_memory.O_logn[i] / 10**6, 2) if round(fit_data_memory.O_logn[i] / 10**6, 2) > 1 else 1), 2),
            "O(n)": round(math.log(round(fit_data_memory.O_n[i] / 10**6, 2) if round(fit_data_memory.O_n[i] / 10**6, 2) > 1 else 1), 2),
            "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[i] / 10**6, 2) if round(fit_data_memory.O_n2[i] / 10**6, 2) > 1 else 1), 2),
            "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[i] / 10**6, 2) if round(fit_data_memory.O_n3[i] / 10**6, 2) > 1 else 1), 2),
            "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[i] / 10**6, 2) if round(fit_data_memory.O_nlogn[i] / 10**6, 2) > 1 else 1), 2),
            "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[i] / 10**6, 2) if round(fit_data_memory.O_nn[i] / 10**6, 2) > 1 else 1), 2),
            "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[i] / 10**6, 2) if round(fit_data_memory.O_n_fact[i] / 10**6, 2) > 1 else 1), 2),
            "memory_usage_by_time": e2e_results[i].average.memory_usage_by_time
        })
        total_memory_points[i] = e2e_results[i].average.max_memory_usage_bytes
    # set E2E runtime/memory arrays, highest runtime/memory functions, total function runtime/memory usage, and calculate complexity of program
    e2e_object["e2e_runtime"] = e2e_runtime
    e2e_object["e2e_memory"] = e2e_memory
    e2e_object["e2e_highest_runtime_function"] = max_fun_runtime_name
    e2e_object["e2e_highest_memory_usage_function"] = max_fun_memory_name
    e2e_object["e2e_total_average_time"] = round(sum(list(total_runtime_points.values())) / len(e2e_runtime), 2)
    e2e_object["e2e_total_average_memory"] = round(sum(list(total_memory_points.values())) / len(e2e_memory) / 10**6, 2)
    debug("Calculating project runtime complexity")
    e2e_object["e2e_time_complexity"] = find_O_fit(fit_data_runtime, total_runtime_points)
    debug("Calculating project memory complexity")
    e2e_object["e2e_space_complexity"] = find_O_fit(fit_data_memory, total_memory_points)
    output["e2e"] = e2e_object
    debug("e2e object created")

    #create sankey data object
    debug("Creating sankey object")
    output["sankey"] = {
        "sankey_runtime": get_sankey_data(profiler_results, True),
        "sankey_memory": get_sankey_data(profiler_results, False)
    }
    debug("Sankey object created")

    with open(DATA_FILE, 'w') as outfile:
        json.dump(output, outfile)
    debug("JSON created")
    return output
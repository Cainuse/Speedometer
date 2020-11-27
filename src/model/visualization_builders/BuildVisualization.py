import json
from typing import Dict

from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
from src.model.data_transformers.ClosestFit import find_O_fit
from src.model.data_transformers.ReferenceFits import FitData, get_reference_fits


def build_visualization(program_file_path, profiler_results, e2e_results: Dict[int, InputSizeResult]) -> dict:
    """
    Builds the visualizations with the given results
    :param program_file_path: path to the user's program
    :param profiler_results: results from the profile analysis
    :param e2e_results: results from the end to end analysis
    """
    output = {"script_name": program_file_path}

    # create class object, two arrays for runtime and memory containing original file name, avg time/memory per class
    class_runtime = []
    class_memory = []
    for c in profiler_results["class"]:
        class_runtime.append({
            "name": c.filename + "/" + c.name,
            "total_runtime": c.total_run_time,
            "percent_runtime": c.percent_runtime
        })
        class_memory.append({
            "name": c.filename + "/" + c.name,
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
            "name": f.filename + "/" + f.name,
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
    fit_data_runtime: FitData = get_reference_fits(e2e_results, True)
    fit_data_memory: FitData = get_reference_fits(e2e_results, False)
    total_runtime_points = []
    total_memory_points = []

    # e2e object contains two arrays for runtime and memory containing the n parameter, avg runtime/memory, and associated fit data
    for i in e2e_results:
        e2e_runtime.append({
            "n": str(i),
            "total_runtime": e2e_results[i].average.total_runtime_ms,
            "O(1)": fit_data_runtime.O_1[i],
            "O(log(n))": fit_data_runtime.O_logn[i],
            "O(n)": fit_data_runtime.O_n[i],
            "O(n\u00B2)": fit_data_runtime.O_n2[i],
            "O(n\u00B3)": fit_data_runtime.O_n3[i],
            "O(nlog(n))": fit_data_runtime.O_nlogn[i],
            "O(n\u207F)": fit_data_runtime.O_nn[i],
            "O(n!)": fit_data_runtime.O_n_fact[i]
        })
        total_runtime_points.append(e2e_results[i].average.total_runtime_ms)
        e2e_memory.append({
            "n": str(i),
            "total_memory": e2e_results[i].average.max_memory_usage_bytes,
            "O(1)": fit_data_memory.O_1[i],
            "O(log(n))": fit_data_memory.O_logn[i],
            "O(n)": fit_data_memory.O_n[i],
            "O(n\u00B2)": fit_data_memory.O_n2[i],
            "O(n\u00B3)": fit_data_memory.O_n3[i],
            "O(nlog(n))": fit_data_memory.O_nlogn[i],
            "O(n\u207F)": fit_data_memory.O_nn[i],
            "O(n!)": fit_data_memory.O_n_fact[i],
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
    e2e_object["e2e_time_complexity"] = find_O_fit(fit_data_runtime, total_runtime_points)
    e2e_object["e2e_space_complexity"] = find_O_fit(fit_data_memory, total_memory_points)
    output["e2e"] = e2e_object

    with open('client/src/Data/data.json', 'w') as outfile:
        json.dump(output, outfile)
    return output
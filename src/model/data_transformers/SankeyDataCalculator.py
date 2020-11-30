def get_sankey_data(profiler_results, runtime_calc: bool) -> dict:

    class_runtimes = profiler_results["class"]
    function_runtimes = profiler_results["function"]

    nodes, files, classes, functions = _build_nodes(class_runtimes, function_runtimes)
    links = _build_links(class_runtimes, function_runtimes, files, classes, functions, runtime_calc)

    sankey_data = {
        "nodes": nodes,
        "links": links
    }
    return sankey_data


def _build_links(class_runtimes, function_runtimes, files, classes, functions, runtime_calc) -> list:
    links = []

    for class_runtime in class_runtimes:
        source_idx = files[class_runtime.filename]["index"]
        dst_idx = classes[class_runtime.name]["index"]
        value = class_runtime.time_percentage_of_total if runtime_calc else class_runtime.memory_percentage_of_total
        links.append({"source": source_idx, "target": dst_idx, "value": value})

    for class_runtime in class_runtimes:
        source_class = classes[class_runtime.name]["runtime"]
        source_idx = classes[class_runtime.name]["index"]
        for functionIdx in class_runtime.class_functions:
            func_runtime = function_runtimes[functionIdx]
            dst_idx = functions[func_runtime.name]["index"]
            value = func_runtime.time_percentage_of_total if runtime_calc else func_runtime.memory_percentage_of_total
            if runtime_calc:
                if source_class.time_percentage_of_total == 0:
                    value = 0
                else:
                    value /= source_class.time_percentage_of_total
            else:
                if source_class.memory_percentage_of_total == 0:
                    value = 0
                else:
                    value /= source_class.memory_percentage_of_total

            value *= 100
            links.append({"source": source_idx, "target": dst_idx, "value": value})

    return links


def _build_nodes(class_runtimes, function_runtimes) -> (list, dict, dict, dict):
    nodes = []
    files = {}
    classes = {}
    functions = {}

    index = 0
    for class_runtime in class_runtimes:
        if class_runtime.filename not in files.keys():
            nodes.append({"name": class_runtime.filename})
            files[class_runtime.filename] = {"index": index, "runtime": None}  # there is no file runtime
            index += 1

    for class_runtime in class_runtimes:
        if class_runtime.name not in classes.keys():
            nodes.append({"name": class_runtime.name})
            classes[class_runtime.name] = {"index": index, "runtime": class_runtime}
            index += 1

    for function_runtime in function_runtimes:
        if function_runtime.name not in functions.keys():
            nodes.append({"name": function_runtime.name})
            functions[function_runtime.name] = {"index": index, "runtime": function_runtime}
            index += 1

    return nodes, files, classes, functions

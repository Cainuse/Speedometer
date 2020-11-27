from src.model.analyzers.profile_analysis.ProfileAnalyzer import class_runtime, function_runtime
from src.model.data_transformers.SankeyDataCalculator import get_sankey_data

PROFILER_RESULT_1 = {"class": [], "function": [], "line_by_line": []}

PROFILER_RESULT_2 = {
    "class": [
        class_runtime("file_foo", "class_bar1", 0.0, 0.0, 40.0, 60.0, [0, 2]),
        class_runtime("file_foo", "class_bar2", 0.0, 0.0, 60.0, 40.0, [1])
    ],
    "function": [
        function_runtime("file_foo", "function_baz0", 0.0, 0.0, 30.0, 30.0),
        function_runtime("file_foo", "function_baz1", 0.0, 0.0, 60, 40.0),
        function_runtime("file_foo", "function_baz2", 0.0, 0.0, 10.0, 30.0)
    ],
    "line_by_line": []
}


def test_no_data():
    sankey_data = get_sankey_data(PROFILER_RESULT_1, runtime_calc=True)
    assert "nodes" in sankey_data
    assert len(sankey_data["nodes"]) == 0
    assert "links" in sankey_data
    assert len(sankey_data["links"]) == 0


def test_runtime_sankey():
    sankey_data = get_sankey_data(PROFILER_RESULT_2, runtime_calc=True)

    assert "nodes" in sankey_data
    assert "links" in sankey_data

    node_names = [node["name"] for node in sankey_data["nodes"]]
    assert node_names == ["file_foo", "class_bar1", "class_bar2", "function_baz0", "function_baz1", "function_baz2"]

    links = sankey_data["links"]
    expected_links = [
        {"source": 0, "target": 1, "value": 40.0},
        {"source": 0, "target": 2, "value": 60.0},
        {"source": 1, "target": 3, "value": 75.0},
        {"source": 1, "target": 5, "value": 25.0},
        {"source": 2, "target": 4, "value": 100.0},
    ]
    assert links == expected_links


def test_memory_sankey():
    sankey_data = get_sankey_data(PROFILER_RESULT_2, runtime_calc=False)

    assert "nodes" in sankey_data
    assert "links" in sankey_data

    node_names = [node["name"] for node in sankey_data["nodes"]]
    assert node_names == ["file_foo", "class_bar1", "class_bar2", "function_baz0", "function_baz1", "function_baz2"]

    links = sankey_data["links"]
    expected_links = [
        {"source": 0, "target": 1, "value": 60.0},
        {"source": 0, "target": 2, "value": 40.0},
        {"source": 1, "target": 3, "value": 50.0},
        {"source": 1, "target": 5, "value": 50.0},
        {"source": 2, "target": 4, "value": 100.0},
    ]
    assert links == expected_links
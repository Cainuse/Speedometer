import math
import numpy as np

from src.model.Speedometer import Speedometer
from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult
from src.model.analyzers.profile_analysis.ProfileAnalyzer import class_runtime
from src.model.analyzers.profile_analysis.ProfileAnalyzer import function_runtime
from src.model.analyzers.profile_analysis.ProfileAnalyzer import line_by_line_runtime
from src.model.data_transformers.ReferenceFits import FitData, get_reference_fits
from src.model.visualization_builders.BuildVisualization import build_visualization


class TestBuildVisualization:

    TEST_RESULT_1 = TestResult(
        1,
        1000000,
        {0: 10, 1: 20, 2: 30, 3: 40}
    )

    TEST_RESULT_2 = TestResult(
        4,
        2000000,
        {0: 20, 1: 30, 2: 40, 3: 50.5, 4: 100.1}
    )

    TEST_RESULT_3 = TestResult(
        9,
        3000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_4 = TestResult(
        100,
        10000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_5 = TestResult(
        25,
        5000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_6 = TestResult(
        400,
        20000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_7 = TestResult(
        81,
        9000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_8 = TestResult(
        225,
        15000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_9 = TestResult(
        2500,
        50000000,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_10 = TestResult(
        144,
        12000000,
        {0: 3, 1: 7, 2: 11}
    )

    CLASS_OBJECT_1 = class_runtime(
        "test.py",
        "Speedometer",
        46.52,
        3.2,
        100,
        100,
        [0, 1]
    )

    FUN_OBJECT_1 = function_runtime(
        "test.py",
        "getSpeed()",
        23.44,
        1.0,
        50.39,
        31.25
    )

    FUN_OBJECT_2 = function_runtime(
        "test.py",
        "getPosition()",
        23.08,
        2.2,
        49.61,
        68.75
    )

    LINE_OBJECT_1 = line_by_line_runtime(
        "test.py",
        1,
        0.0,
        0.0,
        "class Speedometer:",
        0.0
    )

    LINE_OBJECT_2 = line_by_line_runtime(
        "test.py",
        2,
        0.0,
        0.0,
        "   def getSpeed():",
        0.0
    )

    LINE_OBJECT_3 = line_by_line_runtime(
        "test.py",
        3,
        22.24,
        0.5,
        "      do lots of things",
        47.81
    )

    LINE_OBJECT_4 = line_by_line_runtime(
        "test.py",
        4,
        0.0,
        0.0,
        "      if some condition:",
        0.0
    )

    LINE_OBJECT_5 = line_by_line_runtime(
        "test.py",
        5,
        1.2,
        0.5,
        "          conditional statement",
        2.58
    )

    LINE_OBJECT_6 = line_by_line_runtime(
        "test.py",
        6,
        0.0,
        0.0,
        "   def getPosition():",
        0.0
    )

    LINE_OBJECT_7 = line_by_line_runtime(
        "test.py",
        7,
        23.08,
        2.2,
        "       print(position)",
        49.61
    )

    e2e_result = {
        1: InputSizeResult(TEST_RESULT_1,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
        2: InputSizeResult(TEST_RESULT_2,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
        3: InputSizeResult(TEST_RESULT_3,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
        10: InputSizeResult(TEST_RESULT_4, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        5: InputSizeResult(TEST_RESULT_5, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        20: InputSizeResult(TEST_RESULT_6, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        9: InputSizeResult(TEST_RESULT_7, [TEST_RESULT_7,TEST_RESULT_8,TEST_RESULT_9]),
        15: InputSizeResult(TEST_RESULT_8, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        50: InputSizeResult(TEST_RESULT_9, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        12: InputSizeResult(TEST_RESULT_10, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6])
    }
    profile_result = {
        "class": [CLASS_OBJECT_1],
        "function": [FUN_OBJECT_1, FUN_OBJECT_2],
        "line_by_line": [LINE_OBJECT_1, LINE_OBJECT_2, LINE_OBJECT_3, LINE_OBJECT_4, LINE_OBJECT_5, LINE_OBJECT_6, LINE_OBJECT_7]
    }

    fit_data_runtime: FitData = get_reference_fits(e2e_result, True)
    fit_data_memory: FitData = get_reference_fits(e2e_result, False)

    output = {
        "script_name": "test.py",
        "class": {
            'class_runtime': [{
              'name': 'test.py/Speedometer',
              'total_runtime': CLASS_OBJECT_1.total_run_time,
              'percent_runtime': CLASS_OBJECT_1.time_percentage_of_total
            }],
            'class_memory': [{
                'name': 'test.py/Speedometer',
                'total_memory': CLASS_OBJECT_1.total_memory,
                'percent_memory': CLASS_OBJECT_1.memory_percentage_of_total
            }]},
        "function": {
            'function_runtime': [{
              'name': 'test.py/getSpeed()',
              'total_runtime': FUN_OBJECT_1.total_run_time,
              'percent_runtime': FUN_OBJECT_1.time_percentage_of_total
            }, {
              'name': 'test.py/getPosition()',
              'total_runtime': FUN_OBJECT_2.total_run_time,
              'percent_runtime': FUN_OBJECT_2.time_percentage_of_total
            }],
            'function_memory': [{
              'name': 'test.py/getSpeed()',
              'total_memory': FUN_OBJECT_1.total_memory,
              'percent_memory': FUN_OBJECT_1.memory_percentage_of_total
            }, {
              'name': 'test.py/getPosition()',
              'total_memory': FUN_OBJECT_2.total_memory,
              'percent_memory': FUN_OBJECT_2.memory_percentage_of_total
            }]},
        "line_by_line": [[{
            "fileName": LINE_OBJECT_1.filename,
            "line_num": LINE_OBJECT_1.line_num,
            "code": LINE_OBJECT_1.line_text,
            "total_runtime": LINE_OBJECT_1.total_run_time,
            "total_memory": LINE_OBJECT_1.total_memory,
            "percent_runtime": LINE_OBJECT_1.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_1.memory_percentage_of_total
        }, {
            "fileName": LINE_OBJECT_2.filename,
            "line_num": LINE_OBJECT_2.line_num,
            "code": LINE_OBJECT_2.line_text,
            "total_runtime": LINE_OBJECT_2.total_run_time,
            "total_memory": LINE_OBJECT_2.total_memory,
            "percent_runtime": LINE_OBJECT_2.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_2.memory_percentage_of_total
        }, {
            "fileName": LINE_OBJECT_3.filename,
            "line_num": LINE_OBJECT_3.line_num,
            "code": LINE_OBJECT_3.line_text,
            "total_runtime": LINE_OBJECT_3.total_run_time,
            "total_memory": LINE_OBJECT_3.total_memory,
            "percent_runtime": LINE_OBJECT_3.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_3.memory_percentage_of_total
        }, {
            "fileName": LINE_OBJECT_4.filename,
            "line_num": LINE_OBJECT_4.line_num,
            "code": LINE_OBJECT_4.line_text,
            "total_runtime": LINE_OBJECT_4.total_run_time,
            "total_memory": LINE_OBJECT_4.total_memory,
            "percent_runtime": LINE_OBJECT_4.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_4.memory_percentage_of_total
        }, {
            "fileName": LINE_OBJECT_5.filename,
            "line_num": LINE_OBJECT_5.line_num,
            "code": LINE_OBJECT_5.line_text,
            "total_runtime": LINE_OBJECT_5.total_run_time,
            "total_memory": LINE_OBJECT_5.total_memory,
            "percent_runtime": LINE_OBJECT_5.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_5.memory_percentage_of_total
        }, {
            "fileName": LINE_OBJECT_6.filename,
            "line_num": LINE_OBJECT_6.line_num,
            "code": LINE_OBJECT_6.line_text,
            "total_runtime": LINE_OBJECT_6.total_run_time,
            "total_memory": LINE_OBJECT_6.total_memory,
            "percent_runtime": LINE_OBJECT_6.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_6.memory_percentage_of_total
        }, {
            "fileName": LINE_OBJECT_7.filename,
            "line_num": LINE_OBJECT_7.line_num,
            "code": LINE_OBJECT_7.line_text,
            "total_runtime": LINE_OBJECT_7.total_run_time,
            "total_memory": LINE_OBJECT_7.total_memory,
            "percent_runtime": LINE_OBJECT_7.time_percentage_of_total,
            "percent_memory": LINE_OBJECT_7.memory_percentage_of_total
        }]],
        "e2e": {
            "e2e_runtime": [{
                "n": 1,
                "total_runtime": round(math.log(round(TEST_RESULT_1.total_runtime_ms, 2) if round(TEST_RESULT_1.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[1], 2) if round(fit_data_runtime.O_1[1], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[1], 2) if round(fit_data_runtime.O_logn[1], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[1], 2) if round(fit_data_runtime.O_n[1], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[1], 2) if round(fit_data_runtime.O_n2[1], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[1], 2) if round(fit_data_runtime.O_n3[1], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[1], 2) if round(fit_data_runtime.O_nlogn[1], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[1], 2) if round(fit_data_runtime.O_nn[1], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[1], 2) if round(fit_data_runtime.O_n_fact[1], 2) > 1 else 1), 2)
            }, {
                "n": 2,
                "total_runtime": round(math.log(round(TEST_RESULT_2.total_runtime_ms, 2) if round(TEST_RESULT_2.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[2], 2) if round(fit_data_runtime.O_1[2], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[2], 2) if round(fit_data_runtime.O_logn[2], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[2], 2) if round(fit_data_runtime.O_n[2], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[2], 2) if round(fit_data_runtime.O_n2[2], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[2], 2) if round(fit_data_runtime.O_n3[2], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[2], 2) if round(fit_data_runtime.O_nlogn[2], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[2], 2) if round(fit_data_runtime.O_nn[2], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[2], 2) if round(fit_data_runtime.O_n_fact[2], 2) > 1 else 1), 2)
            }, {
                "n": 3,
                "total_runtime": round(math.log(round(TEST_RESULT_3.total_runtime_ms, 2) if round(TEST_RESULT_3.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[3], 2) if round(fit_data_runtime.O_1[3], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[3], 2) if round(fit_data_runtime.O_logn[3], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[3], 2) if round(fit_data_runtime.O_n[3], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[3], 2) if round(fit_data_runtime.O_n2[3], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[3], 2) if round(fit_data_runtime.O_n3[3], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[3], 2) if round(fit_data_runtime.O_nlogn[3], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[3], 2) if round(fit_data_runtime.O_nn[3], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[3], 2) if round(fit_data_runtime.O_n_fact[3], 2) > 1 else 1), 2)
            }, {
                "n": 10,
                "total_runtime": round(math.log(round(TEST_RESULT_4.total_runtime_ms, 2) if round(TEST_RESULT_4.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[10], 2) if round(fit_data_runtime.O_1[10], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[10], 2) if round(fit_data_runtime.O_logn[10], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[10], 2) if round(fit_data_runtime.O_n[10], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[10], 2) if round(fit_data_runtime.O_n2[10], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[10], 2) if round(fit_data_runtime.O_n3[10], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[10], 2) if round(fit_data_runtime.O_nlogn[10], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[10], 2) if round(fit_data_runtime.O_nn[10], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[10], 2) if round(fit_data_runtime.O_n_fact[10], 2) > 1 else 1), 2)
            }, {
                "n": 5,
                "total_runtime": round(math.log(round(TEST_RESULT_5.total_runtime_ms, 2) if round(TEST_RESULT_5.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[5], 2) if round(fit_data_runtime.O_1[5], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[5], 2) if round(fit_data_runtime.O_logn[5], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[5], 2) if round(fit_data_runtime.O_n[5], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[5], 2) if round(fit_data_runtime.O_n2[5], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[5], 2) if round(fit_data_runtime.O_n3[5], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[5], 2) if round(fit_data_runtime.O_nlogn[5], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[5], 2) if round(fit_data_runtime.O_nn[5], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[5], 2) if round(fit_data_runtime.O_n_fact[5], 2) > 1 else 1), 2)
            }, {
                "n": 20,
                "total_runtime": round(math.log(round(TEST_RESULT_6.total_runtime_ms, 2) if round(TEST_RESULT_6.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[20], 2) if round(fit_data_runtime.O_1[20], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[20], 2) if round(fit_data_runtime.O_logn[20], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[20], 2) if round(fit_data_runtime.O_n[20], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[20], 2) if round(fit_data_runtime.O_n2[20], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[20], 2) if round(fit_data_runtime.O_n3[20], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[20], 2) if round(fit_data_runtime.O_nlogn[20], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[20], 2) if round(fit_data_runtime.O_nn[20], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[20], 2) if round(fit_data_runtime.O_n_fact[20], 2) > 1 else 1), 2)
            }, {
                "n": 9,
                "total_runtime": round(math.log(round(TEST_RESULT_7.total_runtime_ms, 2) if round(TEST_RESULT_7.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[9], 2) if round(fit_data_runtime.O_1[9], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[9], 2) if round(fit_data_runtime.O_logn[9], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[9], 2) if round(fit_data_runtime.O_n[9], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[9], 2) if round(fit_data_runtime.O_n2[9], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[9], 2) if round(fit_data_runtime.O_n3[9], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[9], 2) if round(fit_data_runtime.O_nlogn[9], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[9], 2) if round(fit_data_runtime.O_nn[9], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[9], 2) if round(fit_data_runtime.O_n_fact[9], 2) > 1 else 1), 2)
            }, {
                "n": 15,
                "total_runtime": round(math.log(round(TEST_RESULT_8.total_runtime_ms, 2) if round(TEST_RESULT_8.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[15], 2) if round(fit_data_runtime.O_1[15], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[15], 2) if round(fit_data_runtime.O_logn[15], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[15], 2) if round(fit_data_runtime.O_n[15], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[15], 2) if round(fit_data_runtime.O_n2[15], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[15], 2) if round(fit_data_runtime.O_n3[15], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[15], 2) if round(fit_data_runtime.O_nlogn[15], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[15], 2) if round(fit_data_runtime.O_nn[15], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[15], 2) if round(fit_data_runtime.O_n_fact[15], 2) > 1 else 1), 2)
            }, {
                "n": 50,
                "total_runtime": round(math.log(round(TEST_RESULT_9.total_runtime_ms, 2) if round(TEST_RESULT_9.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[50], 2) if round(fit_data_runtime.O_1[50], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[50], 2) if round(fit_data_runtime.O_logn[50], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[50], 2) if round(fit_data_runtime.O_n[50], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[50], 2) if round(fit_data_runtime.O_n2[50], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[50], 2) if round(fit_data_runtime.O_n3[50], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[50], 2) if round(fit_data_runtime.O_nlogn[50], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[50], 2) if round(fit_data_runtime.O_nn[50], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[50], 2) if round(fit_data_runtime.O_n_fact[50], 2) > 1 else 1), 2)
            }, {
                "n": 12,
                "total_runtime": round(math.log(round(TEST_RESULT_10.total_runtime_ms, 2) if round(TEST_RESULT_10.total_runtime_ms, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_runtime.O_1[12], 2) if round(fit_data_runtime.O_1[12], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_runtime.O_logn[12], 2) if round(fit_data_runtime.O_logn[12], 2) > 1 else 1),2),
                "O(n)": round(math.log(round(fit_data_runtime.O_n[12], 2) if round(fit_data_runtime.O_n[12], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_runtime.O_n2[12], 2) if round(fit_data_runtime.O_n2[12], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_runtime.O_n3[12], 2) if round(fit_data_runtime.O_n3[12], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_runtime.O_nlogn[12], 2) if round(fit_data_runtime.O_nlogn[12], 2) > 1 else 1),2),
                "O(n\u207F)": round(math.log(round(fit_data_runtime.O_nn[12], 2) if round(fit_data_runtime.O_nn[12], 2) > 1 else 1), 2),
                "O(n!)": round(math.log( round(fit_data_runtime.O_n_fact[12], 2) if round(fit_data_runtime.O_n_fact[12], 2) > 1 else 1), 2)
            }],
            "e2e_memory": [{
                "n": 1,
                "total_memory": round(math.log(round(TEST_RESULT_1.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_1.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[1] / 10**6, 2) if round(fit_data_memory.O_1[1], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[1] / 10**6, 2) if round(fit_data_memory.O_logn[1], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[1] / 10**6, 2) if round(fit_data_memory.O_n[1], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[1] / 10**6, 2) if round(fit_data_memory.O_n2[1], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[1] / 10**6, 2) if round(fit_data_memory.O_n3[1], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[1] / 10**6, 2) if round(fit_data_memory.O_nlogn[1], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[1] / 10**6, 2) if round(fit_data_memory.O_nn[1], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[1] / 10**6, 2) if round(fit_data_memory.O_n_fact[1], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_1.memory_usage_by_time
            }, {
                "n": 2,
                "total_memory": round(math.log(round(TEST_RESULT_2.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_2.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[2] / 10**6, 2) if round(fit_data_memory.O_1[2], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[2] / 10**6, 2) if round(fit_data_memory.O_logn[2], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[2] / 10**6, 2) if round(fit_data_memory.O_n[2], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[2] / 10**6, 2) if round(fit_data_memory.O_n2[2], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[2] / 10**6, 2) if round(fit_data_memory.O_n3[2], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[2] / 10**6, 2) if round(fit_data_memory.O_nlogn[2], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[2] / 10**6, 2) if round(fit_data_memory.O_nn[2], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[2] / 10**6, 2) if round(fit_data_memory.O_n_fact[2], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_2.memory_usage_by_time
            }, {
                "n": 3,
                "total_memory": round(math.log(round(TEST_RESULT_3.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_3.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[3] / 10**6, 2) if round(fit_data_memory.O_1[3], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[3] / 10**6, 2) if round(fit_data_memory.O_logn[3], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[3] / 10**6, 2) if round(fit_data_memory.O_n[3], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[3] / 10**6, 2) if round(fit_data_memory.O_n2[3], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[3] / 10**6, 2) if round(fit_data_memory.O_n3[3], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[3] / 10**6, 2) if round(fit_data_memory.O_nlogn[3], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[3] / 10**6, 2) if round(fit_data_memory.O_nn[3], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[3] / 10**6, 2) if round(fit_data_memory.O_n_fact[3], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_3.memory_usage_by_time
            }, {
                "n": 10,
                "total_memory": round(math.log(round(TEST_RESULT_4.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_4.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[10] / 10**6, 2) if round(fit_data_memory.O_1[10], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[10] / 10**6, 2) if round(fit_data_memory.O_logn[10], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[10] / 10**6, 2) if round(fit_data_memory.O_n[10], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[10] / 10**6, 2) if round(fit_data_memory.O_n2[10], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[10] / 10**6, 2) if round(fit_data_memory.O_n3[10], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[10] / 10**6, 2) if round(fit_data_memory.O_nlogn[10], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[10] / 10**6, 2) if round(fit_data_memory.O_nn[10], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[10] / 10**6, 2) if round(fit_data_memory.O_n_fact[10], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_4.memory_usage_by_time
            }, {
                "n": 5,
                "total_memory": round(math.log(round(TEST_RESULT_5.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_5.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[5] / 10**6, 2) if round(fit_data_memory.O_1[5], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[5] / 10**6, 2) if round(fit_data_memory.O_logn[5], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[5] / 10**6, 2) if round(fit_data_memory.O_n[5], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[5] / 10**6, 2) if round(fit_data_memory.O_n2[5], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[5] / 10**6, 2) if round(fit_data_memory.O_n3[5], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[5] / 10**6, 2) if round(fit_data_memory.O_nlogn[5], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[5] / 10**6, 2) if round(fit_data_memory.O_nn[5], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[5] / 10**6, 2) if round(fit_data_memory.O_n_fact[5], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_5.memory_usage_by_time
            }, {
                "n": 20,
                "total_memory": round(math.log(round(TEST_RESULT_6.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_6.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[20] / 10**6, 2) if round(fit_data_memory.O_1[20], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[20] / 10**6, 2) if round(fit_data_memory.O_logn[20], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[20] / 10**6, 2) if round(fit_data_memory.O_n[20], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[20] / 10**6, 2) if round(fit_data_memory.O_n2[20], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[20] / 10**6, 2) if round(fit_data_memory.O_n3[20], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[20] / 10**6, 2) if round(fit_data_memory.O_nlogn[20], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[20] / 10**6, 2) if round(fit_data_memory.O_nn[20], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[20] / 10**6, 2) if round(fit_data_memory.O_n_fact[20], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_6.memory_usage_by_time
            }, {
                "n": 9,
                "total_memory": round(math.log(round(TEST_RESULT_7.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_7.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[9] / 10**6, 2) if round(fit_data_memory.O_1[9], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[9] / 10**6, 2) if round(fit_data_memory.O_logn[9], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[9] / 10**6, 2) if round(fit_data_memory.O_n[9], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[9] / 10**6, 2) if round(fit_data_memory.O_n2[9], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[9] / 10**6, 2) if round(fit_data_memory.O_n3[9], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[9] / 10**6, 2) if round(fit_data_memory.O_nlogn[9], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[9] / 10**6, 2) if round(fit_data_memory.O_nn[9], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[9] / 10**6, 2) if round(fit_data_memory.O_n_fact[9], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_7.memory_usage_by_time
            }, {
                "n": 15,
                "total_memory": round(math.log(round(TEST_RESULT_8.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_8.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[15] / 10**6, 2) if round(fit_data_memory.O_1[15], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[15] / 10**6, 2) if round(fit_data_memory.O_logn[15], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[15] / 10**6, 2) if round(fit_data_memory.O_n[15], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[15] / 10**6, 2) if round(fit_data_memory.O_n2[15], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[15] / 10**6, 2) if round(fit_data_memory.O_n3[15], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[15] / 10**6, 2) if round(fit_data_memory.O_nlogn[15], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[15] / 10**6, 2) if round(fit_data_memory.O_nn[15], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[15] / 10**6, 2) if round(fit_data_memory.O_n_fact[15], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_8.memory_usage_by_time
            }, {
                "n": 50,
                "total_memory": round(math.log(round(TEST_RESULT_9.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_9.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[50] / 10**6, 2) if round(fit_data_memory.O_1[50], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[50] / 10**6, 2) if round(fit_data_memory.O_logn[50], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[50] / 10**6, 2) if round(fit_data_memory.O_n[50], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[50] / 10**6, 2) if round(fit_data_memory.O_n2[50], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[50] / 10**6, 2) if round(fit_data_memory.O_n3[50], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[50] / 10**6, 2) if round(fit_data_memory.O_nlogn[50], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[50] / 10**6, 2) if round(fit_data_memory.O_nn[50], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[50] / 10**6, 2) if round(fit_data_memory.O_n_fact[50], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_9.memory_usage_by_time
            }, {
                "n": 12,
                "total_memory": round(math.log(round(TEST_RESULT_10.max_memory_usage_bytes / 10**6, 2) if round(TEST_RESULT_10.max_memory_usage_bytes, 2) > 1 else 1), 2),
                "O(1)": round(math.log(round(fit_data_memory.O_1[12] / 10**6, 2) if round(fit_data_memory.O_1[12], 2) > 1 else 1), 2),
                "O(log(n))": round(math.log(round(fit_data_memory.O_logn[12] / 10**6, 2) if round(fit_data_memory.O_logn[12], 2) > 1 else 1), 2),
                "O(n)": round(math.log(round(fit_data_memory.O_n[12] / 10**6, 2) if round(fit_data_memory.O_n[12], 2) > 1 else 1), 2),
                "O(n\u00B2)": round(math.log(round(fit_data_memory.O_n2[12] / 10**6, 2) if round(fit_data_memory.O_n2[12], 2) > 1 else 1), 2),
                "O(n\u00B3)": round(math.log(round(fit_data_memory.O_n3[12] / 10**6, 2) if round(fit_data_memory.O_n3[12], 2) > 1 else 1), 2),
                "O(nlog(n))": round(math.log(round(fit_data_memory.O_nlogn[12] / 10**6, 2) if round(fit_data_memory.O_nlogn[12], 2) > 1 else 1), 2),
                "O(n\u207F)": round(math.log(round(fit_data_memory.O_nn[12] / 10**6, 2) if round(fit_data_memory.O_nn[12], 2) > 1 else 1), 2),
                "O(n!)": round(math.log(round(fit_data_memory.O_n_fact[12] / 10**6, 2) if round(fit_data_memory.O_n_fact[12], 2) > 1 else 1), 2),
                "memory_usage_by_time": TEST_RESULT_10.memory_usage_by_time
            }],
            "e2e_highest_runtime_function": "getSpeed()",
            "e2e_highest_memory_usage_function": "getPosition()",
            "e2e_total_average_time": 348.9,
            "e2e_total_average_memory": 12.7,
            "e2e_time_complexity": "n2",
            "e2e_space_complexity": "n"
        },
        "sankey": {
            "sankey_runtime": {
                "nodes": [
                    {"name": "test.py"},
                    {"name": "Speedometer"},
                    {"name": "getSpeed()"},
                    {"name": "getPosition()"},
                ],
                "links": [
                    {"source": 0, "target": 1, "value": 100},
                    {"source": 1, "target": 2, "value": 50.39},
                    {"source": 1, "target": 3, "value": 49.61},
                ]
            },
            "sankey_memory": {
                "nodes": [
                    {"name": "test.py"},
                    {"name": "Speedometer"},
                    {"name": "getSpeed()"},
                    {"name": "getPosition()"},
                ],
                "links": [
                    {"source": 0, "target": 1, "value": 100},
                    {"source": 1, "target": 2, "value": 31.25},
                    {"source": 1, "target": 3, "value": 68.75},
                ]
            }
        }
    }

    # @pytest.fixture(autouse=True)
    # def before_each(self):
    #     self.e2e_analyzer = EndToEndAnalyzer()

    def test_build(self):
        assert self.compare_object(self.output, build_visualization("test.py", self.profile_result, self.e2e_result))

    def compare_object(self, obj1: dict, obj2: dict) -> bool:
        if len(obj1.keys()) != len(obj2.keys()):
            print("Len Obj: ", obj1.keys(), obj2.keys())
            return False
        for k in obj1:
            if isinstance(obj1[k], dict):
                if isinstance(obj2[k], dict):
                    if not self.compare_object(obj1[k], obj2[k]):
                        return False
                else:
                    print("Compare Obj: ", k, obj1[k], obj2[k], obj1, obj2)
                    return False
            else:
                if isinstance(obj1[k], list):
                    if isinstance(obj2[k], list):
                        if not self.compare_arrays(obj1[k], obj2[k]):
                            return False
                    else:
                        print("Compare Obj2: ", k, obj1[k], obj2[k], obj1, obj2)
                        return False
                else:
                    if not obj1[k] == obj2[k]:
                        print("Obj Eq: ", k, obj1[k], obj2[k], obj1, obj2)
                        return False
        return True

    def compare_arrays(self, obj1: list, obj2: list) -> bool:
        if len(obj1) != len(obj2):
            print("Len list: ", obj1, obj2)
            return False
        for k in range(len(obj1)):
            if isinstance(obj1[k], dict):
                if isinstance(obj2[k], dict):
                    if not self.compare_object(obj1[k], obj2[k]):
                        return False
                else:
                    print("Compare List: ", k, obj1[k], obj2[k], obj1, obj2)
                    return False
            else:
                if isinstance(obj1[k], list):
                    if isinstance(obj2[k], list):
                        if not self.compare_arrays(obj1[k], obj2[k]):
                            return False
                    else:
                        print("Compare List2: ", k, obj1[k], obj2[k], obj1, obj2)
                        return False
                else:
                    if not obj1[k] == obj2[k]:
                        print("List Eq: ", k, obj1[k], obj2[k], obj1, obj2)
                        return False
        return True

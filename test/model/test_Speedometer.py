import math
import numpy as np

from src.model.Speedometer import Speedometer
from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult
from src.model.analyzers.profile_analysis.ProfileAnalyzer import class_runtime
from src.model.analyzers.profile_analysis.ProfileAnalyzer import function_runtime
from src.model.analyzers.profile_analysis.ProfileAnalyzer import line_by_line_runtime
from src.model.visualization_builders.BuildVisualization import build_visualization


class TestBuildVisualization:

    TEST_RESULT_1 = TestResult(
        1,
        1,
        {0: 10, 1: 20, 2: 30, 3: 40}
    )

    TEST_RESULT_2 = TestResult(
        4,
        2,
        {0: 20, 1: 30, 2: 40, 3: 50.5, 4: 100.1}
    )

    TEST_RESULT_3 = TestResult(
        9,
        3,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_4 = TestResult(
        100,
        10,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_5 = TestResult(
        25,
        5,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_6 = TestResult(
        400,
        20,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_7 = TestResult(
        81,
        9,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_8 = TestResult(
        225,
        15,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_9 = TestResult(
        2500,
        50,
        {0: 3, 1: 7, 2: 11}
    )

    TEST_RESULT_10 = TestResult(
        144,
        12,
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

    O_1t = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 0)
    O_nt = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 1)
    O_n2t = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 2)
    O_n3t = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 3)
    O_1m = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 0)
    O_nm = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 1)
    O_n2m = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 2)
    O_n3m = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 3)
    O_logn = 1
    O_nlogn = 1
    O_nn = 1
    O_nfact = 1

    output = {
        "script_name": "test.py",
        "class": {
            'class_runtime': [{
              'name': 'test.py/Speedometer',
              'total_runtime': CLASS_OBJECT_1.total_run_time
            }],
            'class_memory': [{
                'name': 'test.py/Speedometer',
                'total_memory': CLASS_OBJECT_1.total_memory
            }]},
        "function": {
            'function_runtime': [{
              'name': 'test.py/getSpeed()',
              'total_runtime': FUN_OBJECT_1.total_run_time
            }, {
              'name': 'test.py/getPosition()',
              'total_runtime': FUN_OBJECT_2.total_run_time
            }],
            'function_memory': [{
              'name': 'test.py/getSpeed()',
              'total_runtime': FUN_OBJECT_1.total_memory
            }, {
              'name': 'test.py/getPosition()',
              'total_runtime': FUN_OBJECT_2.total_memory
            }]},
        "line_by_line": [{
            "fileName": LINE_OBJECT_1.filename,
            "line_num": LINE_OBJECT_1.line_num,
            "code": LINE_OBJECT_1.line_text,
            "total_runtime": LINE_OBJECT_1.total_run_time,
            "total_memory": LINE_OBJECT_1.total_memory
        }, {
            "fileName": LINE_OBJECT_2.filename,
            "line_num": LINE_OBJECT_2.line_num,
            "code": LINE_OBJECT_2.line_text,
            "total_runtime": LINE_OBJECT_2.total_run_time,
            "total_memory": LINE_OBJECT_2.total_memory
        }, {
            "fileName": LINE_OBJECT_3.filename,
            "line_num": LINE_OBJECT_3.line_num,
            "code": LINE_OBJECT_3.line_text,
            "total_runtime": LINE_OBJECT_3.total_run_time,
            "total_memory": LINE_OBJECT_3.total_memory
        }, {
            "fileName": LINE_OBJECT_4.filename,
            "line_num": LINE_OBJECT_4.line_num,
            "code": LINE_OBJECT_4.line_text,
            "total_runtime": LINE_OBJECT_4.total_run_time,
            "total_memory": LINE_OBJECT_4.total_memory
        }, {
            "fileName": LINE_OBJECT_5.filename,
            "line_num": LINE_OBJECT_5.line_num,
            "code": LINE_OBJECT_5.line_text,
            "total_runtime": LINE_OBJECT_5.total_run_time,
            "total_memory": LINE_OBJECT_5.total_memory
        }, {
            "fileName": LINE_OBJECT_6.filename,
            "line_num": LINE_OBJECT_6.line_num,
            "code": LINE_OBJECT_6.line_text,
            "total_runtime": LINE_OBJECT_6.total_run_time,
            "total_memory": LINE_OBJECT_6.total_memory
        }, {
            "fileName": LINE_OBJECT_7.filename,
            "line_num": LINE_OBJECT_7.line_num,
            "code": LINE_OBJECT_7.line_text,
            "total_runtime": LINE_OBJECT_7.total_run_time,
            "total_memory": LINE_OBJECT_7.total_memory
        }],
        "e2e": {
            "e2e_runtime": [{
                "n": 1,
                "total_runtime": TEST_RESULT_1.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(1),
                "O(n)": O_nt[0]*1+O_nt[1],
                "O(n\u00B2)": O_n2t[0]*1**2+O_n2t[1]*1+O_n2t[2],
                "O(n\u00B3)": O_n3t[0]*1**3+O_n3t[1]*1**2+O_n3t[2]*1+O_n3t[3],
                "O(nlog(n))": 1*math.log(1),
                "O(n\u207F)": 1**1,
                "O(n!)": math.factorial(1)
            }, {
                "n": 2,
                "total_runtime": TEST_RESULT_2.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(2),
                "O(n)": O_nt[0]*2+O_nt[1],
                "O(n\u00B2)": O_n2t[0]*2**2+O_n2t[1]*2+O_n2t[2],
                "O(n\u00B3)": O_n3t[0]*2**3+O_n3t[1]*2**2+O_n3t[2]*2+O_n3t[3],
                "O(nlog(n))": 2*math.log(2),
                "O(n\u207F)": 2**2,
                "O(n!)": math.factorial(2)
            }, {
                "n": 3,
                "total_runtime": TEST_RESULT_3.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(3),
                "O(n)": O_nt[0]*3+O_nt[1],
                "O(n\u00B2)": O_n2t[0]*3**2+O_n2t[1]*3+O_n2t[2],
                "O(n\u00B3)": O_n3t[0]*3**3+O_n3t[1]*3**2+O_n3t[2]*3+O_n3t[3],
                "O(nlog(n))": 3*math.log(3),
                "O(n\u207F)": 3**3,
                "O(n!)": math.factorial(3)
            }, {
                "n": 10,
                "total_runtime": TEST_RESULT_4.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(10),
                "O(n)": O_nt[0] * 10 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 10 ** 2 + O_n2t[1] * 10 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 10 ** 3 + O_n3t[1] * 10 ** 2 + O_n3t[2] * 10 + O_n3t[3],
                "O(nlog(n))": 10 * math.log(10),
                "O(n\u207F)": 10 ** 10,
                "O(n!)": math.factorial(10)
            }, {
                "n": 5,
                "total_runtime": TEST_RESULT_5.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(5),
                "O(n)": O_nt[0] * 5 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 5 ** 2 + O_n2t[1] * 5 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 5 ** 3 + O_n3t[1] * 5 ** 2 + O_n3t[2] * 5 + O_n3t[3],
                "O(nlog(n))": 5 * math.log(5),
                "O(n\u207F)": 5 ** 5,
                "O(n!)": math.factorial(5)
            }, {
                "n": 20,
                "total_runtime": TEST_RESULT_6.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(20),
                "O(n)": O_nt[0] * 20 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 20 ** 2 + O_n2t[1] * 20 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 20 ** 3 + O_n3t[1] * 20 ** 2 + O_n3t[2] * 20 + O_n3t[3],
                "O(nlog(n))": 20 * math.log(20),
                "O(n\u207F)": 20 ** 20,
                "O(n!)": math.factorial(20)
            }, {
                "n": 9,
                "total_runtime": TEST_RESULT_7.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(9),
                "O(n)": O_nt[0] * 9 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 9 ** 2 + O_n2t[1] * 9 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 9 ** 3 + O_n3t[1] * 9 ** 2 + O_n3t[2] * 9 + O_n3t[3],
                "O(nlog(n))": 9 * math.log(9),
                "O(n\u207F)": 9 ** 9,
                "O(n!)": math.factorial(9)
            }, {
                "n": 15,
                "total_runtime": TEST_RESULT_8.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(15),
                "O(n)": O_nt[0] * 15 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 15 ** 2 + O_n2t[1] * 15 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 15 ** 3 + O_n3t[1] * 15 ** 2 + O_n3t[2] * 15 + O_n3t[3],
                "O(nlog(n))": 15 * math.log(15),
                "O(n\u207F)": 15 ** 15,
                "O(n!)": math.factorial(15)
            }, {
                "n": 50,
                "total_runtime": TEST_RESULT_9.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(50),
                "O(n)": O_nt[0] * 50 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 50 ** 2 + O_n2t[1] * 50 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 50 ** 3 + O_n3t[1] * 50 ** 2 + O_n3t[2] * 50 + O_n3t[3],
                "O(nlog(n))": 50 * math.log(50),
                "O(n\u207F)": 50 ** 50,
                "O(n!)": math.factorial(50)
            }, {
                "n": 12,
                "total_runtime": TEST_RESULT_10.total_runtime_ms,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(12),
                "O(n)": O_nt[0] * 12 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 12 ** 2 + O_n2t[1] * 12 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 12 ** 3 + O_n3t[1] * 12 ** 2 + O_n3t[2] * 12 + O_n3t[3],
                "O(nlog(n))": 12 * math.log(12),
                "O(n\u207F)": 12 ** 12,
                "O(n!)": math.factorial(12)
            }],
            "e2e_memory": [{
                "n": 1,
                "total_runtime": TEST_RESULT_1.max_memory_usage_bytes,
                "O(1)": O_1m[0],
                "O(log(n))": math.log(1),
                "O(n)": O_nm[0]*1+O_nm[1],
                "O(n\u00B2)": O_n2m[0]*1**2+O_n2m[1]*1+O_n2m[2],
                "O(n\u00B3)": O_n3m[0]*1**3+O_n3m[1]*1**2+O_n3m[2]*1+O_n3m[3],
                "O(nlog(n))": 1*math.log(1),
                "O(n\u207F)": 1**1,
                "O(n!)": math.factorial(1),
                "memory_usage_by_time": TEST_RESULT_1.memory_usage_by_time
            }, {
                "n": 2,
                "total_runtime": TEST_RESULT_2.max_memory_usage_bytes,
                "O(1)": O_1m[0],
                "O(log(n))": math.log(2),
                "O(n)": O_nm[0]*2+O_nm[1],
                "O(n\u00B2)": O_n2m[0]*2**2+O_n2m[1]*2+O_n2m[2],
                "O(n\u00B3)": O_n3m[0]*2**3+O_n3m[1]*2**2+O_n3m[2]*2+O_n3m[3],
                "O(nlog(n))": 2*math.log(2),
                "O(n\u207F)": 2**2,
                "O(n!)": math.factorial(2),
                "memory_usage_by_time": TEST_RESULT_2.memory_usage_by_time
            }, {
                "n": 3,
                "total_runtime": TEST_RESULT_3.max_memory_usage_bytes,
                "O(1)": O_1m[0],
                "O(log(n))": math.log(3),
                "O(n)": O_nm[0]*3+O_nm[1],
                "O(n\u00B2)": O_n2m[0]*3**2+O_n2m[1]*3+O_n2m[2],
                "O(n\u00B3)": O_n3m[0]*3**3+O_n3m[1]*3**2+O_n3m[2]*3+O_n3m[3],
                "O(nlog(n))": 3*math.log(3),
                "O(n\u207F)": 3**3,
                "O(n!)": math.factorial(3),
                "memory_usage_by_time": TEST_RESULT_3.memory_usage_by_time
            }, {
                "n": 10,
                "total_runtime": TEST_RESULT_4.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(10),
                "O(n)": O_nt[0] * 10 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 10 ** 2 + O_n2t[1] * 10 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 10 ** 3 + O_n3t[1] * 10 ** 2 + O_n3t[2] * 10 + O_n3t[3],
                "O(nlog(n))": 10 * math.log(10),
                "O(n\u207F)": 10 ** 10,
                "O(n!)": math.factorial(10),
                "memory_usage_by_time": TEST_RESULT_4.memory_usage_by_time
            }, {
                "n": 5,
                "total_runtime": TEST_RESULT_5.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(5),
                "O(n)": O_nt[0] * 5 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 5 ** 2 + O_n2t[1] * 5 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 5 ** 3 + O_n3t[1] * 5 ** 2 + O_n3t[2] * 5 + O_n3t[3],
                "O(nlog(n))": 5 * math.log(5),
                "O(n\u207F)": 5 ** 5,
                "O(n!)": math.factorial(5),
                "memory_usage_by_time": TEST_RESULT_5.memory_usage_by_time
            }, {
                "n": 20,
                "total_runtime": TEST_RESULT_6.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(20),
                "O(n)": O_nt[0] * 20 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 20 ** 2 + O_n2t[1] * 20 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 20 ** 3 + O_n3t[1] * 20 ** 2 + O_n3t[2] * 20 + O_n3t[3],
                "O(nlog(n))": 20 * math.log(20),
                "O(n\u207F)": 20 ** 20,
                "O(n!)": math.factorial(20),
                "memory_usage_by_time": TEST_RESULT_6.memory_usage_by_time
            }, {
                "n": 9,
                "total_runtime": TEST_RESULT_7.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(9),
                "O(n)": O_nt[0] * 9 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 9 ** 2 + O_n2t[1] * 9 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 9 ** 3 + O_n3t[1] * 9 ** 2 + O_n3t[2] * 9 + O_n3t[3],
                "O(nlog(n))": 9 * math.log(9),
                "O(n\u207F)": 9 ** 9,
                "O(n!)": math.factorial(9),
                "memory_usage_by_time": TEST_RESULT_7.memory_usage_by_time
            }, {
                "n": 15,
                "total_runtime": TEST_RESULT_8.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(15),
                "O(n)": O_nt[0] * 15 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 15 ** 2 + O_n2t[1] * 15 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 15 ** 3 + O_n3t[1] * 15 ** 2 + O_n3t[2] * 15 + O_n3t[3],
                "O(nlog(n))": 15 * math.log(15),
                "O(n\u207F)": 15 ** 15,
                "O(n!)": math.factorial(15),
                "memory_usage_by_time": TEST_RESULT_8.memory_usage_by_time
            }, {
                "n": 50,
                "total_runtime": TEST_RESULT_9.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(50),
                "O(n)": O_nt[0] * 50 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 50 ** 2 + O_n2t[1] * 50 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 50 ** 3 + O_n3t[1] * 50 ** 2 + O_n3t[2] * 50 + O_n3t[3],
                "O(nlog(n))": 50 * math.log(50),
                "O(n\u207F)": 50 ** 50,
                "O(n!)": math.factorial(50),
                "memory_usage_by_time": TEST_RESULT_9.memory_usage_by_time
            }, {
                "n": 12,
                "total_runtime": TEST_RESULT_10.max_memory_usage_bytes,
                "O(1)": O_1t[0],
                "O(log(n))": math.log(12),
                "O(n)": O_nt[0] * 12 + O_nt[1],
                "O(n\u00B2)": O_n2t[0] * 12 ** 2 + O_n2t[1] * 12 + O_n2t[2],
                "O(n\u00B3)": O_n3t[0] * 12 ** 3 + O_n3t[1] * 12 ** 2 + O_n3t[2] * 12 + O_n3t[3],
                "O(nlog(n))": 12 * math.log(12),
                "O(n\u207F)": 12 ** 12,
                "O(n!)": math.factorial(12),
                "memory_usage_by_time": TEST_RESULT_10.memory_usage_by_time
            }],
            "e2e_highest_runtime_function": "getSpeed()",
            "e2e_highest_memory_usage_function": "getPosition()",
            "e2e_total_average_time": 1098.9,
            "e2e_total_average_memory": 17.7,
            "e2e_time_complexity": "n2",
            "e2e_space_complexity": "n"
        }
    }

    e2e_result = {
        1: InputSizeResult(TEST_RESULT_1,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
        2: InputSizeResult(TEST_RESULT_2,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
        3: InputSizeResult(TEST_RESULT_3,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
        10: InputSizeResult(TEST_RESULT_4, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        5: InputSizeResult(TEST_RESULT_5, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        20: InputSizeResult(TEST_RESULT_6, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        9: InputSizeResult(TEST_RESULT_7, [TEST_RESULT_7,TEST_RESULT_8,TEST_RESULT_9]),
        15: InputSizeResult(TEST_RESULT_8, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        100: InputSizeResult(TEST_RESULT_9, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6]),
        12: InputSizeResult(TEST_RESULT_10, [TEST_RESULT_4,TEST_RESULT_5,TEST_RESULT_6])
    }
    profile_result = {
        "class": [CLASS_OBJECT_1],
        "function": [FUN_OBJECT_1, FUN_OBJECT_2],
        "line_by_line": [LINE_OBJECT_1, LINE_OBJECT_2, LINE_OBJECT_3, LINE_OBJECT_4, LINE_OBJECT_5, LINE_OBJECT_6, LINE_OBJECT_7]
    }

    # @pytest.fixture(autouse=True)
    # def before_each(self):
    #     self.e2e_analyzer = EndToEndAnalyzer()

    def test_build(self):
        assert self.compare_object(self.output, build_visualization("test.py", self.profile_result, self.e2e_result))

    def compare_object(self, obj1: dict, obj2: dict) -> bool:
        if len(obj1.keys()) != len(obj2.keys()):
            return False
        for k in obj1:
            if obj1[k] is dict:
                if obj2[k] is dict:
                    if not self.compare_object(obj1[k], obj2[k]):
                        return False
                else:
                    return False
            if obj1[k] is list:
                if obj2[k] is list:
                    if not self.compare_arrays(obj1[k], obj2[k]):
                        return False
                else:
                    return False
            if not obj1[k] == obj2[k]:
                return False
        return True

    def compare_arrays(self, obj1: list, obj2: list) -> bool:
        if len(obj1) != len(obj2):
            return False
        for k in range(len(obj1)):
            if obj1[k] is dict:
                if obj2[k] is dict:
                    if not self.compare_object(obj1[k], obj2[k]):
                        return False
                else:
                    return False
            if obj1[k] is list:
                if obj2[k] is list:
                    if not self.compare_arrays(obj1[k], obj2[k]):
                        return False
                else:
                    return False
            if not obj1[k] == obj2[k]:
                return False
        return True

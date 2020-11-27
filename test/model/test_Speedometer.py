# import math
# import numpy as np
#
# from src.model.Speedometer import Speedometer
# from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
# from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult
# from src.model.analyzers.profile_analysis.ProfileAnalyzer import class_runtime
# from src.model.analyzers.profile_analysis.ProfileAnalyzer import function_runtime
# from src.model.analyzers.profile_analysis.ProfileAnalyzer import line_by_line_runtime
#
#
# class TestBuildVisualization:
#
#     TEST_RESULT_1 = TestResult(
#         1,
#         1,
#         {0: 10, 1: 20, 2: 30, 3: 40}
#     )
#
#     TEST_RESULT_2 = TestResult(
#         4,
#         2,
#         {0: 20, 1: 30, 2: 40, 3: 50.5, 4: 100.1}
#     )
#
#     TEST_RESULT_3 = TestResult(
#         9,
#         3,
#         {0: 3, 1: 7, 2: 11}
#     )
#
#     CLASS_OBJECT_1 = class_runtime(
#         "test.py",
#         "Speedometer",
#         46.52,
#         0.5
#     )
#
#     FUN_OBJECT_1 = function_runtime(
#         "test.py",
#         "getSpeed()",
#         23.445,
#         0.1
#     )
#
#     FUN_OBJECT_2 = function_runtime(
#         "test.py",
#         "getPosition()",
#         2.99,
#         0.6
#     )
#
#     LINE_OBJECT_1 = line_by_line_runtime(
#         "test.py",
#         1,
#         0.0,
#         0.0,
#         "def getSpeed():"
#     )
#
#     LINE_OBJECT_2 = line_by_line_runtime(
#         "test.py",
#         2,
#         23.445,
#         0.1,
#         "do lots of things"
#     )
#
#     LINE_OBJECT_3 = line_by_line_runtime(
#         "test.py",
#         3,
#         0.0,
#         0.0,
#         "class Speedometer:"
#     )
#
#     O_1t = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 0)
#     O_nt = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 1)
#     O_n2t = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 2)
#     O_n3t = np.polyfit([1,2,3], [TEST_RESULT_1.total_runtime_ms,TEST_RESULT_2.total_runtime_ms,TEST_RESULT_3.total_runtime_ms], 3)
#     O_1m = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 0)
#     O_nm = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 1)
#     O_n2m = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 2)
#     O_n3m = np.polyfit([1,2,3], [TEST_RESULT_1.max_memory_usage_bytes,TEST_RESULT_2.max_memory_usage_bytes,TEST_RESULT_3.max_memory_usage_bytes], 3)
#     O_logn = 1
#     O_nlogn = 1
#     O_nn = 1
#     O_nfact = 1
#
#     output = {
#         "script_name": "test.py",
#         "class": {
#             'class_runtime': [{
#               'name': 'test.py/Speedometer',
#               'total_runtime': CLASS_OBJECT_1.total_run_time
#             }],
#             'class_memory': [{
#                 'name': 'test.py/Speedometer',
#                 'total_memory': CLASS_OBJECT_1.total_memory
#             }]},
#         "function": {
#             'function_runtime': [{
#               'name': 'test.py/getSpeed()',
#               'total_runtime': FUN_OBJECT_1.total_run_time
#             }, {
#               'name': 'test.py/getPosition()',
#               'total_runtime': FUN_OBJECT_2.total_run_time
#             }],
#             'function_memory': [{
#               'name': 'test.py/getSpeed()',
#               'total_runtime': FUN_OBJECT_1.total_memory
#             }, {
#               'name': 'test.py/getPosition()',
#               'total_runtime': FUN_OBJECT_2.total_memory
#             }]},
#         "line_by_line": [{
#             "fileName": LINE_OBJECT_1.filename,
#             "line_num": LINE_OBJECT_1.line_num,
#             "code": LINE_OBJECT_1.line_text,
#             "total_runtime": LINE_OBJECT_1.total_run_time,
#             "total_memory": LINE_OBJECT_1.total_memory
#         }, {
#             "fileName": LINE_OBJECT_2.filename,
#             "line_num": LINE_OBJECT_2.line_num,
#             "code": LINE_OBJECT_2.line_text,
#             "total_runtime": LINE_OBJECT_2.total_run_time,
#             "total_memory": LINE_OBJECT_2.total_memory
#         }, {
#             "fileName": LINE_OBJECT_3.filename,
#             "line_num": LINE_OBJECT_3.line_num,
#             "code": LINE_OBJECT_3.line_text,
#             "total_runtime": LINE_OBJECT_3.total_run_time,
#             "total_memory": LINE_OBJECT_3.total_memory
#         }],
#         "e2e": {
#             "e2e_runtime": [{
#                 "n": 1,
#                 "total_runtime": TEST_RESULT_1.total_runtime_ms,
#                 "O(1)": O_1t[0],
#                 "O(log(n))": math.log(1),
#                 "O(n)": O_nt[0]*1+O_nt[1],
#                 "O(n\u00B2)": O_n2t[0]*1**2+O_n2t[1]*1+O_n2t[2],
#                 "O(n\u00B3)": O_n3t[0]*1**3+O_n3t[1]*1**2+O_n3t[2]*1+O_n3t[3],
#                 "O(nlog(n))": 1*math.log(1),
#                 "O(n\u207F)": 1**1,
#                 "O(n!)": math.factorial(1)
#             }, {
#                 "n": 2,
#                 "total_runtime": TEST_RESULT_2.total_runtime_ms,
#                 "O(1)": O_1t[0],
#                 "O(log(n))": math.log(2),
#                 "O(n)": O_nt[0]*2+O_nt[1],
#                 "O(n\u00B2)": O_n2t[0]*2**2+O_n2t[1]*2+O_n2t[2],
#                 "O(n\u00B3)": O_n3t[0]*2**3+O_n3t[1]*2**2+O_n3t[2]*2+O_n3t[3],
#                 "O(nlog(n))": 2*math.log(2),
#                 "O(n\u207F)": 2**2,
#                 "O(n!)": math.factorial(2)
#             }, {
#                 "n": 3,
#                 "total_runtime": TEST_RESULT_3.total_runtime_ms,
#                 "O(1)": O_1t[0],
#                 "O(log(n))": math.log(3),
#                 "O(n)": O_nt[0]*3+O_nt[1],
#                 "O(n\u00B2)": O_n2t[0]*3**2+O_n2t[1]*3+O_n2t[2],
#                 "O(n\u00B3)": O_n3t[0]*3**3+O_n3t[1]*3**2+O_n3t[2]*3+O_n3t[3],
#                 "O(nlog(n))": 3*math.log(3),
#                 "O(n\u207F)": 3**3,
#                 "O(n!)": math.factorial(3)
#             }],
#             "e2e_memory": [{
#                 "n": 1,
#                 "total_runtime": TEST_RESULT_1.max_memory_usage_bytes,
#                 "O(1)": O_1m[0],
#                 "O(log(n))": math.log(1),
#                 "O(n)": O_nm[0]*1+O_nm[1],
#                 "O(n\u00B2)": O_n2m[0]*1**2+O_n2m[1]*1+O_n2m[2],
#                 "O(n\u00B3)": O_n3m[0]*1**3+O_n3m[1]*1**2+O_n3m[2]*1+O_n3m[3],
#                 "O(nlog(n))": 1*math.log(1),
#                 "O(n\u207F)": 1**1,
#                 "O(n!)": math.factorial(1),
#                 "memory_usage_by_time": TEST_RESULT_1.memory_usage_by_time
#             }, {
#                 "n": 2,
#                 "total_runtime": TEST_RESULT_2.max_memory_usage_bytes,
#                 "O(1)": O_1m[0],
#                 "O(log(n))": math.log(2),
#                 "O(n)": O_nm[0]*2+O_nm[1],
#                 "O(n\u00B2)": O_n2m[0]*2**2+O_n2m[1]*2+O_n2m[2],
#                 "O(n\u00B3)": O_n3m[0]*2**3+O_n3m[1]*2**2+O_n3m[2]*2+O_n3m[3],
#                 "O(nlog(n))": 2*math.log(2),
#                 "O(n\u207F)": 2**2,
#                 "O(n!)": math.factorial(2),
#                 "memory_usage_by_time": TEST_RESULT_2.memory_usage_by_time
#             }, {
#                 "n": 3,
#                 "total_runtime": TEST_RESULT_3.max_memory_usage_bytes,
#                 "O(1)": O_1m[0],
#                 "O(log(n))": math.log(3),
#                 "O(n)": O_nm[0]*3+O_nm[1],
#                 "O(n\u00B2)": O_n2m[0]*3**2+O_n2m[1]*3+O_n2m[2],
#                 "O(n\u00B3)": O_n3m[0]*3**3+O_n3m[1]*3**2+O_n3m[2]*3+O_n3m[3],
#                 "O(nlog(n))": 3*math.log(3),
#                 "O(n\u207F)": 3**3,
#                 "O(n!)": math.factorial(3),
#                 "memory_usage_by_time": TEST_RESULT_3.memory_usage_by_time
#             }],
#             "e2e_highest_runtime_function": "getSpeed()",
#             "e2e_highest_memory_usage_function": "getPosition()",
#             "e2e_total_average_time": 14 / 3,
#             "e2e_total_average_memory": 2,
#             "e2e_time_complexity": "n2",
#             "e2e_space_complexity": "n"
#         }
#     }
#
#     e2e_result = {
#         1: InputSizeResult(TEST_RESULT_1,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
#         2: InputSizeResult(TEST_RESULT_2,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3]),
#         3: InputSizeResult(TEST_RESULT_3,[TEST_RESULT_1,TEST_RESULT_2,TEST_RESULT_3])
#     }
#     profile_result = {
#         "class": [CLASS_OBJECT_1],
#         "function": [FUN_OBJECT_1, FUN_OBJECT_2],
#         "line_by_line": [LINE_OBJECT_1, LINE_OBJECT_2, LINE_OBJECT_3]
#     }
#
#     # @pytest.fixture(autouse=True)
#     # def before_each(self):
#     #     self.e2e_analyzer = EndToEndAnalyzer()
#
#     def test_build(self):
#         speed = Speedometer()
#         assert self.output is speed.build_visualization("test.py", self.profile_result, self.e2e_result)

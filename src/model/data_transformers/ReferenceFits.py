from typing import Dict, List

import math
import numpy

from numpy import poly1d
from numpy.polynomial import polynomial as poly

from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult


class FitData:

    def __init__(
            self,
            O_1: Dict[int, int],
            O_n: Dict[int, int],
            O_logn: Dict[int, int],
            O_n2: Dict[int, int],
            O_n3: Dict[int, int],
            O_nlogn: Dict[int, int],
            O_nn: Dict[int, int],
            O_n_fact: Dict[int, int],
    ):
        self.O_1: Dict[int, int] = O_1
        self.O_n: Dict[int, int] = O_n
        self.O_logn: Dict[int, int] = O_logn
        self.O_n2: Dict[int, int] = O_n2
        self.O_n3: Dict[int, int] = O_n3
        self.O_nlogn: Dict[int, int] = O_nlogn
        self.O_nn: Dict[int, int] = O_nn
        self.O_n_fact: Dict[int, int] = O_n_fact


def get_reference_fits(e2e_results: Dict[int, InputSizeResult], runtime_calc: bool) -> FitData:
    """
    Sets the key-value pairs for each fit line, n -> O(n)
    :param e2e_results: results from the end to end analysis
    :param runtime_calc: true if looking for runtime, false if looking for memory
    """
    x_values = list(e2e_results.keys())
    y_values = []
    for n, result in e2e_results.items():
        y_values.append(result.average.total_runtime_ms if runtime_calc else result.average.max_memory_usage_bytes)

    return FitData(
        O_1=get_o_1_data(x_values, y_values),
        O_n=get_o_n_data(x_values, y_values),
        O_logn=get_o_logn_data(x_values, y_values),
        O_n2=get_o_n2_data(x_values, y_values),
        O_n3=get_o_n3_data(x_values, y_values),
        O_nlogn=get_o_nlogn_data(x_values, y_values),
        O_nn=get_o_nn_data(x_values, y_values),
        O_n_fact=get_o_n_fact_data(x_values, y_values),
    )


def get_o_1_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    min_y = min(y_values)
    min_x = min(x_values)
    max_x = max(x_values)
    return {x: min_y for x in range(min_x, max_x + 1)}


def get_o_logn_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    log_x_values = numpy.log(x_values)
    if max(log_x_values) > 10**12:
        return {x: -1 for x in range(min(x_values), max(x_values) + 1)}
    f = get_polyfit_function(log_x_values, y_values, 1)
    min_x = min(x_values)
    max_x = max(x_values)
    return {x: f(numpy.log(x)) for x in range(min_x, max_x + 1)}


def get_o_n_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    return get_polyfit(x_values, y_values, 1)


def get_o_n2_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    return get_polyfit(x_values, y_values, 2)


def get_o_n3_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    return get_polyfit(x_values, y_values, 3)


def get_o_nlogn_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    def x_log_x(x: float) -> float:
        try:
            return x * numpy.log(x)
        except OverflowError:
            return 10**12

    x_log_x_values = [x_log_x(x) for x in x_values]
    if max(x_log_x_values) > 10**12:
        return {x: -1 for x in range(min(x_values), max(x_values) + 1)}
    f = get_polyfit_function(x_log_x_values, y_values, 1)
    min_x = min(x_values)
    max_x = max(x_values)
    return {x: f(x_log_x(x)) for x in range(min_x, max_x + 1)}


def get_o_nn_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    def x_to_the_x(x: float) -> float:
        try:
            return math.pow(x, x)
        except OverflowError:
            return 10**12

    x_to_the_x_values = [x_to_the_x(x) for x in x_values]
    if max(x_to_the_x_values) > 10**12:
        return {x: -1 for x in range(min(x_values), max(x_values) + 1)}
    f = get_polyfit_function(x_to_the_x_values, y_values, 1)
    min_x = min(x_values)
    max_x = max(x_values)
    return {x: f(x_to_the_x(x)) for x in range(min_x, max_x + 1)}


def get_o_n_fact_data(x_values: List[int], y_values: List[float]) -> Dict[int, int]:
    def x_fact(x: float) -> float:
        try:
            return math.factorial(x)
        except OverflowError:
            return 10**12

    x_fact_values = [x_fact(x) for x in x_values]
    if max(x_fact_values) > 10**12:
        return {x: -1 for x in range(min(x_values), max(x_values) + 1)}
    f = get_polyfit_function(x_fact_values, y_values, 1)
    min_x = min(x_values)
    max_x = max(x_values)
    return {x: f(x_fact(x)) for x in range(min_x, max_x + 1)}


def get_polyfit(x_values: List[int], y_values: List[float], deg: int) -> Dict[int, int]:
    f = get_polyfit_function(x_values, y_values, deg=deg)
    min_x = min(x_values)
    max_x = max(x_values)
    return {x: f(x) for x in range(min_x, max_x + 1)}


def get_polyfit_function(x_values: List[float], y_values: List[float], deg: int) -> poly1d:
    coefficients = poly.polyfit(x_values, y_values, deg=[deg, 0])
    return numpy.poly1d(coefficients)

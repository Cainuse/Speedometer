from typing import List

from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult


class InputSizeResult:
    """
    Results for multiple runs, for a given input size
    """
    average: TestResult
    individual: List[TestResult]

    def __init__(self, average: TestResult, individual: List[TestResult]):
        self.average = average
        self.individual = individual

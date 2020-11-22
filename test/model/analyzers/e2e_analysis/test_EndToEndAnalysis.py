import pytest

from src.model.analyzers.e2e_analysis.EndToEndAnalyzer import EndToEndAnalyzer
from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult


class TestComputeAverage:
    e2e_analyzer: EndToEndAnalyzer

    TEST_RESULT_1 = TestResult(
        1234,
        54321.0,
        {0: 10, 1: 20, 2: 30, 3: 40}
    )

    TEST_RESULT_2 = TestResult(
        5678,
        7896.4,
        {0: 20, 1: 30, 2: 40, 3: 50.5, 4: 100.1}
    )

    TEST_RESULT_3 = TestResult(
        4567,
        11.0,
        {0: 3, 1: 7, 2: 11}
    )

    @pytest.fixture(autouse=True)
    def before_each(self):
        self.e2e_analyzer = EndToEndAnalyzer()

    def test_empty_runs(self):
        individual_runs = []
        result: InputSizeResult = self.e2e_analyzer._compute_average(individual_runs)
        assert len(result.individual) is 0
        assert len(result.average.memory_usage_by_time) is 0

    def test_one_run(self):
        individual_runs = [self.TEST_RESULT_1]
        result: InputSizeResult = self.e2e_analyzer._compute_average(individual_runs)
        assert result.individual is individual_runs
        assert result.average.total_runtime_ms == 1234
        assert result.average.max_memory_usage_bytes == 54321.0
        assert result.average.memory_usage_by_time == {0: 10, 1: 20, 2: 30, 3: 40}

    def test_two_runs(self):
        individual_runs = [self.TEST_RESULT_1, self.TEST_RESULT_2]
        result: InputSizeResult = self.e2e_analyzer._compute_average(individual_runs)
        assert result.individual is individual_runs
        assert result.average.total_runtime_ms == 3456
        assert result.average.max_memory_usage_bytes == 31108.7
        assert result.average.memory_usage_by_time == {0: 15, 1: 25, 2: 35, 3: 45.25, 4: 100.1}

    def test_three_runs(self):
        individual_runs = [self.TEST_RESULT_1, self.TEST_RESULT_2, self.TEST_RESULT_3]
        result: InputSizeResult = self.e2e_analyzer._compute_average(individual_runs)
        assert result.individual is individual_runs
        assert result.average.total_runtime_ms == 3826.333333333333
        assert result.average.max_memory_usage_bytes == 20742.8
        assert result.average.memory_usage_by_time == {0: 11, 1: 19, 2: 27, 3: 45.25, 4: 100.1}

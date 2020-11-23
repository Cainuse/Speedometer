from typing import Dict


class TestResult:
    """
    Results for an individual run, for a given input size
    """
    total_runtime_ms: int
    max_memory_usage_bytes: float
    memory_usage_by_time: Dict[int, float]

    def __init__(self, total_runtime_ms=0, max_memory_usage_bytes=0, memory_usage_by_time=None):
        self.total_runtime_ms = total_runtime_ms
        self.max_memory_usage_bytes = max_memory_usage_bytes
        self.memory_usage_by_time = dict() if memory_usage_by_time is None else memory_usage_by_time

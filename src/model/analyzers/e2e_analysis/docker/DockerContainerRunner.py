from datetime import datetime
from multiprocessing.pool import Pool
from typing import Dict

import docker
import time as Time

from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult

DOCKER_CLIENT = docker.from_env()
# How often to poll in milli seconds
UPDATE_FREQ = 20


def run_and_inspect_docker_image(docker_image_name: str) -> TestResult:
    """
    Builds a docker container for indicated image and runs the container, extracting total time elapsed
    and collects memory usage by time and captures the maximum memory usage during container's lifetime
    :param docker_image_name: Name of the docker image to be ran
    :return: TestResult containing total running time, maximum memory usage and memory usage by time
    """

    docker_image = DOCKER_CLIENT.images.get(docker_image_name)
    docker_container = DOCKER_CLIENT.containers.create(docker_image)

    watcher_results = _create_watchers(docker_container)
    docker_container.start()
    mem_use_by_time = _parse_watcher_results(watcher_results)
    max_mem_usage = max(mem_use_by_time.values())

    stats: dict = DOCKER_CLIENT.api.inspect_container(docker_container.id)
    state = stats["State"]
    started_time = state["StartedAt"]
    end_time = state["FinishedAt"]

    started_time_date_time = datetime.strptime(started_time[:-2], "%Y-%m-%dT%H:%M:%S.%f")
    end_time_date_time = datetime.strptime(end_time[:-2], "%Y-%m-%dT%H:%M:%S.%f")

    result = TestResult((end_time_date_time - started_time_date_time).total_seconds(), max_mem_usage, mem_use_by_time)
    docker_container.remove()
    return result


def _parse_watcher_results(watcher_results) -> Dict[int, float]:
    retrieved = [results.get() for results in watcher_results]
    extended_dict = {time: memory for retrieved_result in retrieved for time, memory in retrieved_result.items()}
    sorted_keys = list(extended_dict.keys())
    sorted_keys.sort()
    sorted_dict = {time: extended_dict[time] for time in sorted_keys}
    return sorted_dict


def _create_watchers(docker_container, count=1):
    # We can potentially increase 'count' here to reduce the interval size for sampling
    # however I haven't been able to find a sweet spot
    pool = Pool(count)
    watchers = []
    for i in range(0, count):
        watchers.append(pool.apply_async(watch_container, [docker_container.id]))
        Time.sleep(1)

    return watchers


def watch_container(container_id) -> Dict[int, float]:
    docker_container = DOCKER_CLIENT.containers.get(container_id)
    mem_use_by_time: Dict[float, float] = dict()

    while docker_container.status != "exited":
        docker_stats = DOCKER_CLIENT.api.stats(container_id, stream=False)
        if docker_stats["memory_stats"] != {}:
            # print(docker_stats)
            mem_use_by_time[Time.time()] = docker_stats["memory_stats"]["usage"] * 1.0
        docker_container.reload()

    mem_usage_by_time_calibrated: Dict[int, float] = dict()
    min_time = min(mem_use_by_time.keys())
    for time, memory in mem_use_by_time.items():
        mem_usage_by_time_calibrated[int((time-min_time)*1000)] = memory

    return mem_usage_by_time_calibrated

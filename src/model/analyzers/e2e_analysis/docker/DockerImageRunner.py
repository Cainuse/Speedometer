from datetime import datetime
from typing import Dict

import docker
import time

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

    max_mem_usage = 0
    mem_use_by_time: Dict[int, float] = dict()

    docker_image = DOCKER_CLIENT.images.get(docker_image_name)
    docker_container = DOCKER_CLIENT.containers.create(docker_image)
    docker_container.start()

    counter = 0
    while docker_container.status != "exited":
        docker_stats = docker_container.stats(stream=False)
        if docker_stats["memory_stats"] != {}:
            print(docker_stats)
            mem_use_by_time[counter] = docker_stats["memory_stats"]["usage"] * 1.0
            max_mem_usage = docker_stats["memory_stats"]["max_usage"] * 1.0

        time.sleep(UPDATE_FREQ / 1000)
        docker_container.reload()
        counter += 1

    stats: dict = DOCKER_CLIENT.api.inspect_container(docker_container.id)
    state = stats["State"]
    started_time = state["StartedAt"]
    end_time = state["FinishedAt"]

    started_time_date_time = datetime.strptime(started_time[:-2], "%Y-%m-%dT%H:%M:%S.%f")
    end_time_date_time = datetime.strptime(end_time[:-2], "%Y-%m-%dT%H:%M:%S.%f")

    result = TestResult((end_time_date_time - started_time_date_time).total_seconds(), max_mem_usage, mem_use_by_time)
    docker_container.remove()
    return result

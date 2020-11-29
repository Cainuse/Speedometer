import os

from src.model.analyzers.e2e_analysis.docker import DockerImageBuilder, DockerContainerRunner

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def test_a_long_running_script():
    dockerfile_path = os.path.join(CURRENT_DIR_PATH, "resources", "dockerfile_with_long_running_script", "Dockerfile")
    name = DockerImageBuilder.build_docker_image(dockerfile_path)
    result = DockerContainerRunner.run_and_inspect_docker_image(name)

    print("Total Runtime = {}, Max Mem Usage = {}, Usage by time = {}"
          .format(result.total_runtime_ms, result.max_memory_usage_bytes, result.memory_usage_by_time))

    assert result.total_runtime_ms > 3000, "the script takes at least 3000 ms to run"

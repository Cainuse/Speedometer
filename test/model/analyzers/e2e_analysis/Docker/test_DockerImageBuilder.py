import src.model.analyzers.e2e_analysis.docker.DockerImageBuilder as DockerImageBuilder
import os

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

"""
Test build_docker_image()
"""


def test():
    dockerfile_path = os.path.join(CURRENT_DIR_PATH, "resources", "Dockerfile")
    name = DockerImageBuilder.build_docker_image(dockerfile_path)
    assert name in DockerImageBuilder.list_images()
    DockerImageBuilder.delete_all_docker_images(force=True)

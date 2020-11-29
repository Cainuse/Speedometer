import os

import pytest

import src.model.analyzers.e2e_analysis.docker.DockerImageBuilder as DockerImageBuilder

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

"""
Test build_docker_image()
"""


@pytest.fixture(autouse=True)
def after_each():
    """
    Runs after each test
    """
    yield  # let the test run first
    DockerImageBuilder.delete_all_docker_images(force=True, exceptions=["python"])


def test_valid_dockerfile():
    dockerfile_path = os.path.join(CURRENT_DIR_PATH, "resources", "minimal_dockerfile", "Dockerfile")
    name = DockerImageBuilder.build_docker_image(dockerfile_path)
    assert name in DockerImageBuilder.list_images()


def test_invalid_dockerfile_path():
    with pytest.raises(Exception):
        dockerfile_path = "an/invalid/path"
        DockerImageBuilder.build_docker_image(dockerfile_path)

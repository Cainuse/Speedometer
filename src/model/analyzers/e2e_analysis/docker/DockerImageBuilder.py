import os
from subprocess import Popen
import re
from typing import List

import docker

from src.model.analyzers.e2e_analysis.docker import DockerUtil
from src.model.util.Logger import debug

DOCKER_CLIENT = docker.from_env()


def build_docker_image(dockerfile_path: str) -> str:
    """
    Builds an image using the given dockerfile using a unique image name
    :param dockerfile_path: path to the dockerfile to use for building the image
    :return: the name of the image created. Randomly generated.
    """
    debug("Starting docker image build for {}".format(dockerfile_path))
    if os.path.isfile(dockerfile_path):
        build_path, _ = os.path.split(dockerfile_path)  # if given path is to Dockerfile, get the parent
    else:
        build_path = dockerfile_path  # else use the directory given

    if not os.path.exists(build_path):
        raise Exception("Build path {} does not exist".format(build_path))

    _pull_base_image_if_absent("python:latest")
    try:
        repository: str = DockerUtil.get_random_string_of_length(20, uppercase=False, numbers=False)
        DOCKER_CLIENT.images.build(path=build_path, tag=repository)
        debug("Image build complete!")
        return repository
    except Exception as e:
        raise Exception("Failed to build image for {}".format(dockerfile_path), e)


def list_images(remove_version=True) -> List[str]:
    """
    Returns a list of repository names for the currently built images
    :return: a list of string
    """
    # create a list of image names in the format repository:version
    with_version_name: List[str] = [tag for image in DOCKER_CLIENT.images.list() for tag in image.tags]
    # return list with version removed
    return [re.sub(':.*', "", tag) for tag in with_version_name] if remove_version else with_version_name


def delete_all_docker_images(force=False, exceptions=None):
    """
    Deletes all built docker images
    """
    exceptions = [] if exceptions is None else exceptions
    image_names = list_images()
    for name in image_names:
        if name not in exceptions:
            DOCKER_CLIENT.images.remove(name, force=force)


def load_docker_image(path: str):
    with open(path, "rb") as file:
        DOCKER_CLIENT.images.load(file)


def _pull_base_image_if_absent(base_image_name: str):
    local_images = list_images(remove_version=False)
    if base_image_name not in local_images:
        debug("Base Docker image '{}' not found".format(base_image_name))
        debug("Downloading and extracting base image.")
        debug("If you're running Speedometer for the first time, this may take a few minutes")
        pull_process = Popen(['docker', 'pull', base_image_name])
        pull_process.wait()


if __name__ == "__main__":
    load_docker_image("D:\\University of British Columbia\\Academics\\Year 4\\Term 1\\CPSC 410\\Projects\\Project 2\\cpsc410_project2_team4\\resources\\scalene.tar")

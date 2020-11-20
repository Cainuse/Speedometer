import docker
import os
import re
from typing import List

from src.model.analyzers.e2e_analysis.docker import DockerUtil

DOCKER_CLIENT = docker.from_env()


def build_docker_image(dockerfile_path: str) -> str:
    """
    Builds an image using the given dockerfile using a unique image name
    :param dockerfile_path: path to the dockerfile to use for building the image
    :return: the name of the image created. Randomly generated.
    """
    if os.path.isfile(dockerfile_path):
        build_path, _ = os.path.split(dockerfile_path)                  # if given path is to Dockerfile, get the parent
    else:
        build_path = dockerfile_path                                                      # else use the directory given

    if not os.path.exists(build_path):
        raise Exception("Build path {} does not exist".format(build_path))

    try:
        repository: str = DockerUtil.get_random_string_of_length(20, uppercase=False, numbers=False)
        DOCKER_CLIENT.images.build(path=build_path, tag=repository)
        return repository
    except Exception as e:
        raise Exception("Failed to build image for {}".format(dockerfile_path), e)


def list_images() -> List[str]:
    """
    Returns a list of repository names for the currently built images
    :return: a list of string
    """
    # create a list of image names in the format repository:version
    with_version_name: List[str] = [tag for image in DOCKER_CLIENT.images.list() for tag in image.tags]
    # return list with version removed
    return [re.sub(':.*', "", tag) for tag in with_version_name]


def delete_all_docker_images(force=False):
    """
    Deletes all built docker images
    """
    image_names = list_images()
    for name in image_names:
        DOCKER_CLIENT.images.remove(name, force=force)

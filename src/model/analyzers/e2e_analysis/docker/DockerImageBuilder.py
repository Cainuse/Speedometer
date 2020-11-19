import docker
import os

from src.model.analyzers.e2e_analysis.docker import Docker_Util


def build_docker_image(dockerfile_path: str) -> str:
    """
    Builds an image using the given dockerfile using a unique image name
    :param dockerfile_path: path to the dockerfile to use for building the image
    :return: the name of the image created. Randomly generated.
    """
    print("entered")
    if os.path.isfile(dockerfile_path):
        build_path, _ = os.path.split(dockerfile_path)                  # if given path is to Dockerfile, get the parent
    else:
        build_path = dockerfile_path                                                      # else use the directory given

    if not os.path.exists(build_path):
        raise Exception("Build path {} does not exist".format(build_path))

    image_tag: str = Docker_Util.get_random_string_of_length(20, uppercase=False, numbers=False)
    print("Creating: " + image_tag)
    docker_client = docker.from_env()
    image, _ = docker_client.images.build(path=build_path, tag=image_tag)
    print(image)
    return ""

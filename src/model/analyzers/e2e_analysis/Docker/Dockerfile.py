from os import path
import os
import random
import string
from typing import Union


def build_dockerfile(program_file_path: str, program_args: list) -> str:
    """
    Creates a Dockerfile to test the given program with the given command
    :param program_file_path: path to python program that will be run
    :param program_args: arguments to pass the python program
    :return: the path for the generated Dockerfile
    """
    dockerfile_contents = _load_template_dockerfile()

    program_file_name = path.basename(program_file_path)  # includes ".py"
    dockerfile_contents = _dockerfile_append_add(dockerfile_contents, program_file_path, program_file_name)

    command = ["python", program_file_name]
    command.extend(program_args)
    dockerfile_contents = _dockerfile_append_cmd(dockerfile_contents, command)

    output_path = path.abspath(path.join(".", "generated_dockerfiles", _get_random_folder_name()))
    _write_dockerfile(dockerfile_contents, output_path)
    return output_path


def _dockerfile_append_cmd(dockerfile: str, command: list) -> str:
    """
    Appends an CMD command to the end of the dockerfile contents
    :param dockerfile: dockerfile contents as string
    :param command: the command to run as a list of arguments
    :return: new dockerfile contents
    """
    return dockerfile + "\nCMD {command}".format(command=_stringify_command_list(command))


def _stringify_command_list(command: list) -> str:
    """
    Returns the given command args as comma separated string. Arguments are surrounded by escaped quotes and
    box brackets are placed around the string
    """
    command = ["\"{}\"".format(arg) for arg in command]
    return "[{}]".format(", ".join(command))


def _dockerfile_append_add(dockerfile: str, target: str, destination: str) -> str:
    """
    Appends an ADD command to the end of the dockerfile contents
    :param dockerfile: dockerfile contents as string
    :param target: target file to add
    :param destination: destination to copy file to (within container)
    :return: new dockerfile contents
    """
    return dockerfile + "\nADD {target} {destination}".format(target=target, destination=destination)


def _load_template_dockerfile() -> str:
    """
    :return: template dockerfile as string
    """
    with open("Dockerfile_Template", "r+") as file:
        return file.read()


def _write_dockerfile(contents: str, output_path: str) -> Union[None, Exception]:
    """
    Writes the given contents to a Dockerfile at the given path
    :param contents: string contents of Dockerfile
    :param output_path: path to a directory where Dockerfile should be saved
    """
    os.makedirs(output_path, exist_ok=True)
    if not path.isdir(output_path):
        return Exception()

    output_file = path.join(output_path, "Dockerfile")
    with open(output_file, "rw+") as file:
        file.write(contents)


def _get_random_folder_name():
    length = 20
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

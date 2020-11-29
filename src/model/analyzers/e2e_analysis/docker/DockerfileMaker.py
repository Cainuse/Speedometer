import os
import shutil
from os import path

from src.model.analyzers.e2e_analysis.docker import DockerUtil

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
GENERATED_DOCKERFILES_PATH = path.abspath(path.join(CURRENT_DIR_PATH, "generated_dockerfiles"))
PYTHON_TEMPLATE_PATH = path.abspath(path.join(CURRENT_DIR_PATH, "PythonDockerfileTemplate"))
SCALENE_TEMPLATE_PATH = path.abspath(path.join(CURRENT_DIR_PATH, "ScaleneDockerfileTemplate"))


def build_python_dockerfile(program_file_path: str, program_args: list) -> str:
    """
    Creates a Dockerfile to test the given program with the given command
    :param program_file_path: **absolute** path to python program that will be run
    :param program_args: arguments to pass the python program
    :return: the path for the generated Dockerfile
    """

    program_file_name = path.basename(program_file_path)
    command = ["python", program_file_name]
    command.extend(program_args)
    return build_dockerfile(PYTHON_TEMPLATE_PATH, program_file_path, command)


def build_scalene_dockerfile(program_file_path: str, program_args: list) -> str:
    program_file_name = path.basename(program_file_path)
    command = ["scalene", program_file_name]
    command.extend(program_args)
    return build_dockerfile(SCALENE_TEMPLATE_PATH, program_file_path, command)


def build_dockerfile(template_path: str, program_file_path: str, command: list) -> str:
    dockerfile_contents = _load_template_dockerfile(template_path)

    program_file_name = path.basename(program_file_path)
    dockerfile_contents = _dockerfile_append_copy(dockerfile_contents, program_file_name, ".")

    dockerfile_contents = _dockerfile_append_cmd(dockerfile_contents, command)

    random_folder_name = _get_random_folder_name()
    output_directory_path = path.abspath(path.join(GENERATED_DOCKERFILES_PATH, random_folder_name))

    output_path = path.abspath(path.join(output_directory_path, "Dockerfile"))
    _write_dockerfile(dockerfile_contents, output_path)

    _copy_file(program_file_path, output_directory_path)
    return output_path


def clear_generated_dockerfiles() -> bool:
    """
    Deletes all generated dockerfiles
    :returns: true if successfully deleted dockerfiles, false for any errors
    """
    try:
        shutil.rmtree(GENERATED_DOCKERFILES_PATH)
        return True
    except Exception as e:
        print("Failed to delete file: " + str(e))
        return False


def _copy_file(src_file_path: str, dest_dir_path: str):
    """
    Copies the given file to the given directory
    :param src_file_path: path to file to copy
    :param dest_dir_path: destination directory to copy file to
    """
    try:
        shutil.copy(src_file_path, dest_dir_path)
    except Exception as e:
        raise Exception("Failed to copy {} to {}".format(src_file_path, dest_dir_path), e)


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


def _dockerfile_append_copy(dockerfile: str, target: str, destination: str) -> str:
    """
    Appends an ADD command to the end of the dockerfile contents
    :param dockerfile: dockerfile contents as string
    :param target: target file to add
    :param destination: destination to copy file to (within container)
    :return: new dockerfile contents
    """
    return dockerfile + "\nCOPY {target} {destination}".format(target=target, destination=destination)


def _load_template_dockerfile(path: str) -> str:
    """
    :return: template dockerfile as string
    """
    with open(path, "r+") as file:
        return file.read()


def _write_dockerfile(contents: str, output_path: str) -> None:
    """
    Writes the given contents to a Dockerfile at the given path
    :param contents: string contents of Dockerfile
    :param output_path: path to a Dockerfile where contents should be saved
    """
    parent, file_name = path.split(output_path)
    os.makedirs(parent, exist_ok=True)

    try:
        with open(output_path, "w+") as file:
            file.write(contents)
    except Exception as e:
        print(e)
        raise e


def _get_random_folder_name():
    return DockerUtil.get_random_string_of_length(20)

from os import path
import os
import shutil

from src.model.analyzers.e2e_analysis.docker import DockerUtil

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
GENERATED_DOCKERFILES_PATH = path.abspath(path.join(CURRENT_DIR_PATH, "generated_dockerfiles"))
TEMPLATE_PATH = path.abspath(path.join(CURRENT_DIR_PATH, "DockerfileTemplate"))


def build_dockerfile(program_file_path: str, program_args: list) -> str:
    """
    Creates a Dockerfile to test the given program with the given command
    :param program_file_path: **absolute** path to python program that will be run
    :param program_args: arguments to pass the python program
    :return: the path for the generated Dockerfile
    """
    dockerfile_contents = _load_template_dockerfile()
    dockerfile_contents = _dockerfile_append_copy(dockerfile_contents, program_file_path, ".")

    program_file_name = path.basename(program_file_path)  # includes ".py"
    command = ["python", program_file_name]
    command.extend(program_args)
    dockerfile_contents = _dockerfile_append_cmd(dockerfile_contents, command)

    output_path = path.abspath(path.join(GENERATED_DOCKERFILES_PATH, _get_random_folder_name(), "Dockerfile"))
    _write_dockerfile(dockerfile_contents, output_path)
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


def _load_template_dockerfile() -> str:
    """
    :return: template dockerfile as string
    """
    with open(TEMPLATE_PATH, "r+") as file:
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


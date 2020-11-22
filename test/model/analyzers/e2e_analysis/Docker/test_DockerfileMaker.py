import src.model.analyzers.e2e_analysis.docker.DockerfileMaker as DockerfileMaker

"""
Test _stringify_command_list()
"""


def test_stringify_command_list_empty_list():
    command = []
    expected = "[]"
    assert DockerfileMaker._stringify_command_list(command) == expected


def test_stringify_command_list_one_arg():
    command = ["python"]
    expected = "[\"python\"]"
    assert DockerfileMaker._stringify_command_list(command) == expected


def test_stringify_command_list_two_arg():
    command = ["python", "test.py"]
    expected = "[\"python\", \"test.py\"]"
    assert DockerfileMaker._stringify_command_list(command) == expected


"""
Test build_dockerfile()
"""


def helper_test_dockerfile(program_file_path, args, expected_contents):
    output_path = DockerfileMaker.build_dockerfile(program_file_path, args)
    try:
        with open(output_path, "r") as dockerfile:
            contents = dockerfile.read()
            assert contents == expected_contents
    finally:
        DockerfileMaker.clear_generated_dockerfiles()


def test_build_dockerfile_empty_args():
    program_file_path = "./test.py"
    args = []
    expected_contents = "FROM python\nCOPY ./test.py .\nCMD [\"python\", \"test.py\"]"
    helper_test_dockerfile(program_file_path, args, expected_contents)


def test_build_dockerfile_one_args():
    program_file_path = "./test.py"
    args = ["-d"]
    expected_contents = "FROM python\nCOPY ./test.py .\nCMD [\"python\", \"test.py\", \"-d\"]"
    helper_test_dockerfile(program_file_path, args, expected_contents)


def test_build_dockerfile_multiple_args():
    program_file_path = "./test.py"
    args = ["-d", "1000"]
    expected_contents = "FROM python\nCOPY ./test.py .\nCMD [\"python\", \"test.py\", \"-d\", \"1000\"]"
    helper_test_dockerfile(program_file_path, args, expected_contents)


def test_build_dockerfile_relative_program_path():
    program_file_path = "./some/relative/path/test.py"
    args = ["-d", "1000"]
    expected_contents = \
        "FROM python\nCOPY ./some/relative/path/test.py .\nCMD [\"python\", \"test.py\", \"-d\", \"1000\"]"
    helper_test_dockerfile(program_file_path, args, expected_contents)


def test_build_dockerfile_absolute_program_path_unix():
    program_file_path = "/c/some/absolute/path/test.py"
    args = ["-d", "1000"]
    expected_contents = \
        "FROM python\nCOPY /c/some/absolute/path/test.py .\nCMD [\"python\", \"test.py\", \"-d\", \"1000\"]"
    helper_test_dockerfile(program_file_path, args, expected_contents)

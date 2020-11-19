import pytest
from src.model.analyzers.e2e_analysis.Docker.Dockerfile import _stringify_command_list

"""
Test _stringify_command_list()
"""


def test_stringify_command_list_empty_list():
    command = []
    expected = "[]"
    assert _stringify_command_list(command) == expected


def test_stringify_command_list_one_arg():
    command = ["python"]
    expected = "[\"python\"]"
    assert _stringify_command_list(command) == expected


def test_stringify_command_list_two_arg():
    command = ["python", "test.py"]
    expected = "[\"python\", \"test.py\"]"
    assert _stringify_command_list(command) == expected


"""
Test _write_dockerfile()
"""


@pytest.mark.skip("Not Implemented")
def test_write_dockerfile():
    return Exception()


@pytest.mark.skip("Not Implemented")
def test_load_template_dockerfile():
    return Exception()


@pytest.mark.skip("Not Implemented")
def test_dockerfile_append_add():
    return Exception()


@pytest.mark.skip("Not Implemented")
def test_dockerfile_append_cmd():
    return Exception()


@pytest.mark.skip("Not Implemented")
def test_build_dockerfile():
    return Exception()

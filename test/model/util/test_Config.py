import os
from os import path

import pytest

from src.model.util.Config import Config

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_SAMPLE_CONFIGS = path.abspath(path.join(CURRENT_DIR_PATH, "..", "resources", "sample_configs"))


def test_sample_config_complete():
    config_path = path.join(PATH_TO_SAMPLE_CONFIGS, "sample_config_complete.json")
    config = Config(config_path)
    assert config.get_input_sizes() == [1, 2, 10, 20, 30, 100, 2000]
    assert config.get_args_for(1) == ["-n", "51", "-f", "/some/file"]
    assert config.get_args_for(2) == ["-n", "52", "-f", "/some/file"]
    assert config.get_args_for(10) == ["-n", "60", "-f", "/some/file"]
    assert config.get_args_for(20) == ["-n", "70", "-f", "/some/file"]
    assert config.get_args_for(30) == ["-n", "80", "-f", "/some/file"]
    assert config.get_args_for(100) == ["-n", "150", "-f", "/some/file"]
    assert config.get_args_for(2000) == ["-n", "2050", "-f", "/some/file"]


def test_sample_config_missing_arg_property():
    with pytest.raises(Exception):
        config_path = path.join(PATH_TO_SAMPLE_CONFIGS, "sample_config_missing_arg_property.json")
        Config(config_path)


def test_sample_config_non_list_args():
    with pytest.raises(Exception):
        config_path = path.join(PATH_TO_SAMPLE_CONFIGS, "sample_config_non_list_args.json")
        Config(config_path)


def test_sample_config_non_numeric_sizes():
    with pytest.raises(Exception):
        config_path = path.join(PATH_TO_SAMPLE_CONFIGS, "sample_config_non_numeric_sizes.json")
        Config(config_path)


def test_config_file_does_not_exist():
    with pytest.raises(Exception):
        config_path = "/non/existent/path"
        Config(config_path)


def test_config_non_file_path():
    with pytest.raises(Exception):
        config_path = PATH_TO_SAMPLE_CONFIGS
        Config(config_path)

import os
import sys
from os.path import abspath, join
import argparse

# add root directory to packages
ROOT_PATH = abspath(join(abspath(__file__), "..", ".."))
sys.path.insert(0, ROOT_PATH)

from src.model.util import Logger
from src.model.util.Config import Config
from src.model.Speedometer import Speedometer
from src.model.util.BuildUtil import package_visualization_and_open


def _parse_and_verify_path(path: str) -> str:

    if path is None:
        raise Exception("No path given")

    if type(path).__name__ != 'str':
        raise Exception("Path is not a string - {}".format(path))

    if not os.path.isabs(path):
        path = os.path.abspath(os.path.join(ROOT_PATH, path))   # if rel path, get path relative to root

    if not (os.path.exists(path) and os.path.isfile(path)):
        raise Exception("Invalid path {}".format(path))

    return path


def _parse_program_file_path(args: argparse.Namespace) -> str:
    """
    Parses the value of the file path of the program to analyze passed as an argument.
    If the path is relative, computes and returns the absolute path.
    :return: absolute version of the path path given by user to program to analyze.
    :raises: Exception if the path is invalid (file does not exist/is not python program)
    """
    try:
        program_path = args.program
        program_path = _parse_and_verify_path(program_path)
        _, extension = os.path.splitext(program_path)
        if extension != ".py":
            raise Exception("Program file is not a Python file")
        return program_path
    except Exception as e:
        raise Exception("Failed to load program file.", e)


def _parse_config_file(args: argparse.Namespace) -> Config:
    """
    Parses the value of the file path of the config file provided by the user, builds Config object and returns it.
    If the path is relative, computes and returns the absolute path.
    :return: Config object instantiated with user-provided config file
    :raises: Exception if the path is invalid (file does not exist/is not JSON/does not follow format)
    """
    try:
        config_path = args.config
        config_path = _parse_and_verify_path(config_path)
        _, extension = os.path.splitext(config_path)
        if extension != ".json":
            raise Exception("Config file is not a JSON file")
        return Config(config_path)
    except Exception as e:
        raise Exception("Failed to load config file.", e)


def _parse_debug_flag(args: argparse.Namespace) -> bool:
    return args.v


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Speedometer - program complexity analysis")
    parser.add_argument('--program', type=str, help='path to the Python program to analyze')
    parser.add_argument('--config', type=str, help='path to the config file')
    parser.add_argument('-v', action='store_true', help='set this flag for verbose output')
    return parser.parse_args()


def main():
    """
    Processes user-provided arguments to initiate Speedometer analysis
    """
    try:
        args = _parse_args()
        if _parse_debug_flag(args):
            Logger.set_debug_on()

        Logger.set_stage("INITIALIZING")

        Logger.debug("Loading the python program to analyze", force=True)
        program_file_path: str = _parse_program_file_path(args)
        Logger.debug("Python program {} loaded".format(program_file_path))

        Logger.debug("Loading the associated config file")
        config: Config = _parse_config_file(args)
        Logger.debug("Config file {} loaded".format(config.path))

        Logger.set_stage("ANALYSIS")
        Logger.debug("Starting analysis...", force=True)
        speedometer = Speedometer()
        speedometer.run(program_file_path, config)
        Logger.debug("Analysis is complete!", force=True)

        Logger.set_stage("VISUALIZATION")
        Logger.debug("Building results_visualization of results", force=True)
        package_visualization_and_open()
        Logger.debug("Build complete!", force=True)
    except Exception as e:
        Logger.set_stage("PROGRAM ERROR")
        Logger.debug("Error analyzing program", force=True)
        Logger.debug("Full Stack Trace - " + str(e), force=True)


if __name__ == "__main__":
    main()

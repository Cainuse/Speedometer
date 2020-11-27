import sys
from os.path import abspath, join

# add root directory to packages
ROOT_PATH = abspath(join(abspath(__file__), "..", ".."))
sys.path.insert(0, ROOT_PATH)

from src.model.util import Config
from src.model.Speedometer import Speedometer
from src.model.util.BuildUtil import package_visualization_and_open


def _parse_program_file_path() -> str:
    """
    Parses the value of the file path of the program to analyze passed as an argument.
    If the path is relative, computes and returns the absolute path.
    :return: absolute version of the path path given by user to program to analyze.
    :raises: Exception if the path is invalid (file does not exist/is not python program)
    """

    # TODO: Implement
    if len(sys.argv) > 1:
        return sys.argv(1)
    else:
        print("No file given to analyze.")


def _parse_config_file() -> Config:
    """
    Parses the value of the file path of the config file provided by the user, builds Config object and returns it.
    If the path is relative, computes and returns the absolute path.
    :return: Config object instantiated with user-provided config file
    :raises: Exception if the path is invalid (file does not exist/is not JSON/does not follow format)
    """

    # TODO: Implement
    if len(sys.argv) > 2:
        return sys.argv(2)
    else:
        print("No config file given.")


def main():
    """
    Processes user-provided arguments to initiate Speedometer analysis
    """
    program_file_path: str = _parse_program_file_path()
    config: Config = _parse_config_file()

    speedometer = Speedometer()
    speedometer.run(program_file_path, config)

    package_visualization_and_open()


if __name__ == "__main__":
    main()

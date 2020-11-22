from src.model.Speedometer import Speedometer

import sys

def _parse_program_file_path() -> str:
    """
    Parses the value of the file path of the program to analyze
    passed as an argument
    :return: path given by user to program to analyze.
             return Exception if the path is invalid (file does not exist/is not python program)
    """

    # TODO: Implement
    if len(sys.argv) > 1:
        return sys.argv(1)
    else:
        print("No file given to analyze.")


def _parse_config_file_path() -> str:
    """
    Parses the value of the file path of the config file provided by the user
    :return: path given by user for the config file
             return Exception if the path is invalid (file does not exist/is not JSON/does not follow format)
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
    program_file_path = _parse_config_file_path()
    config_file_path = _parse_config_file_path()

    speedometer = Speedometer()
    speedometer.run(program_file_path, config_file_path)


if __name__ == "__main__":
    main()

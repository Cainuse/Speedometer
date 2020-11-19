from src.model.Speedometer import Speedometer


def _parse_program_file_path() -> str:
    """
    Parses the value of the file path of the program to analyze
    passed as an argument
    :return: path given by user to program to analyze.
             return Exception if the path is invalid (file does not exist/is not python program)
    """

    # TODO: Implement


def _parse_config_file_path() -> str:
    """
    Parses the value of the file path of the config file provided by the user
    :return: path given by user for the config file
             return Exception if the path is invalid (file does not exist/is not JSON/does not follow format)
    """

    # TODO: Implement


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

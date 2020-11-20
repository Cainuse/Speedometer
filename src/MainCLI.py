from src.model import Config
from src.model.Speedometer import Speedometer


def _parse_program_file_path() -> str:
    """
    Parses the value of the file path of the program to analyze passed as an argument.
    If the path is relative, computes and returns the absolute path.
    :return: absolute version of the path path given by user to program to analyze.
    :raises: Exception if the path is invalid (file does not exist/is not python program)
    """

    # TODO: Implement
    raise Exception("Not implemented")


def _parse_config_file() -> Config:
    """
    Parses the value of the file path of the config file provided by the user, builds Config object and returns it.
    If the path is relative, computes and returns the absolute path.
    :return: Config object instantiated with user-provided config file
    :raises: Exception if the path is invalid (file does not exist/is not JSON/does not follow format)
    """

    # TODO: Implement
    raise Exception("Not implemented")


def main():
    """
    Processes user-provided arguments to initiate Speedometer analysis
    """
    program_file_path: str = _parse_config_file()
    config: Config = _parse_config_file()

    speedometer = Speedometer()
    speedometer.run(program_file_path, config)

    # TODO: open the generated webpage in browser


if __name__ == "__main__":
    main()

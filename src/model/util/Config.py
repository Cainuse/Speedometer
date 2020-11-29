import json
import os
from typing import Dict, List


class Config:
    ARGS_PROP = "arguments"

    args: Dict[int, list]
    path: str

    def __init__(self, config_file_path):
        """
        Inits a Config class object
        :param config_file_path: path to the config file
        """
        self.path = config_file_path
        string_data = self._get_file_as_str(config_file_path)
        json_data = json.loads(string_data)
        self.args = self._parse_args(json_data)

    def get_args_for(self, n: int) -> list:
        """
        Reads the arguments for the python program for the given sample size
        :param n: sample size for which to read arguments
        :return: list of string containing arguments
        :raises Exception: if no args defined for 'n'
        """
        if n not in self.args.keys():
            raise Exception("No arguments defined for input size {}".format(n))
        return self.args[n]

    def get_input_sizes(self) -> list:
        """
        Returns the input sizes for which arguments are defined within the config file
        :return: a list of integers representing the input sizes
        """

        return [i for i in self.args.keys()]

    def _get_file_as_str(self, path: str) -> str:
        """
        Returns the data of the given file as a string
        :param path: path to file
        :return: data as string
        :raises Exception: if file does not exist or there is an error reading the file
        """
        try:
            with open(path, "r") as file:
                return file.read()
        except Exception as e:
            raise Exception("Cannot read {}. {}".format(path, str(e)))

    def _parse_args(self, data: dict) -> Dict[int, List[str]]:
        """
        Parses the arguments for each input size from the given config file data
        :param data: json data from config file
        :return: arguments for each input size
        """
        if self.ARGS_PROP not in data:
            raise Exception("Invalid config file. No 'arguments' property given")

        args_data = data[self.ARGS_PROP]
        parsed_args: Dict[int, List[str]] = dict()

        for size_str, args in args_data.items():
            try:
                size_int = int(size_str)
                if not type(args).__name__ == 'list':
                    raise Exception('args are not a list')
                parsed_args[size_int] = args
            except Exception as e:
                raise Exception("Could not parse args for input size {}. {}".format(size_str, str(e)))

        return parsed_args

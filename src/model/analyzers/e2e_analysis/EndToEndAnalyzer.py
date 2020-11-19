import os
import subprocess
import json
from datetime import datetime
from typing import List, Dict

from src.model.analyzers.e2e_analysis.Config import Config
from src.model.analyzers.e2e_analysis.docker.Dockerfile import build_dockerfile


class TestResult:
    """
    Results for an individual run, for a given input size
    """
    total_runtime: float
    # TODO: add more


class InputSizeResult:
    """
    Results for multiple runs, for a given input size
    """
    average: TestResult
    individual: List[TestResult]


class EndToEndAnalyzer:

    RUNS_PER_INPUT_SIZE: int = 3

    results = dict()

    def analyze(self, program_file_path: str, config_file_path: str) -> None:
        """
        Runs e2e analyses on the given program
        :param program_file_path: **absolute** path to the program to analyze
        :param config_file_path: path to the config file
        """
        config: Config = Config(config_file_path)
        input_sizes: List[int] = config.get_input_sizes()

        # creates all required dockerfiles and stores paths in a dict of <input_size, dockerfile path>
        dockerfiles: Dict[int, str] = {s: self._build_dockerfile_for_input(program_file_path, s, config) for s in input_sizes}

        # builds all the dockerfiles into images and stores the image names in a dict of <input_size, image name>
        images: Dict[int, str] = {s: self._build_docker_image(dockerfile) for s, dockerfile in dockerfiles.items()}

        # execute the test runs
        for input_size, image in images.items():
            individual_results: List[TestResult] = self._run_test_container(image, self.RUNS_PER_INPUT_SIZE)
            computed_results: InputSizeResult = self._compute_average(individual_results)
            self.results[input_size] = computed_results

    def get_results(self) -> Dict[int, InputSizeResult]:
        """
        :return: the results from the analysis as a dict.
                 the keys int the dictionary are the input sizes
                 the values are the results for that sample size
        """

        # TODO: implement this

    def _compute_average(self, individual_runs: List[TestResult]) -> InputSizeResult:
        """
        Computes an average result for the individual runs and combines both into an InputSizeResult
        :param individual_runs: results for the individual runs of the container
        :return: a combined result with a computed average
        """

        # TODO: implement this

    def _run_test_container(self, image_name: str, runs: int) -> List[TestResult]:
        """
        Spins-up a container from the given image and runs the program for the given input 'run' number of times
        Returns the results for each run
        :param image_name: name of the docker image configured to run test for an input size
        :return: a list of Result objects - one for each run
        """

        # TODO: implement this
        # TODO: maybe there should be a timeout?

        # # Get information about the docker container
        # output = subprocess.run(["docker", "inspect", "e2e"], stdout=subprocess.PIPE)
        #
        # # Convert bytes to string
        # output = output.stdout.decode('utf-8')
        #
        # # Convert String to json and extract data
        # output_json = json.loads(output)
        #
        # container = output_json[0]
        #
        # container_state = container["State"]
        #
        # container_start_time = container_state["StartedAt"]
        # container_state_time = datetime.strptime(container_start_time[:-2], "%Y-%m-%dT%H:%M:%S.%f").microsecond
        #
        # container_end_time = container_state["FinishedAt"]
        # container_end_time = datetime.strptime(container_end_time[:-2], "%Y-%m-%dT%H:%M:%S.%f").microsecond
        #
        # # Total runtime in microseconds
        # print("Total Runtime is: " + str(container_end_time - container_state_time) + " microseconds")
        # print("Total Runtime is: " + str((container_end_time - container_state_time) / 10 ** 6) + " seconds")
        #
        # # Delete Created Docker image and container after script executes
        # os.system("docker rm e2e && docker rmi e2e")

    def _build_docker_image(self, dockerfile_path) -> str:
        """
        Builds the image for the given dockerfile
        :param dockerfile_path: path to dockerfile
        :return: the name of the generated image
        """

        # TODO: implement this

        # # Build Docker Image
        # os.system("docker build -t e2e .")
        #
        # # Run Docker Image in a container
        # os.system("docker run --name e2e e2e")

    def _build_dockerfile_for_input(self, program_file_path: str, input_size: int, config: Config) -> str:
        """
        Builds a dockerfile to run the program for the given input size and returns the path to the dockerfile
        :param program_file_path: path to python program to test
        :param input_size: input size on which to test program
        :param config: user provided config
        :return: path to generated dockerfile
        """
        return build_dockerfile(program_file_path, config.get_args_for(input_size))

from typing import List, Dict

from src.model.util.Config import Config
from src.model.analyzers.e2e_analysis.docker.DockerImageBuilder import build_docker_image, delete_all_docker_images
from src.model.analyzers.e2e_analysis.docker.DockerContainerRunner import run_and_inspect_docker_image
from src.model.analyzers.e2e_analysis.docker.DockerfileMaker import build_python_dockerfile
from src.model.analyzers.e2e_analysis.result_types.InputSizeResult import InputSizeResult
from src.model.analyzers.e2e_analysis.result_types.TestResult import TestResult
from src.model.util.Logger import debug


class EndToEndAnalyzer:
    RUNS_PER_INPUT_SIZE: int = 3

    results = dict()

    def analyze(self, program_file_path: str, config: Config) -> None:
        """
        Runs e2e analyses on the given program
        :param program_file_path: **absolute** path to the program to analyze
        :param config: config object for user-defined configuration
        """
        input_sizes: List[int] = config.get_input_sizes()

        # creates all required dockerfiles and stores paths in a dict of <input_size, dockerfile path>
        debug("Creating dockerfiles for each input size")
        dockerfiles: Dict[int, str] = \
            {size: self._build_dockerfile_for_input(program_file_path, size, config) for size in input_sizes}

        # builds all the dockerfiles into images and stores the image names in a dict of <input_size, image name>
        debug("Building docker images for each input size")
        images: Dict[int, str] = \
            {size: build_docker_image(dockerfile) for size, dockerfile in dockerfiles.items()}

        # execute the test runs
        for input_size, image in images.items():
            debug("Analyzing for input size {}".format(input_size))
            individual_results: List[TestResult] = self._run_test_container(image, self.RUNS_PER_INPUT_SIZE)
            computed_results: InputSizeResult = self._compute_average(individual_results)
            self.results[input_size] = computed_results

        debug("End-to-end analysis complete!")
        debug("Doing some clean-up!")
        try:
            delete_all_docker_images(exceptions=["python"], force=True)
            debug("All cleaned-up here.")
        except:
            debug("Cleanup failed. Please cleanup Docker manually")

    def get_results(self) -> Dict[int, InputSizeResult]:
        """
        :return: the results from the analysis as a dict.
                 the keys int the dictionary are the input sizes
                 the values are the results for that sample size
        """
        return self.results

    def _compute_average(self, individual_runs: List[TestResult]) -> InputSizeResult:
        """
        Computes an average result for the individual runs and combines both into an InputSizeResult
        :param individual_runs: results for the individual runs of the container
        :return: a combined result with a computed average
        """
        debug("Computing average result")

        runs: float = len(individual_runs) * 1.0
        average_result = TestResult()
        sample_times_with_counts: Dict[int, int] = dict()

        for run in individual_runs:
            average_result.total_runtime_ms += run.total_runtime_ms / runs
            average_result.max_memory_usage_bytes += run.max_memory_usage_bytes / runs

            for time, memory in run.memory_usage_by_time.items():
                if time not in average_result.memory_usage_by_time:
                    average_result.memory_usage_by_time[time] = 0
                if time not in sample_times_with_counts:
                    sample_times_with_counts[time] = 0

                sample_times_with_counts[time] += 1
                average_result.memory_usage_by_time[time] += memory

        for time, memory in average_result.memory_usage_by_time.items():
            average_result.memory_usage_by_time[time] /= sample_times_with_counts[time]

        debug("Average runtime: {} ms".format(average_result.total_runtime_ms))
        debug("Average memory use: {} bytes".format(average_result.max_memory_usage_bytes))
        return InputSizeResult(average_result, individual_runs)

    def _run_test_container(self, image_name: str, runs: int) -> List[TestResult]:
        """
        Spins-up a container from the given image and runs the program for the given input 'run' number of times
        Returns the results for each run
        :param image_name: name of the docker image configured to run test for an input size
        :return: a list of Result objects - one for each run
        """

        results: List[TestResult] = []
        try:
            for i in range(runs):
                debug("Running trial number {} of {}".format(i + 1, runs))
                results.append(run_and_inspect_docker_image(image_name))
        except Exception as e:
            raise Exception("An error occurred during run test container", e)
        return results

    def _build_dockerfile_for_input(self, program_file_path: str, input_size: int, config: Config) -> str:
        """
        Builds a dockerfile to run the program for the given input size and returns the path to the dockerfile
        :param program_file_path: path to python program to test
        :param input_size: input size on which to test program
        :param config: user provided config
        :return: path to generated dockerfile
        """
        return build_python_dockerfile(program_file_path, config.get_args_for(input_size))

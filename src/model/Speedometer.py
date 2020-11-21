from src.model import Config
from src.model.analyzers.e2e_analysis.EndToEndAnalyzer import EndToEndAnalyzer
from src.model.analyzers.profile_analysis.ProfileAnalyzer import ProfileAnalyzer


class Speedometer:
    """
    Entry-point for the Speedometer analyses tool.
    Call run() to start analysis
    """

    def run(self, program_file_path: str, config: Config) -> None:
        """
        Runs the analysis on the user-provided python program
        :param program_file_path: path to the program to analyze
        :param config: config object for user-defined configuration
        """

        profiler = ProfileAnalyzer()
        profiler.analyze(program_file_path, config)
        profiler_results = profiler.get_results()

        e2e_analyzer = EndToEndAnalyzer()
        e2e_analyzer.analyze(program_file_path, config)
        e2e_results = e2e_analyzer.get_results()

        self.build_visualization(profiler_results, e2e_results)

    def build_visualization(self, profiler_results, e2e_results) -> None:
        """
        Builds the visualizations with the given results
        :param profiler_results: results from the profile analysis
        :param e2e_results: results from the end to end analysis
        """

        # TODO: implement this

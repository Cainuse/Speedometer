from src.model.util import Config
from src.model.analyzers.e2e_analysis.EndToEndAnalyzer import EndToEndAnalyzer
from src.model.analyzers.profile_analysis.ProfileAnalyzer import ProfileAnalyzer
from src.model.util.Logger import debug
from src.model.visualization_builders.BuildVisualization import build_visualization


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
        debug("Starting profile analysis")
        profiler = ProfileAnalyzer()
        profiler.analyze(program_file_path, config)
        profiler_results = profiler.get_results()
        debug("Profile analysis complete")

        debug("Starting end to end analysis")
        e2e_analyzer = EndToEndAnalyzer()
        e2e_analyzer.analyze(program_file_path, config)
        e2e_results = e2e_analyzer.get_results()
        debug("End to end analysis complete")

        build_visualization(program_file_path, profiler_results, e2e_results)

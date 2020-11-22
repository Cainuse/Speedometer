import os
import sys
import re

class function_runtime:
    """
    Python runtime of function as given by Scalene
    """
    file: str
    name: str
    tot_run_time: float

    def __init__(self, file, name, runtime):
        self.file = file
        self.name = name
        self.tot_run_time = runtime

class line_by_line_runtime:
    """
    Python runtime of individual line as given by Scalene
    """
    file: str
    line_num: int
    tot_run_time: float

    def __init__(self, file, linenum, runtime):
        self.file = file
        self.line_num = linenum
        self.tot_run_time = runtime

class ProfileAnalyzer:

    results: dict = {"e2e": {}, "function": [], "line_by_line": []}

    def analyze(self,program_file_path: str) -> None:
        """
        Runs profile analyses on the given program
        :param program_file_path: path to the program to analyze
        """

        p = os.popen('scalene ' + program_file_path)
        output = p.read()
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        result = ansi_escape.sub('', output)
        chart_start = re.compile(r'\n(.*)\n(.*)\s+Line(\s+)\│Time %(\s+)\│Time %(\s+)\│Sys(\s+)(.+\n)*')
        chart_str = re.search(chart_start,result)
        if (chart_str != None):
            outArr = chart_str.group(0).splitlines()
            for i in range(len(outArr)):
                outArr[i] = outArr[i].strip()
            self.processLines(outArr)
        else:
            print("File was too short for scalene to analyze")

    def processLines(self, arr: list):
        """
        Helper function for processing Scalene output
        :param arr: Scalene output split by line
        """

        file_dict = self.ScaleneArrayStrip(arr, "% of time", 5)

        for a in file_dict:
            file_name = a.split(": % of time")[0]
            reference_time = self.getRefTime(a)
            func = function_runtime(file_name, "", 0.0)

            for l in file_dict[a]:
                line = line_by_line_runtime(file_name, 0, 0.0)
                line_split = l.split("│")

                if line_split[4].startswith("def") and line_split[4].endswith(":"):
                    if func.name != "" and func.tot_run_time > 0.0:
                        self.results["function"].append(func)
                    func = function_runtime(file_name, line_split[4][4:len(line_split[4]) - 1], 0.0)

                if not (line_split[1].isspace() or line_split[2].isspace()):
                    line.line_num = int(line_split[0].strip())
                    lineTime = int(line_split[1].strip().replace("%", "")) / 100 * reference_time
                    line.tot_run_time = lineTime
                    func.tot_run_time += lineTime

                if line.tot_run_time > 0.0:
                    self.results["line_by_line"].append(line)

            if func.name != "" and func.tot_run_time > 0.0:
                self.results["function"].append(func)

    def ScaleneArrayStrip(self, arr: list, split_str: str, header_len: int) -> dict:
        """
        Helper function to split Scalene output into map of file header to lines in file
        :param arr: Scalene output split by line
        :param split_str: String that determines header line
        :param header_len: Line length of Scalene header to remove
        """
        ret = {}
        start = len(arr)
        for i in range(len(arr)):
            if split_str in arr[i]:
                end = i - 1
                if end > start:
                    ret[arr[start]] = arr[start + header_len:end]
                start = i
            if i == len(arr) - 1:
                ret[arr[start]] = arr[start + header_len:i]
        return ret

    def getRefTime(self, header: str):
        """
        Helper function for calculating time from Scalene output
        :param header: Scalene output line that includes filename, total time, and % of time for file
        """

        timeString = header.split(": % of time = ")[1]
        timeSplit = timeString.split("% out of   ")
        timeSplit[1] = timeSplit[1].replace("s.", "")
        return float(timeSplit[0]) / 100 * float(timeSplit[1])

    def get_results(self) -> dict:
        """
        :return: the results from the analysis as a dict
        """

        return self.results
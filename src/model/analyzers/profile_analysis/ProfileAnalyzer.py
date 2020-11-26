from src.model import Config
import os
import sys
import re

class function_runtime:
    """
    Python runtime of function as given by Scalene
    """
    filename: str
    name: str
    total_run_time: float
    total_memory: float

    def __init__(self, filename, name, runtime, memory):
        self.filename = filename
        self.name = name
        self.total_run_time = runtime
        self.total_memory = memory

class line_by_line_runtime:
    """
    Python runtime of individual line as given by Scalene
    """
    filename: str
    line_num: int
    line_text: str
    total_run_time: float
    total_memory: float

    def __init__(self, filename, linenum, runtime, memory, linetext):
        self.filename = filename
        self.line_num = linenum
        self.total_run_time = runtime
        self.total_memory = memory
        self.line_text = linetext

class class_runtime:
    """
    Python runtime of function as given by Scalene
    """
    filename: str
    name: str
    total_run_time: float
    total_memory: float

    def __init__(self, filename, name, runtime, memory):
        self.filename = filename
        self.name = name
        self.total_run_time = runtime
        self.total_memory = memory

class ProfileAnalyzer:

    results: dict = {"class": [], "function": [], "line_by_line": []}

    def analyze(self,program_file_path: str, config:Config) -> None:
        """
        Runs profile analyses on the given program
        :param program_file_path: path to the program to analyze
        :param config: config object for user-defined configuration
        """

        p = os.popen('scalene ' + program_file_path)
        output = p.read()
        # parse Scalene output, removing formatting & any logging from user files
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        result = ansi_escape.sub('', output)
        chart_start = re.compile(r'\n(.*)\n(.*)\n(.*)\s+Line(\s+)\│Time %(\s+)\│Time %(\s+)\│Sys(\s+)(.+\n)*')
        chart_str = re.search(chart_start,result)
        # send array of Scalene output split by newline
        if (chart_str != None):
            outArr = chart_str.group(0).splitlines()
            for i in range(len(outArr)):
                outArr[i] = outArr[i].strip()
            self.processLines(outArr)
        else:
            raise RuntimeError("File was too short for scalene to analyze")

    def processLines(self, arr: list):
        """
        Helper function for processing Scalene output
        :param arr: Scalene output split by line
        """
        # Map file header (with name & total time) to line contents (with %time and %mem per line)
        # 5 lines without memory usage, 6 lines with
        file_dict = self.ScaleneArrayStrip(arr, "Memory usage:", "% of time", 5)

        for a in file_dict:
            # Get total file time from header in ms
            total_memory = 0.0
            if len(a.split("\n")) > 1:
                file_name = (a.split("\n")[1]).split(": % of time")[0]
                mem_num = ((a.split("\n")[0]).split("(max:")[1]).split("MB)")[0]
                total_memory = float(mem_num)
            else:
                file_name = a.split(": % of time")[0]
            reference_time = self.getRefTime(a) * 1000.0
            func = function_runtime(file_name, "", 0.0, 0.0)
            clas = class_runtime(file_name, "", 0.0, 0.0)

            for l in file_dict[a]:
                line_split = l.split("│")
                code_position = len(line_split)-1
                line = line_by_line_runtime(file_name, 0, 0.0, 0.0, line_split[code_position])
                # Create function object when line starts with "def"
                if line_split[code_position].strip().startswith("def") and line_split[code_position].strip().endswith(":"):
                    if func.name != "" and func.total_run_time > 0.0:
                        self.results["function"].append(func)
                    func_name = line_split[code_position].strip()[4:len(line_split[code_position]) - 1]
                    func = function_runtime(file_name, func_name, 0.0, 0.0)
                # Create class object when lines starts with "class"
                if line_split[code_position].strip().startswith("class") and line_split[code_position].strip().endswith(":"):
                    if clas.name != "" and clas.total_run_time > 0.0:
                        self.results["class"].append(clas)
                    class_name = line_split[code_position].strip()[6:len(line_split[code_position]) - 1]
                    clas = class_runtime(file_name, class_name, 0.0, 0.0)
                # If Scalene output determines line has significant time, calculate time in ms and add it to line/function/class objects
                line.line_num = int(line_split[0].strip())
                if not (line_split[1].isspace() or line_split[2].isspace()):
                    lineTime = (int(line_split[1].strip().replace("%", "")) + int(line_split[2].strip().replace("%", ""))) / 100 * reference_time
                else:
                    lineTime = 0.0
                line.total_run_time = lineTime
                func.total_run_time += lineTime
                clas.total_run_time += lineTime
                if len(line_split) > 5:
                    line_memory = total_memory
                    # TODO
                    line.total_memory = line_memory
                    func.total_memory += lineTime
                    clas.total_memory += lineTime
                # Add line object to results
                self.results["line_by_line"].append(line)
            # If function object exists with data, add to results
            if func.name != "" and func.total_run_time > 0.0:
                self.results["function"].append(func)
            # If class object exists with data, add to results
            if clas.name != "" and clas.total_run_time > 0.0:
                self.results["class"].append(clas)

    def ScaleneArrayStrip(self, arr: list, prim_split_str: str, sec_split_str: str, header_len: int) -> dict:
        """
        Helper function to split Scalene output into map of file header to lines in file
        :param arr: Scalene output split by line
        :param prim_split_str: First string that determines header line
        :param sec_split_str: If first string not found, second string that determines header line
        :param header_len: Line length of Scalene header to remove
        """
        ret = {}
        start = len(arr)
        lines_start_pos = header_len
        key_string = ""
        i = 0
        while i < len(arr):
            if arr[i].strip().startswith(prim_split_str):
                end = i - 1
                if end > start:
                    ret[key_string] = arr[lines_start_pos:end]
                start = i
                key_string = arr[start] + "\n" + arr[start + 1]
                lines_start_pos = start+header_len+1
                i += 1
            else:
                if sec_split_str in arr[i]:
                    end = i - 1
                    if end > start:
                        ret[key_string] = arr[lines_start_pos:end]
                    start = i
                    key_string = arr[start]
                    lines_start_pos = start + header_len
            if i == len(arr) - 1:
                ret[arr[start]] = arr[start + header_len:i]
            i += 1
        return ret

    def getRefTime(self, header: str) -> float:
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

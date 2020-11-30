from src.model.analyzers.e2e_analysis.docker.DockerContainerRunner import create_docker_container
from src.model.analyzers.e2e_analysis.docker.DockerImageBuilder import load_docker_image, build_docker_image
from src.model.analyzers.e2e_analysis.docker.DockerfileMaker import build_scalene_dockerfile
from src.model.util import Config
from subprocess import check_output
import re
import math
from typing import Union, List
import os

from src.model.util.Logger import debug

class function_runtime:
    """
    Python runtime of function as given by Scalene
    """
    filename: str
    name: str
    total_run_time: float
    total_memory: float
    memory_percentage_of_total: float
    time_percentage_of_total:int

    def __init__(self, filename, name, runtime, memory, time_percentage, memory_percentage=None):
        self.filename = filename
        self.name = name
        self.total_run_time = runtime
        self.total_memory = memory
        self.time_percentage_of_total = time_percentage
        self.memory_percentage_of_total = memory_percentage

    def __eq__(self, other):
        if (isinstance(other, function_runtime)):
            return ((self.filename == other.filename) and (self.name == other.name) and \
                (self.total_run_time == other.total_run_time) and (self.total_memory == other.total_memory)  \
                    and (self.memory_percentage_of_total ==other.memory_percentage_of_total) and\
                    (self.time_percentage_of_total == other.time_percentage_of_total))
        return False

class line_by_line_runtime:
    """
    Python runtime of individual line as given by Scalene
    """
    filename: str
    line_num: int
    line_text: str
    total_run_time: float
    total_memory: float
    memory_percentage_of_total: float
    time_percentage_of_total:int

    def __init__(self, filename, linenum, runtime, memory, linetext, time_percentage):
        self.filename = filename
        self.line_num = linenum
        self.total_run_time = runtime
        self.total_memory = memory
        self.line_text = linetext
        self.time_percentage_of_total = time_percentage
        self.memory_percentage_of_total = -1

    def __eq__(self, other):
        if isinstance(other, line_by_line_runtime):
            return ((self.filename == other.filename) and (self.line_num == other.line_num) and
                    (self.line_text == other.line_text) and (self.total_run_time == other.total_run_time) and
                    (self.total_memory == other.total_memory) and (self.memory_percentage_of_total ==other.memory_percentage_of_total) and
                    (self.time_percentage_of_total == other.time_percentage_of_total))
        return False

class class_runtime:
    """
    Python runtime of function as given by Scalene
    """
    filename: str
    name: str
    total_run_time: float
    total_memory: float
    memory_percentage_of_total: float
    time_percentage_of_total:int
    class_functions: list # These will be integers, representing the index in results["function"]

    def __init__(self, filename, name, runtime, memory,time_percentage, memory_percentage=None, class_functions=None):
        self.filename = filename
        self.name = name
        self.total_run_time = runtime
        self.total_memory = memory
        self.time_percentage_of_total = time_percentage
        self.class_functions = class_functions if class_functions is not None else []
        self.memory_percentage_of_total = memory_percentage

    def __eq__(self, other):
        if (isinstance(other, class_runtime)):
            return ((self.filename == other.filename) and (self.name == other.name) and
                    (self.total_run_time == other.total_run_time) and (self.total_memory == other.total_memory)
                    and (self.memory_percentage_of_total ==other.memory_percentage_of_total) and
                    (self.time_percentage_of_total == other.time_percentage_of_total) and (self.class_functions == other.class_functions))
        return False

class ProfileAnalyzer:

    results: dict = {"class": [], "function": [], "line_by_line": []}

    def analyze(self, program_file_path: str, config: Config) -> None:
        """
        Runs profile analyses on the given program
        :param program_file_path: path to the program to analyze
        :param config: config object for user-defined configuration
        """
        self.results={"class": [], "function": [], "line_by_line": []}
        debug("Running scalene profile analysis")
        
        args = config.get_args_for(max(config.get_input_sizes()))
        debug("Using input size {} for scalene analysis".format(max(config.get_input_sizes())))
        debug("Starting scalene run")
        # output = check_output(scalene_args, encoding='UTF-8', cwd=os.path.abspath(program_file_dir))
        output = self._run_scalene_in_docker(program_file_path, args)
        debug(output)
        debug("Parsing output")
        self.parseOutput(output)

    def _run_scalene_in_docker(self, program_file_path, scalene_args: List[str]):
        debug("Loading the scalene docker container")
        load_docker_image(os.path.abspath("resources/scalene.tar"))
        output_path = build_scalene_dockerfile(program_file_path, scalene_args)
        image_name = build_docker_image(output_path)
        container = create_docker_container(image_name)
        debug("Starting the scalene docker container")
        container.start()
        container.wait()
        output =  bytes(container.logs()).decode('UTF-8')
        container.stop()
        return output

        
    def parseOutput(self,output:str):
        # parse Scalene output, removing formatting & any logging from user files
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        result = ansi_escape.sub('', output)
        chart_start = re.compile(r'(.*)\n(.*)\n(.*)\n(.*)\s+Line(\s+)\│Time %(\s+)\│Time %(\s+)\│Sys(\s+)(.+\n)*')
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
        debug("Processing scalene output...")
        file_dict = self.ScaleneArrayStrip(arr, "Memory usage:", "% of time", 6)

        for a in file_dict:
            # Get total file time from header in ms
            total_memory = 0.0
            if len(a.split("\n")) > 1:
                debug("CHECKING FILENAME - Full Scalene message: {}".format(a))
                debug("Split Message: {}".format(a.split("\n")[1]))
                file_name = (a.split("\n")[1]).split(": % of time")[0]
                mem_num = ((a.split("\n")[0]).split("(max:")[1]).split("MB)")[0]
                total_memory = float(mem_num)
            else:
                file_name = a.split(": % of time")[0]
            reference_time = self.getRefTime(a) * 1000.0
            func = function_runtime(file_name, "", 0.0, 0.0,0)
            func_indentation = ""
            clas = class_runtime(file_name, "", 0.0, 0.0,0)
            class_indentation = ""
            debug("Total Runtime Calculated: {}ms".format(reference_time))
            debug("Total Memory Calculated: {}MB".format(total_memory))

            for l in file_dict[a]:
                line_split = l.split("│")
                code_position = len(line_split)-1
                line = line_by_line_runtime(file_name, 0, 0.0, 0.0, line_split[code_position],0)
                leading_whitespace = re.match(r"\s*", line_split[code_position]).group()
                # Create function object when line starts with "def"
                if line_split[code_position].strip().startswith("def") and line_split[code_position].strip().endswith(":"):
                    if func.name != "" and func.total_run_time > 0.0:
                        self.computeMemoryPercentageForSection(func,total_memory)
                        self.results["function"].append(func)
                    func_name = line_split[code_position].strip()[4:len(line_split[code_position].strip()) - 1]
                    func = function_runtime(file_name, func_name, 0.0, 0.0,0)
                # Create class object when lines starts with "class"
                elif line_split[code_position].strip().startswith("class") and line_split[code_position].strip().endswith(":"):
                    if clas.name != "" and clas.total_run_time > 0.0:
                        self.computeMemoryPercentageForSection(clas,total_memory)
                        self.results["class"].append(clas)
                    class_name = line_split[code_position].strip()[6:len(line_split[code_position].strip()) - 1]
                    clas = class_runtime(file_name, class_name, 0.0, 0.0,0)
                #If indentation matches that of previous function
                elif leading_whitespace == func_indentation and func.name!="":
                    self.computeMemoryPercentageForSection(func,total_memory)
                    self.results["function"].append(func)
                    if (clas.name !=""):
                        clas.class_functions.append(len(self.results["function"])-1)
                    func = function_runtime(file_name, "", 0.0, 0.0,0)
                #If indentation matches that of previous class
                elif leading_whitespace == class_indentation and clas.name!="":
                    self.computeMemoryPercentageForSection(clas,total_memory)
                    self.results["class"].append(clas)
                    clas = class_runtime(file_name, "", 0.0, 0.0,0)

                # If Scalene output determines line has significant time, calculate time in ms and add it to line/function/class objects
                line.line_num = int(line_split[0].strip())
                if not (line_split[1].isspace() and line_split[2].isspace()):
                    if line_split[1].isspace() and not(line_split[2].isspace()):
                        lineTimePercentage = int(line_split[2].strip().replace("%", ""))
                        lineTime = int(line_split[2].strip().replace("%", "")) / 100 * reference_time
                    elif line_split[2].isspace() and not(line_split[1].isspace()):
                        lineTimePercentage = int(line_split[1].strip().replace("%", ""))
                        lineTime = int(line_split[1].strip().replace("%", "")) / 100 * reference_time
                    else:
                        lineTimePercentage = (int(line_split[1].strip().replace("%", "")) + int(line_split[2].strip().replace("%", "")))
                        lineTime = (int(line_split[1].strip().replace("%", "")) + int(line_split[2].strip().replace("%", ""))) / 100 * reference_time
                else:
                    lineTime = 0.0
                    lineTimePercentage = 0
                self.updateRelevantData(line,func,clas,line_split,lineTime,lineTimePercentage,total_memory)
            # If function object exists that hasn't been saved (i.e. near the end of the file), add to results
            if func.name != "" and func.total_run_time > 0.0:
                self.computeMemoryPercentageForSection(func,total_memory)
                self.results["function"].append(func)
                if (clas.name !=""):
                    clas.class_functions.append(len(self.results["function"])-1)
            # If class object exists that hasn't been saved (i.e. near the end of the file), add to results
            if clas.name != "" and clas.total_run_time > 0.0:
                self.computeMemoryPercentageForSection(clas,total_memory)
                self.results["class"].append(clas)

    def computeMemoryPercentageForSection(self,section: Union[function_runtime, class_runtime, line_by_line_runtime],total_memory:float):
        if (math.isclose(total_memory,0.0)):            
            section.memory_percentage_of_total = 0.0            
        else: 
            section.memory_percentage_of_total = section.total_memory / total_memory *100

    def updateRelevantData(self,line:line_by_line_runtime, func:function_runtime, clas:class_runtime, line_split:list, lineTime:float, lineTimePercentage:int, total_memory:float):
        line.total_run_time = lineTime
        func.total_run_time += lineTime
        clas.total_run_time += lineTime
        line.time_percentage_of_total = lineTimePercentage
        func.time_percentage_of_total += lineTimePercentage
        clas.time_percentage_of_total += lineTimePercentage
        if len(line_split) > 5:
            if len(line_split[5].strip())==0:
                line_memory = 0.0
            else:
                line_memory = float(line_split[5])
            line.total_memory = line_memory
            self.computeMemoryPercentageForSection(line,total_memory)

            func.total_memory += line_memory
            clas.total_memory += line_memory
        # Add line object to results
        self.results["line_by_line"].append(line)

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
                #This is the case where the memory is properly displayed
                end = i - 1
                if end > start:
                    ret[key_string] = arr[lines_start_pos:end]
                start = i
                key_string = arr[start] + "\n" + arr[start + 1]
                lines_start_pos = start+header_len+1
                i += 1
            else:
                if sec_split_str in arr[i]:
                    #This is the case where the memory is properly displayed, should not appear in practice
                    end = i - 1
                    if end > start:
                        ret[key_string] = arr[lines_start_pos:end]
                    start = i
                    key_string = arr[start]
                    lines_start_pos = start + header_len
            if i == len(arr) - 1:
                ret[key_string] = arr[start + header_len:i]
            i += 1
        return ret

    def getRefTime(self, header: str) -> float:
        """
        Helper function for calculating time from Scalene output
        :param header: Scalene output line that includes filename, total time, and % of time for file
        """
        timeString = header.split(": % of time =")[1]
        timeSplit = timeString.split("% out of")
        timeSplit[1] = timeSplit[1].replace("s.", "")
        return float(timeSplit[0].strip()) / 100 * float(timeSplit[1].strip())


    def get_results(self) -> dict:
        """
        :return: the results from the analysis as a dict
        """

        return self.results

class ProfileAnalyzer:

    results: {"e2e": {}, "function": [], "line_by_line": []}

    def analyze(self, program_file_path: str) -> None:
        """
        Runs profile analyses on the given program
        :param program_file_path: path to the program to analyze
        """

        if len(sys.argv) > 1:
            p = os.popen('scalene ' + program_file_path)
            output = p.read()
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            result = ansi_escape.sub('', output)
            outArr = result.splitlines()
            for i in range(len(outArr)):
                outArr[i] = outArr[i].strip()
            processLines(outArr)
        else:
            print("No file given to analyze.")

    def processLines(self, arr: list):
        """
        Helper function for processing Scalene output
        :param arr: Scalene output split by line
        """

        fileDict = {}
        start = 0
        for i in range(len(arr)):
            if "% of time =" in arr[i]:
                end = i - 1
                if (end > start):
                    fileDict[arr[start]] = arr[start + 5:end]
                start = i
            if i == len(arr) - 1:
                fileDict[arr[start]] = arr[start + 5:i]
        for a in fileDict:
            file_name = a.split(": % of time")[0]
            referenceTime = getRefTime(a)
            func = {"file": file_name, "name": "", "tot_run_time": 0}
            for l in fileDict[a]:
                line = {"file": file_name, "tot_run_time": 0}
                lineSplit = l.split("│")
                if lineSplit[4].startswith("def") and lineSplit[4].endswith(":"):
                    if func["name"] != "" and func["tot_run_time"] > 0:
                        results["function"].append(func)
                    func = {"file": file_name, "name": lineSplit[4][4:len(lineSplit[4]) - 1], "tot_run_time": 0}
                if not (lineSplit[1].isspace() or lineSplit[2].isspace()):
                    line["line_num"] = lineSplit[0].strip()
                    lineTime = int(lineSplit[1].strip().replace("%", "")) / 100 * referenceTime
                    line["tot_run_time"] = lineTime
                    func["tot_run_time"] += lineTime
                if line["tot_run_time"] > 0:
                    results["line_by_line"].append(line)
            if func["name"] != "" and func["tot_run_time"] > 0:
                results["function"].append(func)

    def getRefTime(self, header: str):
        """
        Helper function for calculating time from Scalene output
        :param header: Scalene output line that includes filename, total time, and % of time for file
        """

        timeString = header.split(": % of time =  ")[1]
        timeSplit = timeString.split("% out of   ")
        timeSplit[1] = timeSplit[1].replace("s.", "")
        return float(timeSplit[0]) / 100 * float(timeSplit[1])

    def get_results(self) -> dict:
        """
        :return: the results from the analysis as a dict
        """

        return results
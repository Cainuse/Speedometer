import os
import subprocess
import json
from datetime import datetime


class EndToEndAnalyzer:

    def analyze(self, program_file_path: str, config_file_path: str) -> None:
        """
        Runs e2e analyses on the given program
        :param program_file_path: path to the program to analyze
        :param config_file_path: path to the config file
        """
        # Copy content of target file and paste it into new file created
        target_file = open(program_file_path, "r")
        content = target_file.read()

        target_file_copy = open("test.py", "w+")
        target_file_copy.write(content)
        target_file_copy.close()

        # Create Dockerfile
        docker_file = open("Dockerfile", "w+")
        FROM = "FROM python:3"
        ADD = "ADD test.py /"
        CMD = "CMD [ \"python\", \"./test.py\"]"

        docker_file.write(FROM + "\n" + ADD + "\n" + CMD)
        docker_file.close()

        # Build Docker Image
        os.system("docker build -t e2e .")

        # Run Docker Image in a container
        os.system("docker run --name e2e e2e")

        # Get information about the docker container
        output = subprocess.run(["docker", "inspect", "e2e"], stdout=subprocess.PIPE)

        # Convert bytes to string
        output = output.stdout.decode('utf-8')

        # Convert String to json and extract data
        output_json = json.loads(output)

        container = output_json[0]

        container_state = container["State"]

        container_start_time = container_state["StartedAt"]
        container_state_time = datetime.strptime(container_start_time[:-2], "%Y-%m-%dT%H:%M:%S.%f").microsecond

        container_end_time = container_state["FinishedAt"]
        container_end_time = datetime.strptime(container_end_time[:-2], "%Y-%m-%dT%H:%M:%S.%f").microsecond

        # Total runtime in microseconds
        print("Total Runtime is: " + str(container_end_time - container_state_time) + " microseconds")
        print("Total Runtime is: " + str((container_end_time - container_state_time) / 10 ** 6) + " seconds")

        # Delete Created Docker image and container after script executes
        os.system("docker rm e2e && docker rmi e2e")

    def get_results(self) -> dict:
        """
        :return: the results from the analysis as a dict
        """

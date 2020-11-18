import os

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

        # Run Docker Image in a container and immediately delete it after execution
        os.system("docker run --rm e2e")

    def get_results(self) -> dict:
        """
        :return: the results from the analysis as a dict
        """

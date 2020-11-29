import shutil
import webbrowser
import os
import subprocess

from src.model.util.Logger import debug

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", ".."))
CLIENT_SRC = os.path.join(PROJECT_PATH, "src", "client")


def package_visualization_and_open() -> None:
    """
    Run out-dated build folder removal, build react client,
    move build files to dist folder, and run the generated html file in that order
    """
    _clean_up()
    _build_client()
    dst = _move_build_files()
    try:
        _run_build_file_in_browser(dst)
    except:
        print(
            "Failed to open the generated html file. Please open dist/build/index.html with a "
            "web browser manually.")


def _clean_up() -> None:
    """
    Removes the build folder in the dist dir if it exists so that the new one can be moved there
    """
    build_path = os.path.join(PROJECT_PATH, "dist", "build")
    if os.path.exists(build_path):
        shutil.rmtree(build_path)


def _build_client() -> None:
    """
    Builds the react client
    """

    yarn_build_succ_msg = "The build folder is ready to be deployed."

    try:
        debug("Installing yarn dependencies for visualization")
        debug(CLIENT_SRC)
        process = subprocess.Popen(["yarn", "install"], cwd=CLIENT_SRC)  # TODO: PIPE if debug is off
        process.wait()
        debug("Compiling visualization code")
        build_output = subprocess.check_output(["yarn", "build"], cwd=CLIENT_SRC).decode("utf-8")
        if yarn_build_succ_msg not in build_output:
            raise Exception("An error occurred while building client")
    except Exception as e:
        raise Exception("Could not build visualization. Ensure you have the latest version of yarn installed.", e)


def _move_build_files() -> str:
    """
    Moves the files in the client build folder to the dist folder
    :return: Path of the destination folder
    :raises: Exception if any of the paths are invalid (file does not exist)
    """

    src_path = os.path.join(PROJECT_PATH, "src", "client", "build")
    dst_path = os.path.join(PROJECT_PATH, "dist")
    shutil.move(src_path, dst_path)
    return dst_path


def _run_build_file_in_browser(dst_path) -> None:
    """
    Runs the generated HTML file in browser
    :raises: Exception if any of the paths are invalid (file does not exist), or the file is not of correct format
    """
    debug("Opening visualization in browser")
    try:
        webbrowser.open('file://' +
                        os.path.join(dst_path, "build", "index.html"))
    except Exception as e:
        raise Exception("Could not open file in browser.")

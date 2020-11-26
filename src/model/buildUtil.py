import shutil
import webbrowser
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_post_process() -> None:
    """
    Run out-dated build folder removal, build react client,
    move build files to dist folder, and run the generated html file in that order
    """
    _clean_up()
    _build_client()
    dst = _move_build_files()
    _run_build_file_in_browser(dst)


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
    os.chdir("./client")
    os.system("yarn install && yarn build")


def _move_build_files() -> str:
    """
    Copies the files in the client build folder to the dist folder
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
    try:
        webbrowser.open('file://' + os.path.join(dst_path, "build", "index.html"))
    except Exception as e:
        raise Exception("Could not open file in browser.")
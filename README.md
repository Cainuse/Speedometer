# Speedometer

## Requirements

- Python 3.x
- Docker (with sudo privileges if on linux)
    - You also need to download the Scalene docker image from [here](https://drive.google.com/file/d/11ToQiG0ONLSz_8-D3dS5OLkXvDHIZyJC/view?usp=sharing) and place it under `<project root>/resources`
- Other python dependencies:
    - Run `pip install -r requirements.txt` in the root folder of the project
- Yarn

## Setup

1. Download all requirements from the previous section (you may need to restart your computer)
2. Clone the repo into your local computer
3. Run `pip install -r requirements.txt` in the root folder of the project if you haven't already
4. Download the Scalene docker image tar and place it under `<project root>/resources` if you haven't already

## Usage

Test your setup using one of our sample scripts under `<project root>/samples`. Each sub-directory contains a python script as well as a configuration file.

For this example, we will run `dumb_sort` (which is just insertion sort):

From the root directory of the project run (assuming your Python 3.x installation is under `python3`):

```python
python3 src/MainCLI.py -v --program "samples/merge_sort/Merge.py" --config "samples/merge_sort/merge_config.json"
```

where `--program` gives the path to the python file, `--config` gives the path to the config file and `-v` is a (optional) flag for verbose output

Let the program run for a few minutes. If this is the first time you're running Speedometer, this can take up to 10 mins

Once the analysis is complete, a browser window should automatically open to show a visualization of the results. If it does not open automatically, you can open it manually through `<project root>/dist/build/index.html`

## Limitations

* Mac OS or Linux only
* Does not support multi-file projects yet

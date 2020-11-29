# Speedometer - Prototype Design

## Description of Project

Speedometer performs dynamic analysis of a Python program to empirically calculate its time/space complexity, as well as provide a module-by-module breakdown of CPU time usage and memory usage.

The user provides their python code and a configuration file to help run their code, and the program returns a visualization of the results.

## Sample User Input

### The Program to Test

For this example, we will test the performance of a Python file called `unknownComplexity.py`. 

This Python program takes two arguments - a file name as a string, and an integer. For example, the program may be run by the following command:

```python
python unknownComplexity.py "a file name" 200
```

It does not matter how the program uses the inputs, except for the fact that the integer associated with the second command dictates the 'size' of the input that the program must work on.

### The Config File

This file contains commands that will run the `unknownComplexity.py` with different input sizes. For example:

```json
{
    "input_size": {
        "1": ["a file name", 1],
        "10": ["a file name", 10],
        "100": ["a file name", 100],
        "1000": ["a file name", 1000],
        "10000": ["a file name", 10000],
    }
}
```

### Running the analysis

The user can then run the analysis using the following command:

```bash
speedometer /path/to/unknownComplexity.py /path/to/config/file.json
```

## Wireframe for visual output

[View the wireframe on Figma](https://www.figma.com/file/4YQEQzz0XZD33ePeqh8TxW/FML-Complexity-2.0?node-id=0%3A1)

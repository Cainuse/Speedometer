from src.model.analyzers.profile_analysis import ProfileAnalyzer
import pytest  

def testParseOutputNegativeCase():
    with pytest.raises(RuntimeError) as e_info:
        p = ProfileAnalyzer.ProfileAnalyzer()
        p.parseOutput("")

def testcomputeMemoryPercentageClass():
    p = ProfileAnalyzer.ProfileAnalyzer()
    c = ProfileAnalyzer.class_runtime('file/generic','generic',200, 20)
    p.computeMemoryPercentageForSection(c,200)
    assert  c.memory_percentage_of_total== 0.10

def testcomputeMemoryPercentageFunc():
    p = ProfileAnalyzer.ProfileAnalyzer()
    c = ProfileAnalyzer.function_runtime('file/generic','foo',200, 10)
    p.computeMemoryPercentageForSection(c,200)
    assert  c.memory_percentage_of_total== 0.05

def testcomputeMemoryPercentageLine():
    p = ProfileAnalyzer.ProfileAnalyzer()
    c = ProfileAnalyzer.function_runtime('file/generic','l',200, 10)
    p.computeMemoryPercentageForSection(c,200)
    assert  c.memory_percentage_of_total== 0.05

def testScaleneArrayStrip():
    p = ProfileAnalyzer.ProfileAnalyzer()
    arr = ["","Memory usage:","","","","","",'test-data','']
    file_dict = p.ScaleneArrayStrip(arr, "Memory usage:", "% of time", 6)
    assert len(file_dict) == 1
    assert len(file_dict["Memory usage:\n"]) == 1
    assert file_dict["Memory usage:\n"][0] == 'test-data'

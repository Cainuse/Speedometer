from src.model.analyzers.profile_analysis.ProfileAnalyzer import class_runtime
from src.model.analyzers.profile_analysis import ProfileAnalyzer
import pytest 

def testParseOutputNegativeCase():
    with pytest.raises(RuntimeError) as e_info:
        p = ProfileAnalyzer.ProfileAnalyzer()
        p.parseOutput("Scalene: Program did not run for long enough to profile.")

    with pytest.raises(RuntimeError) as e:
        p = ProfileAnalyzer.ProfileAnalyzer()
        p.parseOutput("Scalene failed to find ")

def testParseOutputBaseCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    test_lines = ["\nMemory usage: ▀▄ (max:   1.00MB)",                                       
                  "sratch.py: % of time = 100.00% out of   0.09s." ,                               
                  "╷       ╷        ╷    ╷       ╷      ╷              ╷       ╷ ",                                                   
                  "Line │Time % │Time %  │Sys │Mem %  │Net   │Memory usage  │Copy   │       ",                                             
                  "│Python │native  │%   │Python │(MB)  │over time / % │(MB/s) │sratch.py ",                                          
                  "╺━━━━━━┿━━━━━━━┿━━━━━━━━┿━━━━┿━━━━━━━┿━━━━━━┿━━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸",
                  "1 │       │        │    │  100% │    1 │▀100%         │       │for i in range(6000):",                               
                  "2 │       │        │    │       │      │              │       │    x = i*i" ,                             
                  "3 │   99% │     1% │    │       │      │              │       │    print(x)",
                  "       ╵       ╵        ╵    ╵       ╵      ╵              ╵       ╵\n" ]
    input = "\n".join(test_lines)
    p.parseOutput(input)
    res = p.get_results()
    assert res["function"] == []
    assert res["class"] == []

    # expected_line_by_line = []
    first_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",1,0,1,"for i in range(6000):",0)
    first_line.memory_percentage_of_total = 100.0
    second_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",2,0,0,"    x = i*i",0)
    second_line.memory_percentage_of_total = 0.0
    third_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",3,90.0,0,"    print(x)",100)
    third_line.memory_percentage_of_total = 0.0
    
    valid = res["line_by_line"][0] == first_line and res["line_by_line"][1] == second_line and res["line_by_line"][2] == third_line
    if not(valid):
        raise Exception()

def testParseOutputLinesFunctionCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    test_lines = ["\nMemory usage: ■▀■▀■▀■▀ (max:   2.00MB)",                                       
                  "sratch.py: % of time = 100.00% out of   0.06s." ,                               
                  "╷       ╷        ╷    ╷       ╷      ╷              ╷       ╷ ",                                                   
                  "Line │Time % │Time %  │Sys │Mem %  │Net   │Memory usage  │Copy   │       ",                                             
                  "│Python │native  │%   │Python │(MB)  │over time / % │(MB/s) │sratch.py ",                                          
                  "╺━━━━━━┿━━━━━━━┿━━━━━━━━┿━━━━┿━━━━━━━┿━━━━━━┿━━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸",
                  "     1 │       │        │    │       │      │              │       │def process(y):",                               
                  "     2 │       │        │    │       │      │              │       │    for i in range(y):" ,                             
                  "     3 │       │        │    │  100% │    0 │▄▄            │       │        x = i*i",
                  "     4 │   99% │     1% │    │  100% │    2 │■▀■▀■▀ 80%    │       │        print(x)",
                  "     5 │       │        │    │       │      │              │       │",
                  "     6 │       │        │    │       │      │              │       │process(6000)",
                  "       ╵       ╵        ╵    ╵       ╵      ╵              ╵       ╵\n" ]
    input = "\n".join(test_lines)
    p.parseOutput(input)
    res = p.get_results() 

    function_data = ProfileAnalyzer.function_runtime("sratch.py","process(y)",60.0,2.0,100)
    function_data.memory_percentage_of_total = 100.0
    assert res["function"][0] == function_data
    assert res["class"] == []

    # expected_line_by_line = []
    first_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",1,0,0,"def process(y):",0)
    first_line.memory_percentage_of_total = 0.0
    second_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",2,0,0,"    for i in range(y):",0)
    second_line.memory_percentage_of_total = 0.0
    third_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",3,0,0,"        x = i*i",0)
    third_line.memory_percentage_of_total = 0.0
    fourth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",4,60,2,"        print(x)",100)
    fourth_line.memory_percentage_of_total = 100.0
    fifth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",5,0,0,"",0)
    fifth_line.memory_percentage_of_total = 0.0
    sixth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",6,0,0,"process(6000)",0)
    sixth_line.memory_percentage_of_total = 0.0
    
    valid = res["line_by_line"][0] == first_line and res["line_by_line"][1] == second_line and res["line_by_line"][2] == third_line and\
        res["line_by_line"][3] == fourth_line and res["line_by_line"][4] == fifth_line and res["line_by_line"][5] == sixth_line
    if not(valid):
        raise Exception()

def testParseOutputClassCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}
    test_lines = ["\nMemory usage: ■■▀▀ (max:   4.00MB)",                                       
                  "sratch.py: % of time = 100.00% out of   0.08s." ,                               
                  "╷       ╷        ╷    ╷       ╷      ╷              ╷       ╷ ",                                                   
                  "Line │Time % │Time %  │Sys │Mem %  │Net   │Memory usage  │Copy   │       ",                                             
                  "│Python │native  │%   │Python │(MB)  │over time / % │(MB/s) │sratch.py ",                                          
                  "╺━━━━━━┿━━━━━━━┿━━━━━━━━┿━━━━┿━━━━━━━┿━━━━━━┿━━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸",
                  "     1 │       │        │    │       │      │              │       │class c:",                               
                  "     2 │       │        │    │       │      │              │       │    def process(y):" ,                             
                  "     3 │       │        │    │       │      │              │       │        for i in range(y):",
                  "     4 │       │        │    │       │      │              │       │            x = i*i",
                  "     5 │   99% │     1% │    │  100% │    4 │■■▀▀100%      │       │            print(x)",
                  "     6 │       │        │    │       │      │              │       │",
                  "     7 │       │        │    │       │      │              │       │a = c()",
                  "     8 │       │        │    │       │      │              │       │c.process(6000)",
                  "       ╵       ╵        ╵    ╵       ╵      ╵              ╵       ╵\n" ]
    input = "\n".join(test_lines)
    p.parseOutput(input)
    res = p.get_results() 

    class_data = ProfileAnalyzer.class_runtime("sratch.py","c",80.0,4.0,100)
    class_data.memory_percentage_of_total = 100.0
    class_data.class_functions.append(0)
    function_data = ProfileAnalyzer.function_runtime("sratch.py","process(y)",80.0,4.0,100)
    function_data.memory_percentage_of_total = 100.0
    assert res["function"][0]==function_data
    assert len(res["function"]) == 1
    assert res["class"][0] == class_data
    assert len(res["class"]) == 1

    # expected_line_by_line = []
    first_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",1,0,0,"class c:",0)
    first_line.memory_percentage_of_total = 0.0
    second_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",2,0,0,"    def process(y):",0)
    second_line.memory_percentage_of_total = 0.0
    third_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",3,0,0,"        for i in range(y):",0)
    third_line.memory_percentage_of_total = 0.0
    fourth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",4,0,0,"            x = i*i",0)
    fourth_line.memory_percentage_of_total = 0.0
    fifth_line =ProfileAnalyzer.line_by_line_runtime("sratch.py",5,80,4,"            print(x)",100)
    fifth_line.memory_percentage_of_total = 100.0
    sixth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",6,0,0,"",0)
    sixth_line.memory_percentage_of_total = 0.0
    seventh_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",7,0,0,"a = c()",0)
    seventh_line.memory_percentage_of_total = 0.0
    eighth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",8,0,0,"c.process(6000)",0)
    eighth_line.memory_percentage_of_total = 0.0
    
    valid = res["line_by_line"][0] == first_line and res["line_by_line"][1] == second_line and res["line_by_line"][2] == third_line and\
        res["line_by_line"][3] == fourth_line and res["line_by_line"][4] == fifth_line and res["line_by_line"][5] == sixth_line and\
        res["line_by_line"][6] == seventh_line and res["line_by_line"][7] == eighth_line
    if not(valid):
        raise Exception()
    p.results = {}    
def testProcessLinesEmptyCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.processLines([])
    assert p.get_results() == {"function":[],"class":[],"line_by_line":[]}

def testProcessLinesBaseCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    test_lines = ["Memory usage: ▀▄ (max:   1.00MB)",                                       
                  "sratch.py: % of time = 100.00% out of   0.09s." ,                               
                  "╷       ╷        ╷    ╷       ╷      ╷              ╷       ╷ ",                                                   
                  "Line │Time % │Time %  │Sys │Mem %  │Net   │Memory usage  │Copy   │       ",                                             
                  "│Python │native  │%   │Python │(MB)  │over time / % │(MB/s) │sratch.py",                                          
                  "╺━━━━━━┿━━━━━━━┿━━━━━━━━┿━━━━┿━━━━━━━┿━━━━━━┿━━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸",
                  "1 │       │        │    │  100% │    1 │▀100%         │       │for i in range(6000):",                               
                  "2 │       │        │    │       │      │              │       │    x = i*i" ,                             
                  "3 │   99% │     1% │    │       │      │              │       │    print(x)",
                  "       ╵       ╵        ╵    ╵       ╵      ╵              ╵       ╵" ]
    p.processLines(test_lines)
    res = p.get_results()
    assert res["function"] == []
    assert res["class"] == []

    # expected_line_by_line = []
    first_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",1,0,1,"for i in range(6000):",0)
    first_line.memory_percentage_of_total = 100.0
    second_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",2,0,0,"    x = i*i",0)
    second_line.memory_percentage_of_total = 0.0
    third_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",3,90.0,0,"    print(x)",100)
    third_line.memory_percentage_of_total = 0.0
    
    complist = ["filename","name","total_run_time","total_memory","memory_percentage_of_total","time_percentage_of_total","line_text"]
    valid = res["line_by_line"][0] == first_line and res["line_by_line"][1] == second_line and res["line_by_line"][2] == third_line
    if not(valid):
        raise Exception()
    p = None 

def testProcessLinesFunctionCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    test_lines = ["Memory usage: ■▀■▀■▀■▀ (max:   2.00MB)",                                       
                  "sratch.py: % of time = 100.00% out of   0.06s." ,                               
                  "╷       ╷        ╷    ╷       ╷      ╷              ╷       ╷ ",                                                   
                  "Line │Time % │Time %  │Sys │Mem %  │Net   │Memory usage  │Copy   │       ",                                             
                  "│Python │native  │%   │Python │(MB)  │over time / % │(MB/s) │sratch.py ",                                          
                  "╺━━━━━━┿━━━━━━━┿━━━━━━━━┿━━━━┿━━━━━━━┿━━━━━━┿━━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸",
                  "     1 │       │        │    │       │      │              │       │def process(y):",                               
                  "     2 │       │        │    │       │      │              │       │    for i in range(y):" ,                             
                  "     3 │       │        │    │  100% │    0 │▄▄            │       │        x = i*i",
                  "     4 │   99% │     1% │    │  100% │    2 │■▀■▀■▀ 80%    │       │        print(x)",
                  "     5 │       │        │    │       │      │              │       │",
                  "     6 │       │        │    │       │      │              │       │process(6000)",
                  "       ╵       ╵        ╵    ╵       ╵      ╵              ╵       ╵\n" ]
    p.processLines(test_lines)
    res = p.get_results() 

    function_data = ProfileAnalyzer.function_runtime("sratch.py","process(y)",60.0,2.0,100)
    function_data.memory_percentage_of_total = 100.0
    assert res["function"][0] == function_data
    assert len(res["function"]) == 1
    assert res["class"] == []

    # expected_line_by_line = []
    first_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",1,0,0,"def process(y):",0)
    first_line.memory_percentage_of_total = 0.0
    second_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",2,0,0,"    for i in range(y):",0)
    second_line.memory_percentage_of_total = 0.0
    third_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",3,0,0,"        x = i*i",0)
    third_line.memory_percentage_of_total = 0.0
    fourth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",4,60,2,"        print(x)",100)
    fourth_line.memory_percentage_of_total = 100.0
    fifth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",5,0,0,"",0)
    fifth_line.memory_percentage_of_total = 0.0
    sixth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",6,0,0,"process(6000)",0)
    sixth_line.memory_percentage_of_total = 0.0
    
    valid = res["line_by_line"][0] == first_line and res["line_by_line"][1] == second_line and res["line_by_line"][2] == third_line and\
        res["line_by_line"][3] == fourth_line and res["line_by_line"][4] == fifth_line and res["line_by_line"][5] == sixth_line
    if not(valid):
        raise Exception()
    p = None 

def testProcessLinesClassCase():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    test_lines = [" Memory usage: ■■▀▀ (max:   4.00MB)",                                       
                  "sratch.py: % of time = 100.00% out of   0.08s." ,                               
                  "╷       ╷        ╷    ╷       ╷      ╷              ╷       ╷ ",                                                   
                  "Line │Time % │Time %  │Sys │Mem %  │Net   │Memory usage  │Copy   │       ",                                             
                  "│Python │native  │%   │Python │(MB)  │over time / % │(MB/s) │sratch.py ",                                          
                  "╺━━━━━━┿━━━━━━━┿━━━━━━━━┿━━━━┿━━━━━━━┿━━━━━━┿━━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸",
                  "     1 │       │        │    │       │      │              │       │class c:",                               
                  "     2 │       │        │    │       │      │              │       │    def process(y):" ,                             
                  "     3 │       │        │    │       │      │              │       │        for i in range(y):",
                  "     4 │       │        │    │       │      │              │       │            x = i*i",
                  "     5 │   99% │     1% │    │  100% │    4 │■■▀▀100%      │       │            print(x)",
                  "     6 │       │        │    │       │      │              │       │",
                  "     7 │       │        │    │       │      │              │       │a = c()",
                  "     8 │       │        │    │       │      │              │       │c.process(6000)",
                  "       ╵       ╵        ╵    ╵       ╵      ╵              ╵       ╵\n" ]
    p.processLines(test_lines)
    res = p.get_results() 

    class_data = ProfileAnalyzer.class_runtime("sratch.py","c",80.0,4.0,100)
    class_data.memory_percentage_of_total = 100.0
    class_data.class_functions.append(0)
    function_data = ProfileAnalyzer.function_runtime("sratch.py","process(y)",80.0,4.0,100)
    function_data.memory_percentage_of_total = 100.0
    assert res["function"][0]==function_data
    assert len(res["function"]) == 1
    assert res["class"][0] == class_data
    assert len(res["class"]) == 1

    # expected_line_by_line = []
    first_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",1,0,0,"class c:",0)
    first_line.memory_percentage_of_total = 0.0
    second_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",2,0,0,"    def process(y):",0)
    second_line.memory_percentage_of_total = 0.0
    third_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",3,0,0,"        for i in range(y):",0)
    third_line.memory_percentage_of_total = 0.0
    fourth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",4,0,0,"            x = i*i",0)
    fourth_line.memory_percentage_of_total = 0.0
    fifth_line =ProfileAnalyzer.line_by_line_runtime("sratch.py",5,80,4,"            print(x)",100)
    fifth_line.memory_percentage_of_total = 100.0
    sixth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",6,0,0,"",0)
    sixth_line.memory_percentage_of_total = 0.0
    seventh_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",7,0,0,"a = c()",0)
    seventh_line.memory_percentage_of_total = 0.0
    eighth_line = ProfileAnalyzer.line_by_line_runtime("sratch.py",8,0,0,"c.process(6000)",0)
    eighth_line.memory_percentage_of_total = 0.0
    
    valid = res["line_by_line"][0] == first_line and res["line_by_line"][1] == second_line and res["line_by_line"][2] == third_line and\
        res["line_by_line"][3] == fourth_line and res["line_by_line"][4] == fifth_line and res["line_by_line"][5] == sixth_line and\
        res["line_by_line"][6] == seventh_line and res["line_by_line"][7] == eighth_line
    if not(valid):
        raise Exception()
    p = None 

def testcomputeMemoryPercentageClass():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    c = ProfileAnalyzer.class_runtime('file/generic','generic',200, 20,0)
    p.computeMemoryPercentageForSection(c,200)
    assert  c.memory_percentage_of_total== 10.0

def testcomputeMemoryPercentageFunc():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    c = ProfileAnalyzer.function_runtime('file/generic','foo',200, 10,0)
    p.computeMemoryPercentageForSection(c,200)
    assert  c.memory_percentage_of_total== 5.0

def testcomputeMemoryPercentageLine():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    c = ProfileAnalyzer.line_by_line_runtime('file/generic','l',200, 10," ",0)
    p.computeMemoryPercentageForSection(c,200)
    assert  c.memory_percentage_of_total== 5.0

def testScaleneArrayStrip():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    arr = ["","Memory usage:","","","","","",'test-data','']
    file_dict = p.ScaleneArrayStrip(arr, "Memory usage:", "% of time", 6)
    assert len(file_dict) == 1
    assert len(file_dict["Memory usage:\n"]) == 1
    assert file_dict["Memory usage:\n"][0] == 'test-data'

def testUpdateRelevantData():
    p = ProfileAnalyzer.ProfileAnalyzer()
    p.results = {"class": [], "function": [], "line_by_line": []}   
    c = ProfileAnalyzer.function_runtime('file/generic','l',200, 10,0)    
    f = ProfileAnalyzer.function_runtime('file/generic','l',200, 10,0)
    l = ProfileAnalyzer.line_by_line_runtime('file/generic','l',0, 0," ",0)

    line_split = ['','','','','','20','']
    p.updateRelevantData(l,f,c,line_split,10.0,28,300)
    assert l.total_run_time == 10.0
    assert l.total_memory == 20.0
    assert l.time_percentage_of_total == 28
    assert l.memory_percentage_of_total == 6.666666666666667

    assert c.total_run_time == 210.0
    assert c.total_memory == 30
    assert c.time_percentage_of_total == 28

    assert f.total_run_time == 210.0
    assert f.total_memory == 30.0
    assert f.time_percentage_of_total == 28.0


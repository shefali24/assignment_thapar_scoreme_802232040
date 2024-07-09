import pytest
from main import longest_path

def test_longest_path():
    graph1 = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph1) == 7

    graph2 = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
    ]
    assert longest_path(graph2) == 6

    graph3 = [
        [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
    ]
    assert longest_path(graph3) == 30

    graph4 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph4) == 3

    print("All test cases pass")

if __name__ == "__main__":
    pytest.main()
'''
output:
C:\Users\HP\anaconda3\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2022.2/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --path C:/Users/HP/assignment/test_main.py -- --last-failed 
Testing started at 16:34 ...
Launching pytest with arguments --last-failed C:/Users/HP/assignment/test_main.py --no-header --no-summary -q in C:\Users\HP\assignment

============================= test session starts =============================
collecting ... collected 1 item
run-last-failure: rerun previous 1 failure

test_main.py::test_longest_path FAILED                                   [100%]
test_main.py:3 (test_longest_path)
2 != 3

Expected :3
Actual   :2
<Click to see difference>

def test_longest_path():
        graph1 = [
            [(1, 3), (2, 2)],
            [(3, 4)],
            [(3, 1)],
            []
        ]
        assert longest_path(graph1) == 7
    
        graph2 = [
            [(1, 2), (2, 1)],
            [(3, 1)],
            [(3, 5)],
            []
        ]
        assert longest_path(graph2) == 6
    
        graph3 = [
            [(1, 10)],
            [(2, 10)],
            [(3, 10)],
            []
        ]
        assert longest_path(graph3) == 30
    
        graph4 = [
            [(1, 1), (2, 1)],
            [(3, 1)],
            [(3, 1)],
            []
        ]
>       assert longest_path(graph4) == 3
E       assert 2 == 3
E        +  where 2 = longest_path([[(1, 1), (2, 1)], [(3, 1)], [(3, 1)], []])

test_main.py:35: AssertionError


============================== 1 failed in 0.07s ==============================

Process finished with exit code 1




'''

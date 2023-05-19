import json
import os
import sys


ROOT_DIR = os.path.join(os.path.dirname(__file__), "../")
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.append(ROOT_DIR)
sys.path.append(SRC_DIR)
from pythondelegate.delegate import Delegate
from typing import Tuple
from pythondelegate.funcs import Func2Arg

def add(a:int, b:int):
    return a + b, f"a + b = {a+b}"
    
func = Func2Arg[str, str, int]([add])
result, process = func.Invoke(2, 8)
print(f"{result}, {process}")
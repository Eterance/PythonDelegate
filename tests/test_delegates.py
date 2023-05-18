import json
import os
import sys
from typing import Tuple


ROOT_DIR = os.path.join(os.path.dirname(__file__), "../")
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.append(ROOT_DIR)
sys.path.append(SRC_DIR)
from pythondelegate.delegate import Delegate
from pythondelegate.actions import Action1Arg, Action2Args
from pythondelegate.funcs import Func1Arg, Func2Arg
from pythondelegate.event_handler import EventHandler
from pythondelegate.event_args import EventArgs

class AAA():
    def aaa(self):
        pass

def aaa():
    print("aaa")

def bbb():
    print("bbb")

def ccc():
    print("ccc")

def ddd():
    print("ddd")


def hhh(a):
    print(f"{a}, go fk yourself")
    
def lol(a):
    print(f"{a}, lol")
    
def win(a):
    print(f"{a}, u cant not win twice!")
    
    
def add(a:int, b:int):
    print(f"{a} + {b} = {a+b}")
    return a, b
    
def minus(a:int, b:int): 
    print(f"{a} - {b} = {a-b}")
    return a, b

def multi(a:int, b:int):  
    print(f"{a} * {b} = {a*b}")
    return a, b

def div(a:int, b:int):
    print(f"{a} / {b} = {a/b}")
    return a, b

def hello(a:str):
    print(a)
    return a

def main():    
    """action = Action2Args[int, int]()
    action = Action2Args[int, int]([add])
    action += Action2Args[int, int]([minus])
    action += multi
    action(50, 20)
    print(f"action.count = {action.count}")
    print(f"Is minus in action? {minus in action}")
    action = action - minus
    action -= Action2Args[int, int]([multi])
    action2 = Action2Args[int, int]([div])
    action = Action2Args.Combine([action, action2, add])
    action(60, 2)
    print(f"action.count = {action.count}")
    print(f"Is minus in action? {minus in action}")"""
    
    
    print("-----")
    func = Func2Arg[int, int, Tuple[int, int]]()
    func = Func2Arg[int, int, Tuple[int, int]]([add])
    func += Func2Arg[int, int, Tuple[int, int]]([minus])
    func += multi
    res1, res2 = func(50, 70)
    print(func(50, 70))
    print(f"action.count = {func.count}")
    print(f"Is minus in action? {minus in func}")
    func = func - minus
    func -= Func2Arg([multi])
    action2 = Func2Arg[int, int, Tuple[int, int]]([div])
    func = Func2Arg[int, int, Tuple[int, int]].Combine([func, action2, add])
    func.Invoke()
    print(func(50, 700))
    print(f"action.count = {func.count}")
    print(f"Is minus in action? {minus in func}")
    
    
if __name__ == "__main__":
    main()
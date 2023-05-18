# Action 类

封装具有参数（也可以没有）但是不具有返回值的方法。

## 示例

以下示例使用 `Action2Arg[T1, T2]` 类，该类可封装了具有两个泛型参数的方法。

```python
from pythondelegate.actions import Action2Args

def aaa(a:str, times:int):
    total = ", ".join([a for _ in range(times)])
    print(f"aaa: {total}")
    
action = Action2Args[str, int]([aaa])
action("111", 3) # aaa: 111, 111, 111
```

## 不同数量的泛型参数

如果要封装的方法不具有参数，可以使用 `Action` 类。

如果要封装的方法具有多个，可以使用 `ActionNArg[T1, T2, .. , TN]` 类，其中 `N` 为参数的数量。比如，要封装具有 3 个参数的方法，可以使用 `Action3Arg[T1, T2, T3]` 类。

## 另请参阅

- [Delegate 类](Delegate.md)

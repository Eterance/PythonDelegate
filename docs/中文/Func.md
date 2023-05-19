# Func 类

封装具有参数（也可以没有）以及具有返回值的方法。

## 示例

以下示例使用 `Func2Arg[T1, T2, TRESULT]` 类，该类可封装了具有两个泛型参数和一个泛型返回值的方法。

```python

from typing import Tuple
from pythondelegate.funcs import Func2Arg

def add(a:int, b:int):
    return a + b, f"a + b = {a+b}"
    
func = Func2Arg[int, int, Tuple[int, str]]([add])
result, process = func(2, 8)
```

## 不同数量的泛型参数

如果要封装的方法不具有参数，可以使用 `Func` 类。

如果要封装的方法具有多个，可以使用 `FuncNArg[T1, T2, .. , TN, TRESULT]` 类，其中 `N` 为参数的数量，`TRESULT` 代表返回值类型。比如，要封装具有 3 个参数和一个返回值的方法，可以使用 `Func3Arg[T1, T2, T3, TRESULT]` 类。

## 另请参阅

- [Delegate 类](Delegate.md)

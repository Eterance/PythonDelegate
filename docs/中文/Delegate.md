# Delegate 类

## 定义

委托的基类。

## 示例

下面的示例演示了如何声明一个 `Delegate` 类的实例对象，在初始化阶段就向该委托对象传递了函数 `aaa`。然后，调用该委托对象。委托对象会调用函数 `aaa`。

```python
from pythondelegate.delegate import Delegate

def aaa():
    print("aaa")

delegate = Delegate([aaa])
delegate() # should print aaa
```

> 注意：  
>
> `Delegate` 类并没有为输入参数和返回值提供泛型注释。因此，建议只将`Delegate` 类用于无输入参数也无返回值的方法。  
>
> 若要将委托应用于具有输入参数或返回值的方法，请使用 [Action](docs/中文/Action.md) 或 [Func](docs/中文/Func.md) 类，或者继承 `Delegate` 类并自行实现泛型注释。

## 向委托添加/删除方法

除了在委托实例初始化时向构造函数传递方法列表之外，还可以使用自增运算符向委托添加方法。

```python
def aaa():
    print("aaa")

def bbb():
    print("bbb")

delegate = Delegate([aaa])
delegate += bbb # add bbb to delegate
```

自增运算符的左侧要可调用（Callable）的对象。当然，委托本身也是可调用的，因此也可以将一个委托添加到另一个委托中（**只能添加同一类型的委托**）。

```python
delegate_aaa = Delegate([aaa])
delegate_bbb = Delegate([bbb])
delegate_aaa += delegate_bbb # add delegate_bbb to delegate_aaa
```

要注意的是，向委托中添加/删除方法并不会修改当前的委托对象，而是会返回一个新的委托对象。

使用自减运算符即可从委托中删除方法。

```python
delegate = Delegate([aaa, bbb])
delegate -= aaa # remove aaa from delegate
```

## 委托的调用

因为委托是可调用（Callable）的对象，因此可以像调用方法一样调用委托。

```python
delegate = Delegate([aaa])
delegate() # equal to aaa()
```

`Invoke` 方法也会起到一样的作用。

```python
delegate() # equal to aaa()
delegate.Invoke() # equal to aaa()
```

## 委托的运算

委托可以使用 `+` 运算符进行合并，使用 `-` 运算符向委托中删除方法。

```python
def aaa():
    print("aaa")

def bbb():
    print("bbb")

delegate = Delegate([bbb])
delegate_bbb = Delegate([bbb])
delegate = delegate + aaa
delegate = delegate - delegate_bbb
```

此时，delegate 的调用列表中只包含 aaa 方法。

> 注意：
>
> 委托加减运算时，运算符左侧**只能是委托**，右侧是可调用对象（包括同类型委托）。

## 委托签名

与 C# 中的方法签名需要与[委托](https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/delegates/)签名相同（或者使用[委托变体](https://learn.microsoft.com/zh-cn/dotnet/csharp/programming-guide/concepts/covariance-contravariance/using-variance-in-delegates)）这一规定不同，当使用泛型 [Action](Action.md) 或者 [Func](Func.md) 委托，或者自定义委托时，委托签名（也就是输入参数和返回值的类型）并不是，也做不到强制与方法签名相同。实际上，委托签名只是提供了类型注释的能力。

比如，以下代码完全是可执行的：

```python
from pythondelegate.funcs import Func2Arg

def add(a:int, b:int):
    return a + b, f"a + b = {a+b}"
    
func = Func2Arg[str, str, int]([add])
result, process = func.Invoke(2, 8)
```

虽然正确的委托签名应该是 `Func2Arg[int, int, Tuple[int, str]]`，但是代码仍可以执行，结果也正确。不过不建议这么做，因为这使委托失去了提供正确类型注解的能力。

## 另请参阅

- [Action 类](Action.md)
- [Func 类](Func.md)

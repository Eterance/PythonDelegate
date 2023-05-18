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

## 另请参阅

- [Action 类](Action.md)
- [Func 类](Func.md)

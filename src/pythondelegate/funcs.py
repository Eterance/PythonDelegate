from typing import Callable, Generic, TypeVar
from pythondelegate.delegate import Delegate


T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
T5 = TypeVar('T5')
T6 = TypeVar('T6')
T7 = TypeVar('T7')
T8 = TypeVar('T8')
T9 = TypeVar('T9')
T10 = TypeVar('T10')
T11 = TypeVar('T11')
T12 = TypeVar('T12')
T13 = TypeVar('T13')
T14 = TypeVar('T14')
T15 = TypeVar('T15')
T16 = TypeVar('T16')
TRESULT = TypeVar('TRESULT')



class Func(Delegate, Generic[TRESULT]):
    """
    Represents a list of methods that have no parameter and return a TRESULT type value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Func[TRESULT]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Func[TRESULT]', callable_list: list[Callable])->'Func[TRESULT]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Func[TRESULT]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Func[TRESULT]':
        return super().__sub__(item)
    
    # Override
    def __call__(self):        
        return self.Invoke()
    
    # Override
    def Invoke(self)->TRESULT:
        """
        Return the result of the last invoked method.
        """
        for function in self._functions:
            result = function()
        return result
    
class Func1Arg(Delegate, Generic[T1, TRESULT]):
    """
    Represents a list of methods that have 1 parameter and return a TRESULT type value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Func1Arg[T1, TRESULT]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Func1Arg[T1, TRESULT]', callable_list: list[Callable])->'Func1Arg[T1, TRESULT]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Func1Arg[T1, TRESULT]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Func1Arg[T1, TRESULT]':
        return super().__sub__(item)
    
    # Override
    def __call__(self, arg1:T1):        
        return self.Invoke(arg1)
    
    # Override
    def Invoke(self, arg1:T1)->TRESULT:
        """
        Return the result of the last invoked method.
        """
        for function in self._functions:
            result = function(arg1)
        return result

class Func2Arg(Delegate, Generic[T1, T2, TRESULT]):
    """
    Represents a list of methods that have 2 parameter and return a TRESULT type value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Func2Arg[T1, T2, TRESULT]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Func2Arg[T1, T2, TRESULT]', callable_list: list[Callable])->'Func2Arg[T1, T2, TRESULT]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Func2Arg[T1, T2, TRESULT]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Func2Arg[T1, T2, TRESULT]':
        return super().__sub__(item)
    
    # Override
    def __call__(self, arg1:T1, arg2:T2):        
        return self.Invoke(arg1, arg2)
    
    # Override
    def Invoke(self, arg1:T1, arg2:T2)->TRESULT:
        """
        Return the result of the last invoked method.
        """
        for function in self._functions:
            result = function(arg1, arg2)
        return result

class Func3Arg(Delegate, Generic[T1, T2, T3, TRESULT]):
    """
    Represents a list of methods that have 3 parameters and return a TRESULT type value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Func3Arg[T1, T2, T3, TRESULT]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Func3Arg[T1, T2, T3, TRESULT]', callable_list: list[Callable])->'Func3Arg[T1, T2, T3, TRESULT]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Func3Arg[T1, T2, T3, TRESULT]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Func3Arg[T1, T2, T3, TRESULT]':
        return super().__sub__(item)
    
    # Override
    def __call__(self, arg1: T1, arg2: T2, arg3: T3):
        return self.Invoke(arg1, arg2, arg3)
    
    # Override
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3) -> TRESULT:
        """
        Return the result of the last invoked method.
        """
        result = None
        for function in self._functions:
            result = function(arg1, arg2, arg3)
        return result

class Func4Arg(Delegate, Generic[T1, T2, T3, T4, TRESULT]):
    """
    Represents a list of methods that have 4 parameters and return a TRESULT type value.
    """

    # Override
    @classmethod
    def Combine(cls, callable_list: list[Callable]) -> 'Func4Arg[T1, T2, T3, T4, TRESULT]':
        return super().Combine(callable_list)

    # Override
    @classmethod
    def Remove(cls, delegate: 'Func4Arg[T1, T2, T3, T4, TRESULT]', callable_list: list[Callable]) -> 'Func4Arg[T1, T2, T3, T4, TRESULT]':
        return super().Remove(delegate, callable_list)

    # Override
    def __add__(self, item: Callable) -> 'Func4Arg[T1, T2, T3, T4, TRESULT]':
        return super().__add__(item)

    # Override
    def __sub__(self, item: Callable) -> 'Func4Arg[T1, T2, T3, T4, TRESULT]':
        return super().__sub__(item)

    # Override
    def __call__(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4) -> TRESULT:
        return self.Invoke(arg1, arg2, arg3, arg4)

    # Override
    def Invoke(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4) -> TRESULT:
        """
        Return the result of the last invoked method.
        """
        result = None
        for function in self._functions:
            result = function(arg1, arg2, arg3, arg4)
        return result

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

class Action(Delegate):
    """
    Represents a list of methods that have no parameter and do not return value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Action':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Action', callable_list: list[Callable])->'Action':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Action':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Action':
        return super().__sub__(item)
    
    # Override
    def __call__(self):        
        self.Invoke()
    
    # Override
    def Invoke(self):
        super().Invoke()
        
class Action1Arg(Delegate, Generic[T1]):
    """
    Represents a list of methods that have 1 parameter and do not return value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Action1Arg[T1]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Action1Arg[T1]', callable_list: list[Callable])->'Action1Arg[T1]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Action1Arg[T1]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Action1Arg[T1]':
        return super().__sub__(item)
    
    # Override
    def __call__(self, arg1:T1):        
        self.Invoke(arg1)
    
    # Override
    def Invoke(self, arg1:T1):
        super().Invoke(arg1)

class Action2Args(Delegate, Generic[T1, T2]):
    """
    Represents a list of methods that have 2 parameters and do not return value.
    """
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'Action2Args[T1, T2]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'Action2Args[T1, T2]', callable_list: list[Callable])->'Action2Args[T1, T2]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'Action2Args[T1, T2]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'Action2Args[T1, T2]':
        return super().__sub__(item)
    
    # Override
    def __call__(self, arg1:T1, arg2:T2):        
        self.Invoke(arg1, arg2)
    
    # Override
    def Invoke(self, arg1:T1, arg2:T2):
        super().Invoke(arg1, arg2)

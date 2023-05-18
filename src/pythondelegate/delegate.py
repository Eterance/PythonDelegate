from functools import singledispatchmethod
from typing import Optional, Union
import inspect
from types import FunctionType, MethodType
from typing import Any, Callable, Final, List, NoReturn, TypeVar, Generic, final


class Delegate():
    """
    Base class for delegates. Represents a list of methods that have no parameter and do not return a value.\n
    Although the delegate class can be passed parameters, it is not recommended to do so, as the type hint will be lost.\n
    The 'delegate' here is a little different from the delegate in C# (or maybe it's a lot different).\n
    Nested delegates are not allowed (delegate objects can't be add to delegate._functions).\n
    """
    def __init__(self, callable_list:Optional[list[Callable]]=None, is_allow_duplicate_method:bool=True):
        """
        Initialize the delegate.

        Args:
            callable_list (list[Callable], optional): 
            is_allow_duplicate_method (bool, optional): Whether to allow add duplicate methods. Defaults to True.
        """
        self._functions: list[Callable] = []
        if callable_list is not None:
            self._functions = self.__class__.Combine(callable_list).get_invocation_list()
        # Currently, this is not used.
        self._is_allow_duplicate_method: Final = is_allow_duplicate_method
    
    @classmethod
    def Combine(cls, callable_list:list[Callable])->'Delegate':
        """
        Combine multiple callable object in 'callable_list' into one new delegate.\n
        If one of the items in the list is delegate, its methods will be added to the new delegate.\n
        Only delegates of the same type can be combined.\n
        Will not modify the original delegate.

        Args:
            callable_list (list[Callable]): A list of callable objects or delegates.

        Returns:
            Delegate
        """
        result = cls()
        for item in callable_list:
            if callable(item):
                if isinstance(item, Delegate):
                    if type(item) is cls:
                        result._functions.extend(item._functions)
                    else:
                        raise TypeError(f"The delegate in 'callable_list' must be type '{str(cls)}', but got '{str(type(item))}'.")
                else:
                    result._functions.append(item)
            else:
                raise TypeError(f"The item in 'callable_list' must be of type 'Callable'.")
        return result
    
    
    @classmethod
    def Remove(cls, delegate:'Delegate', callable_list:list[Callable]):
        """
        Remove the methods in 'callable_list' from the delegate, and return the new delegate.\n
        If one of the items in the list is delegate, its methods will be removed from the delegate.\n
        Only delegates of the same type can be removed.\n
        Will not modify the original delegate.

        Args:
            delegate (Delegate): The delegate to be manipulated.
            callable_list (list[Callable]): A list of callable objects or delegates.

        Raises:
            TypeError: _description_
            TypeError: _description_

        Returns:
            Delegate
        """
        result = cls.Combine([delegate])
        for item in callable_list:
            if callable(item):
                if isinstance(item, Delegate):
                    if type(item) is cls:
                        for item2 in item._functions:
                            result.remove_method(item2)
                    else:
                        raise TypeError(f"The delegate in 'callable_list' must be type '{str(cls)}', but got '{str(type(item))}'.")
                else:
                    result.remove_method(item)
            else:
                raise TypeError(f"The item in 'callable_list' must be of type 'Callable'.")
        return result
    
    def remove_method(self, function:Callable):
        """
        Remove the method from the delegate.

        Args:
            function (Callable): 
        """
        if function in self._functions:
            self._functions.remove(function)
        
    def __add__(self, item:Callable):
        result = self.__class__.Combine(callable_list=[self, item])
        return result

    def __sub__(self, item:Callable):
        result = self.__class__.Remove(delegate=self, callable_list=[item])
        return result
    
    """def __iadd__(self, item:Union[MethodType, FunctionType, 'Delegate']):
        if inspect.ismethod(item) or inspect.isfunction(item):
            if item not in self._functions or self._is_allow_duplicate_method:
                self.add(item)
        elif type(item) is type(self):
            self.combine(item)
        else:
            raise TypeError("The item must be of type method/function or " + str(type(self)))
        return self"""
    
    """def __isub__(self, item:Union[MethodType, FunctionType]):
        if (inspect.ismethod(item) or inspect.isfunction(item)):
            self.remove(item)
        else:
            raise TypeError("The item must be of type method/function.")
        return self"""
    
    def __call__(self, *args, **kwargs):        
        return self.Invoke(*args, **kwargs)
    
    def Invoke(self, *args, **kwargs):        
        for function in self._functions:
            function(*args, **kwargs)
            
    @final
    def __len__(self):
        return len(self._functions)
    
    @final
    def __contains__(self, item:Callable):
        return item in self._functions
    
    @property
    @final
    def count(self)->int:
        """
        The number of methods in the delegate.
        """
        return len(self)
    
    @final
    def get_invocation_list(self) -> 'list[Callable[[], None]]':
        """
        Returns the invocation list of the delegate.

        Returns:
            list[Callable[[], None]]: a list of methods.
        """
        result: list[Callable] = []
        for item in self._functions:
            result.append(item)
        return result

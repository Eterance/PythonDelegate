import inspect
from typing import Callable, Generic, TypeVar

from pythondelegate.actions import Action2Args

SENDER_TYPE = TypeVar('SENDER_TYPE')
EVENTARGS_TYPE = TypeVar('EVENTARGS_TYPE')

class EventHandler(Action2Args, Generic[EVENTARGS_TYPE]):
    # Override
    @classmethod
    def Combine(cls, callable_list: 'list[Callable]')->'EventHandler[EVENTARGS_TYPE]':
        return super().Combine(callable_list)
    
    # Override
    @classmethod
    def Remove(cls, delegate: 'EventHandler[SENDER_TYPE, EVENTARGS_TYPE]', callable_list: 'list[Callable]')->'EventHandler[EVENTARGS_TYPE]':
        return super().Remove(delegate, callable_list)
    
    # Override
    def __add__(self, item: Callable)->'EventHandler[EVENTARGS_TYPE]':
        return super().__add__(item)
    
    # Override
    def __sub__(self, item: Callable)->'EventHandler[EVENTARGS_TYPE]':
        return super().__sub__(item)
    
    # Override
    def __call__(self, sender, e:EVENTARGS_TYPE):        
        self.Invoke(sender, e)
    
    # Override
    def Invoke(self, sender, e:EVENTARGS_TYPE):        
        super().Invoke(sender, e)

#0

def verbose(function):
    
    def wrapper(*args, **kwargs):
        print("before function call")
        outcome = function(*args, **kwargs)
        print("after function call")
        return outcome
    
    return wrapper

@verbose
def hello(name: str):
    print(f"*** Hello {name}! ***")

hello("Nikolay")


#1.2
print('------')

def repeater(count):
    def my_decorator(func):
        def wrapped(function_arg1, function_arg2):
            for i in range(count):
                func(function_arg1, function_arg2)
            return
        return wrapped
    return my_decorator

@repeater(count=4)
def my_fancy_function(arg_1, arg_2):
    print(arg_1+' '+arg_2)

my_fancy_function('nick','fedorov')


#1.3
print('------')

from contextlib import ContextDecorator

class verbose_context(ContextDecorator):
    def __enter__(self):
        print('class: before function call')
        return self

    def __exit__(self, *exc):
        print('class: after function call')
        return False

@verbose_context()
def hello(name: str):
    print(f"*** Hello {name}! ***")

hello('Nikolay')


#1.4
print('------')

class Indenter:
    def __init__(self):
        self.indent_str = "--"
        self.indent_level = 0

    def print(self, word):
        print(self.indent_str*self.indent_level + word)
        self.indent_level += 1

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

with Indenter() as indent:
    #from pdb import set_trace; set_trace()
    indent.print("hello")
    indent.print("hi")
    indent.print("holla")

'''
with Indenter() as indent:
    indent.print("hi")
    with indent:
        indent.print("hello")
        with indent:
            indent.print("bonjour")
    indent.print("hey")

'''

#indent_str="--", indent_level=1 
#indent_str="--" 
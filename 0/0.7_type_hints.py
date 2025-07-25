"""
Python is not a "strongly typed" language, that means that you can make any variable be any type and you don't have to think about it
that is nice when you are wanting to do something quickly, but when you have more complicated projects it can become a
bit confusing to work out what each thing is.

In many languages, you are required to state the type of a variable when you create it, and you can never change it.
In python the closest you can get to that is via type hints, they don't put any actual requirement on you, and you can
ignore them entirely, but mistakes in how you use them will be highlighted, either by the IDE (pycharm) or by a program
called mypy
"""

not_an_int: int = 1.223
not_a_str: str = None
a_str: str = "blah"
an_int = 100

# You can define that a variable is any of a set of types by making the type hint a "Union"
from typing import Union
a_str_or_an_int: Union[str, int] = "hello"
a_str_or_an_int = 100
a_str_or_an_int = 100.5

# You can define that a variable could be none by using "Optional"
from typing import Optional
nullable_int: Optional[int] = None
nullable_int = 12

# lists, sets, dictionary etc type hints have to be imported
from typing import Dict, List, Set, Tuple


# You can type hint functions as well, and it will highlight if you return something of the wrong type
def do_something(arg1: int, arg2: float) -> str:
    if arg1 + arg2 > 0:
        return "Hello"
    return 10

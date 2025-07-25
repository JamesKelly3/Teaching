"""
There are loads of programming languages: e.g.
Python
Java
C/C++
Rust
MatLab
Haskell
SQL
Javascript

There are a few key distinctions between languages that make them distinct from each other.

Static/Dynamic Typed languages:

In statically typed languages when you make a variable, that variable is forever locked to be a single type, e.g.
`int x = 5`. If you ever tried to do e.g. x = "blah" you would get an error. In dynamically typed languages you can change
what a variable is as many times as you want - this can be useful, but can also make it difficult to keep track of
what type a variable is, and can make mistakes easier.
C++, Java, Rust are all statically typed languages, Python is an example of a dynamically typed language.

Interpreted vs Compiled Languages:

When you run a program, the computer must take the code you have written and convert it into machine code - that is,
some kind of code that the computer can understand. Machine code is very annoying to write, so historically people came
with the idea to make languages which are easy to write, and created programs which convert those languages into
machine code.

The programs which convert the code are called compilers and interpreters.
Interpreters:
read the code one line at a time, while it is running and execute it, so every time you want to do something, the computer
first has to convert it to machine code
Compilers:
before the code is running, looks over all of the code and generates machine code for the entire program, this generally
makes code which runs faster, because a) you don't need to do the conversion while the program is running and
b) the compiler can look over all of the code and make optimisations.
C++, Java, Rust, are compiled, Python, Javascript, MatLab are generally used as interpreted languages (though they _can_ be compiled)

Object-oriented vs functional programming
object oriented programming uses classes and objects to model the world, e.g. you might create a class `Person`, and then
create many instances (objects) of that type to represent a group of people.
functional programming uses functions to transform data, it basically models the world by allowing you define how to
move from one state to another
Of the languages mentioned above, only Haskell is really a functional language.

We will mostly use Python to get started, it is quite widely used, and is fairly easy to get going with
That being said every language has benefits and drawbacks, and different languages suit different use cases better
"""
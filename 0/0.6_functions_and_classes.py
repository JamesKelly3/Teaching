"""
functions are a way of defining a bit of logic which you don't want to have to write multiple times, they take arguments
and can return a result (but aren't required to have either)

classes are a slightly more advanced type than the others we have touched on. They allow you to define how every part of your type works,
for example you could define a class which represents a person, and includes information about them, and also allows you to interact with
them in some way
"""

def add_some_numbers(number1, number2, number3):
    result = number1 + number2 + number3
    return result

print(add_some_numbers(10, 11, 12))

class Person:
    # This is __init__ also called the "constructor", it defines how to create a specific instance of the class,
    # and takes in any required data as arguments, in this case name, age and height are arguments
    # self is a special argument for functions which are within classes, and allows you to access attributes of the
    # instance
    def __init__(self, name, age, height):
        # note that "self.name" is different to "name", "name" is the argument to the function, and only exists within the function
        # "self.name" is an attribute of the class, and can be accessed within any function in the class
        self.name = name
        self.age = age
        self.height = height

    # This is a custom function for a person
    def get_older(self):
        self.age = self.age + 1

terry = Person("Terry", 28, 181)
print(terry.name, terry.age, terry.height)
terry.get_older()
print(terry.age)

# You can make another person, without affecting the existing one
esmerelda = Person("Esmerelda", 48, 162)
print(esmerelda.name, terry.name)
"""
Below is a class defining a Person
Given a list of people, print the name of the tallest, and the name of the oldest person
"""


class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

people = [Person("Bob", 22, 172), Person("Alice", 12, 147), Person("Henry", 90, 173), Person("Miranda", 71, 163)]
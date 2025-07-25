"""
Using that same definition of person from question 4, and given a list of people find all of the people taller than 150cm and younger than 25
"""
class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

people = [Person("Bob", 22, 172), Person("Alice", 12, 147), Person("Henry", 60, 183), Person("Miranda", 71, 163)]
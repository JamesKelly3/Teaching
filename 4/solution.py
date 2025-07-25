class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

people = [Person("Bob", 22, 172), Person("Alice", 12, 147), Person("Henry", 60, 183), Person("Miranda", 71, 163)]

# Remember the tallest and the oldest seen so far, before we start we haven't seen anyone
tallest_name, tallest_height = "", 0
oldest_name, oldest_age = "", 0
for person in people:
    if person.height > tallest_height:
        tallest_name = person.name
        tallest_height = person.height
    if person.age > oldest_age:
        oldest_name = person.name
        oldest_age = person.age
print("Tallest:", tallest_name, tallest_height)
print("Oldest:", oldest_name, oldest_age)

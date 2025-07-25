class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

people = [Person("Bob", 22, 172), Person("Alice", 12, 147), Person("Henry", 60, 183), Person("Miranda", 71, 163)]

people_meeting_criteria = []
for person in people:
    if person.age < 25 and person.height > 150:
        people_meeting_criteria.append(person.name)
print(people_meeting_criteria)
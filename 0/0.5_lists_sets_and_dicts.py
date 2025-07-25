"""
tuples, lists, sets and dictionaries are some of the ways you can store multiple things
tuples are "immutable", that means once you have made them, you cannot change them, lists, sets and dictionaries can be changed all you want
"""

example_tuple = (1, 2, 3, 4)
example_list = [4, 5, 6]
example_set = {7, 8, 9}
example_dict = {"hi": 50, "there": 100}

# you can access specific elements in tuples and lists:
# the elements start counting from 0, so the first element in a list is list[0]
print(example_tuple[2])
print(example_list[1])

# you can add new items on the end of a list
example_list.append(10)
print(example_list)
# you can join 2 lists together
print(example_list + [100, 110])

# you can add new items to a set, and it will not add any that are already there
example_set.add(7)
example_set.add(42)
print(example_set)

# you can access items in a dictionary using their key:
print(example_dict["hi"])
# you can add new items into a dictionary using a new key:
example_dict["bye"] = 120
print(example_dict)
# you can override the existing mapping by using a key that's already in the dictionary
example_dict["hi"] = 20000
print(example_dict)

### Loops and iterators

# most languages have some concept of "loops", the most common are "for" and "while" loops

# In python you can think of a for loop as:
# for X in Y do something
# So for every element X within a larger set Y you do something
# This could be as simple as just doing something a set number of times, e.g.

for i in range(10):
    print("Counting", i)

# You can iterate over all of the things in a list (or sets, or tuples):
for item in example_list:
    print("Thing in list:", item)

# you can also do this for dictionaries, and you can choose to look at the keys, the values or both:
for key in example_dict.keys():
    print("KEY", key)
for value in example_dict.values():
    print("VALUE", value)
for key, value in example_dict.items():
    print("BOTH", key, value)

# You can generate lists between two numbers using "range"
print(list(range(10))) # lower bound defaults to 0 if you don't add it
print(list(range(5, 10)))

# with while loops you can think of them as
# while X is True do something - an example could be something like "while time is before 10pm do something"
# an example:
x = 20

while x > 1:
    print("halving x", x)
    x = x / 2

# You would generally use a for loop when you know how many times or how many things you want to do something for
# You would use a while loop when you don't know at the start how many times you will loop
"""
Make the code below more efficient, simple as that!
"""
import time
import random

# ignore this bit, this is just to get some data to use
random.seed(10)
test = [random.randint(0, 30) for i in range(50000)]

def do_something():
    """
    A function which counts how many times each number occurs, only if it exists more than once
    """
    duplicates = set()
    count_of_duplicates = {}
    for i in test:
        for j in test:
            if i == j:
                duplicates.add(i)
    for dupe in duplicates:
        count = 0
        for i in test:
            if i == dupe:
                count += 1
        count_of_duplicates[dupe] = count
    return count_of_duplicates

def efficient_do_something():
    pass

now = time.time()
d = do_something()
print(f"It took {time.time() - now} seconds to run this code")

now = time.time()
e = efficient_do_something()
print(f"It took {time.time() - now} seconds to run this code")

assert d == e
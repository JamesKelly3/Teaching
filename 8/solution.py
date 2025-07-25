"""
Make the code below more efficient, simple as that!
"""
import time
import random

random.seed(10)
test = [random.randint(0, 30) for _ in range(50000)]

def do_something():
    """
    A function which counts how many times each number occurs, only if it is duplicated
    """
    duplicates = set()
    count_of_duplicates = {}
    # this is bad, we look at everything in the list once for everything in the list
    # meaning we look at n^2 things (where n is the length of the list)
    for i in test:
        for j in test:
            if i == j:
                duplicates.add(i)
    # we are doing n comparisons here for every duplicated value
    for dupe in duplicates:
        count = 0
        for i in test:
            if i == dupe:
                count += 1
        count_of_duplicates[dupe] = count
    return count_of_duplicates

def efficient_do_something():
    counts = {}
    # only look at each thing once
    for i in test:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    # we are doing 1 comparison here for every duplicated value
    count_of_duplicates = {dupe: count for (dupe, count) in counts.items() if count > 1}
    return count_of_duplicates


now = time.time()
d = do_something()
print(f"It took {time.time() - now} seconds to run this code")

now = time.time()
e = efficient_do_something()
print(f"It took {time.time() - now} seconds to run this code")

assert d == e

# I wrote code to count roughly how many comparisons each function did, the original does 2501550000
# and the efficient one does 50031

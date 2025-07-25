"""
Trees:
Trees are a set of nodes and branches e.g.:

      a
   /     \
   b     c
  / \   / \
e    f g   h

They are a useful way of storing data.

A binary search tree (BST) is defined where for every node, every node x in the left branch of x is smaller (or equal) than x
and every node in the right branch of x is larger than x

BST's are useful for searching for items in a data set because you only need to compare to one node at each level of the tree
to find the object, meaning you only do log(n) comparisons, whereas iterating over a list linearly would do n comparisons

Complete the class "Node" which has fields "key", "value", "left_subnode" and "right_subnode" and functions "insert_node" and "locate_node"
"key" is the comparison value, and "value" is an arbitrary piece of data
"insert_node" edits the tree to include the new key, value
"locate_node" searches the tree and returns the "value" given a key
"""
import time
# ignore this bit, this is just to get some data to use
import random
random.seed(10)
test = {random.randint(0, 500000000) for i in range(5000000)}
test_values = [random.randint(0, 500000) for i in range(len(test))]

test_data = list(zip(test, test_values))


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # When you create a node, it is a leaf - meaning it has no subnodes
        self.left_subnode = None
        self.right_subnode = None

    def insert(self, key, value):
        if key <= self.key:
            if self.left_subnode is None:
                self.left_subnode = Node(key, value)
            else:
                self.left_subnode.insert(key, value)
        else:
            if self.right_subnode is None:
                self.right_subnode = Node(key, value)
            else:
                self.right_subnode.insert(key, value)

    def locate_node(self, key):
        if key == self.key:
            return self.value
        elif key <= self.key and self.left_subnode is not None:
            return self.left_subnode.locate_node(key)
        elif key > self.key and self.right_subnode is not None:
            return self.right_subnode.locate_node(key)
        else:
            return None

now = time.time()
root = Node(test_data[0][0], test_data[0][1])
for t, v in test_data[1:]:
    root.insert(t, v)
print(f"inserting took {time.time() - now} seconds")

now = time.time()
value = root.locate_node(452482379)
assert value == 405888
print(f"finding took {time.time() - now} seconds with tree")
now = time.time()
value = [v for t, v in test_data if t == 452482379]
assert value[0] == 405888
print(f"finding took {time.time() - now} seconds with linear search")


# Notice that inserting is not particularly fast!
# The main benefit of a BST is that it maintains ordering, so searching it is always cheap, so it's mostly useful if you're going to
# do a lot of lookups

# inserting a single new item takes log(n) comparisons, searching takes log(n), building a tree from scratch is nlog(n)
# searching an unsorted list for a single item takes n comparisons.
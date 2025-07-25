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

# ignore this bit, this is just to get some data to use
import random
random.seed(10)
test = [random.randint(0, 5000) for i in range(500)]
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
        pass
    def locate_node(self, key):
        pass


# Some code to check you solved the problem

root = Node(test_data[0][0], test_data[0][1])
for t, v in test_data[1:]:
    root.insert(t, v)

# this is the example node
assert root.locate_node(3780) == 377159
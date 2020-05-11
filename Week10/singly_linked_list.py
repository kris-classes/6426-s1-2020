"""
Singly Linked List

https://en.wikipedia.org/wiki/Linked_list

Use Python's built-in lists instead of these.
This is just an academic exercise to demonstrate theory behind linked lists.

ISCG 6426 Data Structures & Algorithms S1 2020
Kris Pritchard / @krisrp
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeA.next_node = nodeB
nodeB.next_node = nodeC


def traverse(node):
    print('Singly Linked List Traversal')
    current_node = node
    # https://docs.python.org/3/library/stdtypes.html#truth-value-testing
    while current_node is not None:  # You can also just use 'while node'
        print(current_node)
        current_node = current_node.next_node

    print('End of list')


traverse(nodeA)

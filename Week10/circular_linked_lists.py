"""
Circular Linked List

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
nodeC.next_node = nodeA


"""
Naively traversing will loop forever.
"""

"""
Max depth
"""


def traverse_maxvisits(node, max_visits=10):
    print('Circular Linked List Counter Traversal')
    current_node = node
    num_visits = 0
    # https://docs.python.org/3/library/stdtypes.html#truth-value-testing
    while current_node is not None and num_visits <= max_visits:  # You can also just use 'while node'
        print(f'{num_visits} - {current_node}')
        current_node = current_node.next_node
        num_visits += 1

    print('Max visits reached')


traverse_maxvisits(nodeA)


"""
Use a set to keep track of visited nodes
"""


def traverse_set(node):
    print('Circular Linked List Set Traversal')
    current_node = node
    visited = set()
    # https://docs.python.org/3/library/stdtypes.html#truth-value-testing
    while current_node is not None and current_node not in visited:  # You can also just use 'while node'
        print(f'{current_node}')
        visited.add(current_node)
        current_node = current_node.next_node

    print('Visited all the nodes')


traverse_set(nodeA)

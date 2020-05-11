"""
Breadth-First Search

https://en.wikipedia.org/wiki/Breadth-first_search

This is just a simple academic example to help with understanding.

ISCG 6426 Data Structures & Algorithms S1 2020
Kris Pritchard / @krisrp
"""


class Node:
    """
    Based on https://en.wikipedia.org/wiki/Node_(computer_science)
    """
    def __init__(self, data, nodes=None):
        self.data = data
        self.nodes = nodes

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node('5')
node6 = Node('6')

# Graph from Wikipedia page
node1.nodes = [node2, node5]
node2.nodes = [node3, node5]
node3.nodes = [node2, node4]
node4.nodes = [node3, node5, node6]
node5.nodes = [node1, node2, node4]
node6.nodes = [node4]


def breadth_first_search(node):
    print('Breadth-First Search Traversal')
    # Add the node to a queue.
    queue = []  # Could just define queue = [node] but this is for educational clarity.
    queue.insert(0, node)

    # Add the node to our set of discovered nodes.
    discovered = set()
    discovered.add(node)  # Same here.

    while queue:
        print('===\n')
        # Get a node from the queue.
        current_node = queue.pop()
        print(f'At node: {current_node}')

        # For each adjacent node
        for n in current_node.nodes:
            # If we haven't already discovered it
            if n not in discovered:
                # Add it to the queue
                print(f'Adding {current_node}->{n}')
                queue.insert(0, n)

                # Add it to the set of discovered nodes
                discovered.add(n)

            else:
                # Otherwise we've already discovered it
                print(f'Already discovered {current_node}->{n}')


        print(f'Queue: {queue}.\n\n')
    print(f'Final set of discovered nodes: {discovered}')


breadth_first_search(node1)


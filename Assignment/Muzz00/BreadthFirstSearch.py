import pyxel
import time
import random
#PLEASE REFER TO FIRST TO APPENDIX/INFORMATION OF THE BREADTH FIRST SEARCH DATA STRUCTURE

class Node:
    def __init__(self, data, nodes=None, parent=None, x=None, y=None, xLeft=0):
        self.data = data
        self.nodes = nodes
        self.parent = parent
        self.x = x
        self.y = y
        self.xLeft = xLeft

    def __str__(self):
        # return self.data
        return f'{self.data}'

    def __repr__(self):
        return self.data


# Randomly Generate Num
rand = []
for i in range(15):
    randNum = ""
    while randNum == "" or randNum in rand:
        randNum = random.randint(0, 100)
    rand.append(randNum)

# Nodes are created below
n1 = Node(str(rand[0]))
n2 = Node(str(rand[1]))
n3 = Node(str(rand[2]))
n4 = Node(str(rand[3]))
n5 = Node(str(rand[4]))
n6 = Node(str(rand[5]))
n7 = Node(str(rand[6]))
n8 = Node(str(rand[7]))
n9 = Node(str(rand[8]))
n10 = Node(str(rand[9]))
n11 = Node(str(rand[10]))
n12 = Node(str(rand[11]))
n13 = Node(str(rand[12]))
n14 = Node(str(rand[13]))
n15 = Node(str(rand[14]))

n1.nodes = [n2, n3]
n2.nodes = [n4, n5, n1]
n3.nodes = [n6, n1, n7, n8]
n4.nodes = [n2, n9, n10]
n5.nodes = [n2]
n6.nodes = [n3, n11, n12]
n7.nodes = [n3, n13, n14]
n8.nodes = [n3, n15]
n9.nodes = [n4]
n10.nodes = [n4]
n11.nodes = [n6]
n12.nodes = [n6]
n13.nodes = [n6]
n14.nodes = [n7]
n15.nodes = [n8]


pyxel.init(250, 150)


nodeSelector = n1 # Default Node


def update():
    global nodeSelector
    if pyxel.btn(pyxel.KEY_1):
        nodeSelector = n1

    if pyxel.btn(pyxel.KEY_2):
        nodeSelector = n2

    if pyxel.btn(pyxel.KEY_3):
        nodeSelector = n3


def draw():
    visited = []
    queue = []
    pyxel.cls(0)
    pyxel.text(0, 5, "Press 1, 2 or 3", 15)
    pyxel.text(0, 15, "to switch Node", 15)
    node = nodeSelector # Option of User if not default
    # Default settings
    node.xCount = len(node.nodes)
    node.x = 125
    node.y = 10
    node.xLeft = 0
    visited.append(node)
    queue.append(node)
    while queue:
        curNode = queue.pop(0)

        xCount = 0 # Internal counter of Nodes of a given Node

        # Calulate length of a Node
        lenNode = len(curNode.nodes)
        if curNode.data != node.data:
            lenNode -= 1 # Length of Node - 1 as the parent node wont be in the same horizontal x axis as the other child connected nodes.

        # Refer to appendix 1 for xLeft and appendix 2 for newXSpacing

        # Calculating the childs spacing of a given curNode
        if lenNode != 0:
            temp = (curNode.x - curNode.xLeft) * 2  # Calculates parents spacing dynamically. get the curNode.x e.g. 1's is 125. Minus that with horizontal spacing, which gives half spacing of parent element as Nodes are located on the center of spacing, hence multiple by 2.
            newXSpacing = (temp / lenNode)  # Calulate child spacing. ParentSpacing/numOfChild=ChildSpacing


        for n in curNode.nodes:
            if n not in visited:
                n.parent = curNode
                n.x = (xCount * newXSpacing) + (newXSpacing / 2) # Calculating x axis location. (InternalCounter * SpacingsOfChild) calculates the margin left of the node block. (newXSpacing/2) centers the node within its block rather than floating left.

                # Add xLeft of Parent to x and also to xLeft. We have to loop through the visited as we need to get the stored data that was produced dynamically.
                n.xLeft = xCount * newXSpacing
                for element in visited:
                    if element.data == curNode.data:
                        n.x += element.xLeft
                        n.xLeft += element.xLeft

                n.y = curNode.y + 25 # Add vertical spacing to each node

                visited.append(n)
                queue.append(n)
                xCount += 1

        # DRAWINGS
        # DRAW LINES FIRST
        for element in visited:
            if element.parent is not None:
                x1 = element.parent.x
                y1 = element.parent.y
                x2 = element.x
                y2 = element.y
                pyxel.line(x1, y1, x2, y2, 14)
        # DRAW CIRCLES
        for element in visited:
            pyxel.circ(element.x, element.y, 6, 12)
            pyxel.text(element.x - (len(element.data) * 1.5), element.y - 1, element.data, 2)
    pyxel.text(0, 125, 'Visited Nodes', 15)
    pyxel.text(0, 135, str(visited), 15)
    #print(f'\nVisited Nodes {visited}')


pyxel.run(draw, update)




# Dynamically space all elements.
#                                APPEDIX / INFORMATION OF BREADTH FIRST SEARCH DATA STRUCTURE
#             1
#           /  \
#        /      \
#      2         3
#    / \          \
#  /    \          \
# 4      5          6

# 1) IN THIS DOCUMENT xLeft variable represents the external spacing/margin from the left so that the nodes are equally spaced out.
# In other words calculates external horizontal spacing. e.g. if Node 1 is 250; Node 2 will be 0 and Node 3 will be 125

# 2) The newXSpacing is to calculate the spacing of a child from a given parent Node

# Mohamed Muzzammil P A
# 1519805
# Data Structure and Algorithms
# 01/07/2020
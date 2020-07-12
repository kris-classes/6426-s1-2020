import random
import heapq
import pyxel

class Node:
    def __init__(self, x,y,radius=5,color=8):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.radius = radius
        self.color = color

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)



class App:
    def __init__(self):
        pyxel.init(256, 180, caption="Min heap visualization")
        pyxel.mouse(True)

        self.status = 2

        self.randlslen = 0
        self.randomlist = []
        self.getrandomlist()


        self.outputlist = []
        self.heap()


        #node for n1 to n15

        self.n1 = Node(128, 30, 6, 8)

        self.n2 = Node(70, 65, 6, 8)
        self.n3 = Node(186, 65, 6, 8)

        if self.size >= 4:
            self.n4 = Node(35, 100, 6, 8)
        if self.size >= 5:
            self.n5 = Node(100, 100, 6, 8)
        if self.size >= 6:
            self.n6 = Node(155, 100, 6, 8)
        if self.size >= 7:
            self.n7 = Node(220, 100, 6, 8)

        if self.size >= 8:
            self.n8 = Node(20, 135, 6, 8)
        if self.size >= 9:
            self.n9 = Node(50, 135, 6, 8)
        if self.size >= 10:
            self.n10 = Node(85, 135, 6, 8)
        if self.size >= 11:
            self.n11 = Node(115, 135, 6, 8)
        if self.size >= 12:
            self.n12 = Node(140, 135, 6, 8)
        if self.size >= 13:
            self.n13 = Node(170, 135, 6, 8)
        if self.size >= 14:
            self.n14 = Node(205, 135)
        if self.size >= 15:
            self.n15 = Node(235, 135, 6, 8)

        pyxel.cls(0)

        pyxel.run(self.update, self.draw)


# get random amount of random number
    def getrandomlist(self):
        self.randlslen = random.randint(3, 15)

        for i in range(self.randlslen):
            n = random.randint(1, 99)
            self.randomlist.append(n)
        return self.randomlist


    def minheap(self):
        if self.status == 1:
            return True

    def maxheap(self):
        if self.status == 2:
            return True


    @property
    def size(self):
        return len(self.outputlist)

    def heap(self):
# min heap
        if self.minheap() is True:
            minheapnumlist = self.randomlist
            heapq.heapify(minheapnumlist)
            print('min')
            print(minheapnumlist)
            for j in minheapnumlist:
                j = str(j)
                self.outputlist.append(j)

# max heap
        elif self.maxheap() is True:
            maxheapnumlist = self.randomlist
            heapq._heapify_max(maxheapnumlist)
            print('max')
            print(maxheapnumlist)
            for k in maxheapnumlist:
                k = str(k)
                self.outputlist.append(k)


    def reset(self):
        if self.status == 0:
            self.outputlist = []
            self.randomlist = []
            self.getrandomlist()






    def update(self):
# mouse click for swap min and max heap
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            x = pyxel.mouse_x
            y = pyxel.mouse_y

            if x < 85 and y < 15:
                self.status = 1
                self.outputlist = []
                self.heap()
            elif 170 < x < 255 and y < 15:
                self.status = 2
                self.outputlist = []
                self.heap()

# key press for swap min heap and max heap
        if pyxel.btn(pyxel.KEY_1):
            self.status = 1
            self.outputlist = []
            self.heap()
        elif pyxel.btn(pyxel.KEY_2):
            self.status = 2
            self.outputlist = []
            self.heap()





    def draw(self):
        pyxel.cls(0)

# nevigation button
        pyxel.rectb(0, 0, 85, 15, 12)
        pyxel.text(30, 5, "Min heap", 12)

        pyxel.rectb(0, 0, 170, 15, 12)
        pyxel.text(110, 5, "New Random", 12)

        pyxel.rectb(0, 0, 255, 15, 12)
        pyxel.text(200, 5, "Max heap", 12)

# for each node, draw node, put value in node and draw line between parent and child

        # n1 to n3
        # n1 connect with n2 and n3
        self.n1.draw()
        pyxel.text(125, 28, self.outputlist[0], 7)
        self.n2.draw()
        pyxel.text(67, 63, self.outputlist[1], 7)
        pyxel.line(128, 37, 70, 58, 11)
        self.n3.draw()
        pyxel.text(183, 63, self.outputlist[2], 7)
        pyxel.line(128, 37, 186, 58, 11)

# n4 to n7
# n2 connect with n4 and n5
# n3 connect with n6 and n7
        if self.size >= 4:
            self.n4.draw()
            pyxel.text(32, 98, self.outputlist[3], 7)
            pyxel.line(70, 72, 35, 93, 11)
        if self.size >= 5:
            self.n5.draw()
            pyxel.text(97, 98, self.outputlist[4], 7)
            pyxel.line(70, 72, 100, 93, 11)
        if self.size >= 6:
            self.n6.draw()
            pyxel.text(152, 98, self.outputlist[5], 7)
            pyxel.line(186, 72, 155, 93, 11)
        if self.size >= 7:
            self.n7.draw()
            pyxel.text(217, 98, self.outputlist[6], 7)
            pyxel.line(186, 72, 220, 93, 11)

# n8 to n15
# n4 connect with n8 and n9
# n5 connect with n10 and n11
# n6 connect with n12 and n13
# n7 connect with n14 and n15

        if self.size >= 8:
            self.n8.draw()
            pyxel.text(17, 133, self.outputlist[7], 7)
            pyxel.line(35, 107, 20, 128, 11)
        if self.size >= 9:
            self.n9.draw()
            pyxel.text(47, 133, self.outputlist[8], 7)
            pyxel.line(35, 107, 50, 128, 11)
        if self.size >= 10:
            self.n10.draw()
            pyxel.text(82, 133, self.outputlist[9], 7)
            pyxel.line(100, 107, 85, 128, 11)
        if self.size >= 11:
            self.n11.draw()
            pyxel.text(112, 133, self.outputlist[10], 7)
            pyxel.line(100, 107, 115, 128, 11)
        if self.size >= 12:
            self.n12.draw()
            pyxel.text(137, 133, self.outputlist[11], 7)
            pyxel.line(155, 107, 140, 128, 11)
        if self.size >= 13:
            self.n13.draw()
            pyxel.text(167, 133, self.outputlist[12], 7)
            pyxel.line(155, 107, 170, 128, 11)
        if self.size >= 14:
            self.n14.draw()
            pyxel.text(202, 133, self.outputlist[13], 7)
            pyxel.line(220, 107, 205, 128, 11)
        if self.size >= 15:
            self.n15.draw()
            pyxel.text(232, 133, self.outputlist[14], 7)
            pyxel.line(220, 107, 235, 128, 11)

# display heap as list in button
        pyxel.text(0,170,f"heap: {self.outputlist}",7)



if __name__ == '__main__':
    App()






'''

pick minimum of 3 to maximumm of 15 f random number nad convert to stinglist
draw node and build tree for stringlist and put text of list value for each node
user can swap mai heap and max heap by either click on min heap and max heap button on screen or press 1 and 2

tree structure:
                    n1
                   /  \
                 /     \
               /        \
             /            \
            /              \
           n2               n3
           /  \            /  \
         /     \          /     \
        n4       n5      n6       n7
        /\       /\      /\       /\
       /   \    /   \   /  \     /   \
      n8   n9  n10  n11 n12 n13 n14   n15
  

strengths of using heap
easily fo find greatest and smallest number
Garbage collection runs on the heap memory to free the memory used by the object
no memory size limit


weekness of using heap
takes more time to compute
takes more time to execute
memory more complicated as it used globally





'''

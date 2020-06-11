"""
ISCG6426 Assignment

pip install --upgrade pyxel
See https://github.com/kitao/pyxel for library
Pyxel Discord: https://discord.gg/jNRYyXn
More examples: https://github.com/kris-classes/pyxel-snippets
"""
import pyxel
import random

class Item:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def draw(self):
        pyxel.circb(self.x, self.y, 15, 7)#空心圆
        pyxel.rect(self.x-10, self.y-10, 20, 20, 13)
        pyxel.circ(self.x, self.y, 10, 10)#实心圆
        pyxel.text(self.x-1, self.y-2, self.value, 8)

class Text:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class App:
    def __init__(self):
        pyxel.init(250, 230)

        self.stack = Stack()
        self.mode_pre_order = False
       # self.stack.push('5')
       # self.stack.push('8')


        # Give run the update/draw callbacks
        self.color = 1
        pyxel.mouse(True)
        self.points = []

        pyxel.run(self.update, self.draw)


    def update(self):

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.stack.push(str(random.randint(10, 15)))

        if pyxel.btnp(pyxel.KEY_P):
            self.stack.pop()


        '''
        if pyxel.btnp(pyxel.KEY_A):
            self.stack.push(str(random.randint(10, 15)))
  '''
            
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                self.color = (self.color + 1) % 16
                if self.color == 0:
                    self.color = self.color + 1
                print(f'color is {self.color}')
                self.points.append(Point(pyxel.mouse_x, pyxel.mouse_y, self.color))




    def draw_points(self):
        for point in self.points:
            pyxel.circ(point.x, point.y, 2, 2)
            pyxel.circb(point.x, point.y, 10, point.color)
            pyxel.tri(point.x, point.y+5, point.x-10, point.y-10, point.x+10, point.y-10, point.color)
            pyxel.tri(point.x-10, point.y, point.x+10, point.y, point.x, point.y-15, point.color) #空
            #pyxel.text(point.x, point.y, f'Now is {self.stack.size()} Number', self.color)## show the number of stack

    def draw(self):
        pyxel.cls(1)
        self.draw_points()
        offset = 0
        offy = 30
        offx = 10
        pyxel.line(95, 50, 95, 220, 8)   #left
        pyxel.line(155, 50, 155, 220, 8)   #right
        pyxel.line(95, 220, 155, 220, 8)   # button
        pyxel.line(95, 221, 155, 221, 8)

        pyxel.line(95, 50, 105, 50, 8)
        pyxel.line(145, 50, 155, 50, 8)
        pyxel.line(105, 50, 105, 40, 8)
        pyxel.line(145, 50, 145, 40, 8)



        if self.stack.size() ==0:
            pyxel.text(5, 10, 'This is an empty candy jar, Can put up to five candies', 10)
            pyxel.text(5, 17, 'Try your click your mouse left button to put a new candy', 11)
        if self.stack.size() == 1:
            pyxel.text(75, 195, 'TOP:', 6)
            pyxel.text(5, 15, 'Now you have a candy.', 13)
        if self.stack.size() == 2:
            pyxel.text(75, 165, 'TOP:', 6)
            pyxel.text(5, 15, 'Now you have 2 candies.', 13)
        if self.stack.size() == 3:
            pyxel.text(75, 135, 'TOP:', 6)
            pyxel.text(5, 15, 'Now you have 3 candies.', 14)
        if self.stack.size() == 4:
            pyxel.text(75, 105, 'TOP:', 6)
            pyxel.text(5, 15, 'Now you have 4 candies.', 13)
        if self.stack.size() == 5:
            pyxel.line(105, 40, 145, 40, 7)
            pyxel.text(75, 75, 'TOP:', 6)
            pyxel.text(5, 5, 'Now you have 5 candies. This candy jar is full', 11)
            pyxel.text(5, 15, 'Wanna eat candies? Try to press P', 10)





        for value in self.stack.stack:
            myItem = Item(125+ offx, 230-offy, value)     #1
            myItem.draw()
           # pyxel.text(145, 230-offy, 'Use push()', self.color)
            offset = offset + 1
            offy = offy+30
            if offx == 10:
                offx = offx -10
            else:
                offx = offx + 10

            if offset > 7:
                break

            #myItem2.draw()


class Stack(object):

    def __str__(self):
        return f'{self.stack}'

    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self.stack = []

    def if_Full(self):
        if len(self.stack) == self.maxsize:
            return True
        else:
            return False

    def push(self, item):
        if self.if_Full():
            print('stack is full')
        else:
            self.stack.append(item)


    def pop(self):
        if self.is_empty():
            print('stack is empty')
        else:
            self.stack.pop()


    def peek(self):
        """top"""
        if self.stack is None:
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        """how many"""
        #return self.stack.size()
        return len(self.stack)

    def range(self, start, end):
        return self.stack[start:end]


if __name__ == "__main__":
    s = Stack()
    print(s.size())

    App()
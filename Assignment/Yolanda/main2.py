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
        pyxel.cls(0)
        self.stack = Stack()
        self.stack.push('5')
        self.stack.push('8')

        # Give run the update/draw callbacks
        self.color = 1
        pyxel.mouse(True)
        self.points = []

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_P):
            self.stack.pop()
        if pyxel.btnp(pyxel.KEY_A):
            self.stack.push(str(random.randint(10, 15)))
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
            pyxel.text(point.x, point.y, f'Now is {self.stack.size()} Number', self.color)## show the number of stack

    def draw(self):
        pyxel.cls(0)
        self.draw_points()
        if self.stack.size() <= 3:
            pyxel.text(10, 30, f'{self.stack.range(0,4)}', 2)     #横排
        if 4 <= self.stack.size() <= 7:
            pyxel.text(10, 30, f'{self.stack.range(0, 4)}', 2)
            pyxel.text(10, 50, f'{self.stack.range(4,7)}', 2)
        if 7 < self.stack.size():
            pyxel.text(10, 220, 'Too Many Numbers In This Small Screen!!!', 5)
            pyxel.text(10, 200, ' Try "P"', 10)

        offset = 0
        offy = 30

        for value in self.stack.stack:
            myItem = Item(125, 230-offy, value)     #1
            pyxel.text(145, 230-offy, 'Use push()', self.color)
            offset = offset + 1
            offy = offy+30
            if offset > 7:
                break
            myItem.draw()
            #myItem2.draw()


class Stack(object):

    def __str__(self):
        return f'{self.stack}'

    def __init__(self, maxsize=7):
        self.maxsize = maxsize
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        """top"""
        if self.stack is None:
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        """true false"""
        return self.stack == []
        # return not self.__list

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
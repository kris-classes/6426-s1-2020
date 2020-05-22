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
    '''
 def draw(self):
        color = 1
        for x in self.x:
            pyxel.circb(self.x, self.y, 10, color)
            pyxel.text(self.x-1, self.y-2, self.value, color)
            color = color+1

'''
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class App:
    def __init__(self):
        pyxel.init(220, 220)
        pyxel.cls(0)
       # self.item1 = Item(30,50,'15')
       # self.item2 = Item(50,70,'30')
        self.stack = Stack()
        self.stack.push('5')
        self.stack.push('8')
        #self.stack.push('a')

        # Give run the update/draw callbacks
        self.color = 1
        pyxel.mouse(True)
        self.points = []

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_P):
            self.stack.pop()
        if pyxel.btnp(pyxel.KEY_A):
            self.stack.push(str(random.randint(10, 20)))
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
            #pyxel.text(point.x, point.y, f'Now is {self.color} color', self.color)# change
            pyxel.text(point.x, point.y, f'Now is {self.stack.size()} Number', self.color)## show the number of stack

    def draw(self):
        pyxel.cls(0)
        self.draw_points()
        if self.stack.size() <= 5:
            pyxel.text(50, 100, f'{self.stack.range(0,5)}', 2)     #横排
        if 5<self.stack.size() <= 10:
            pyxel.text(50, 100, f'{self.stack.range(0, 5)}', 2)
            pyxel.text(50, 110, f'{self.stack.range(5,10)}', 2)
        if 10 < self.stack.size():
            pyxel.text(40, 100, 'Too Many Numbers In This Small Screen!!!', 5)
            pyxel.text(80, 110, ' Try "P"', 10)
        #pyxel.text(30, 70, f'this is {self.color} color', 2)"

        #pyxel.rect(10, 20, 10, 10, 5)
        #self.item1.draw()
        #self.item2.draw()
        offset = 0
        for value in self.stack.list:
            myItem = Item(10, 10+offset, value)     #1
            pyxel.line(10, 20, 30, 90, 5) # MAIN
            pyxel.line(20, 80, 30, 90, 5) #LEFT
            pyxel.line(32, 78, 30, 90, 5) #RIGHT
            pyxel.text(30, 90, 'This is the First number' ' Use push()', self.color)
            offset = offset + 20
            if offset > 20:
                myItem = Item(10 + offset, 10, value) #2
                pyxel.line(50, 20, 40, 80, 5)  # MAIN
                pyxel.line(38, 70, 40, 80, 5)  # LEFT
                pyxel.line(48, 70, 40, 80, 5)  # RIGHT
                pyxel.text(40, 80, 'This is the second number' 'Use push()', self.color)
                if offset > 40:
                    myItem = Item(10, offset, value)    #3
                    pyxel.line(10, 70, 40, 120, 5)  # MAIN
                    pyxel.line(30, 115, 40, 120, 5)  # LEFT
                    pyxel.line(38, 110, 40, 120, 5)  # RIGHT
                    pyxel.text(40, 120, 'This is the third number' 'Use push()', self.color)
                    if offset > 60:
                        myItem = Item(10 + offset, 10 , value)  #4
                        pyxel.line(90, 20, 50, 70, 5)  # MAIN
                        pyxel.line(52, 58, 50, 70, 5)  # LEFT
                        pyxel.line(65, 65, 50, 70, 5)  # RIGHT
                        pyxel.text(50, 70, 'This is the fourth number' 'Use push()', self.color)
                        if offset > 80:
                            myItem = Item(10, 10 + offset, value) #5
                            pyxel.line(10, 120, 50, 130, 5)  # MAIN
                            pyxel.line(37, 130, 50, 130, 5)  # LEFT
                            pyxel.line(38, 125, 50, 130, 5)  # RIGHT
                            pyxel.text(50, 130, 'This is the fifth number' 'Use push()', self.color)
                            if offset > 100:
                                myItem = Item(10 + offset, 10, value)  #6
                                pyxel.line(130, 20, 80, 60, 5)  # MAIN
                                pyxel.line(85, 50, 80, 60, 5)  # LEFT
                                pyxel.line(95, 53, 80, 60, 5)  # RIGHT
                                pyxel.text(60, 60, 'This is the sixth number' 'Use push()', self.color)
                                if offset > 120:
                                    myItem = Item(10 , 10+ offset, value) #7
                                    pyxel.line(20, 150, 60, 140, 5)  # MAIN
                                    pyxel.line(50, 137, 60, 140, 5)  # LEFT
                                    pyxel.line(50, 145, 60, 140, 5)  # RIGHT
                                    pyxel.text(60, 140, 'This is the seventh number' 'Use push()', self.color)
                                    if offset > 140:
                                        myItem = Item(10 + offset, 10, value) #8
                                        pyxel.line(170, 20, 110, 50, 12)  # MAIN
                                        pyxel.line(110, 45, 110, 50, 5)  # LEFT
                                        pyxel.line(127, 47, 110, 50, 5)  # RIGHT
                                        pyxel.text(70, 50, 'This is the eighth number' 'Use push()', self.color)
                                        if offset > 160:
                                            myItem = Item(10, 10 + offset, value) #9
                                            pyxel.line(20, 190, 90, 160, 5)  # MAIN
                                            pyxel.line(80, 158, 90, 160, 5)  # LEFT
                                            pyxel.line(88, 170, 90, 160, 5)  # RIGHT
                                            pyxel.text(70, 150, 'This is the ninth number' 'Use push()', self.color)
                                            if offset > 180:
                                                myItem = Item(10 + offset, 10, value) #10
                                                pyxel.line(210, 20, 150, 40, 12)  # MAIN
                                                pyxel.line(155, 35, 150, 40, 5)  # LEFT
                                                pyxel.line(168, 37, 150, 40, 5)  # RIGHT
                                                pyxel.text(80, 40, 'This is the tenth number' 'Use push()', self.color)
                                                if offset > 200:
                                                    break;


            myItem.draw()
            #myItem2.draw()



class Stack(object):
    def __str__(self):
        return f'{self.list}'

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        """top"""
        if self.list is None:
            return None
        else:
            return self.list[-1]

    def is_empty(self):
        """true false"""
        return self.list == []
        # return not self.__list

    def size(self):
        """how many"""
        #return self.stack.size()
        return len(self.list)

    def range(self, start, end):
        return self.list[start:end]


if __name__ == "__main__":
    s = Stack()
    print(s.size())

    App()
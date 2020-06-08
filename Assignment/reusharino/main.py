"""
ISCG6426 Assignment

pip install --upgrade pyxel
See https://github.com/kitao/pyxel for library
Pyxel Discord: https://discord.gg/jNRYyXn
More examples: https://github.com/kris-classes/pyxel-snippets
"""
import pyxel
import random
import heapq


# Create additional classes here if you want.
class Circle:
    def __init__(self, x, y, radius=5, color=8, value=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.value = value

    def update(self):
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)


def randomList():
    LO = [i for i in range(15)]
    random.shuffle(LO)
    return LO


LO = randomList()


class App:

    def __init__(self):
        # Initialize a window. Max size is 256x256 pixels.
        pyxel.init(255, 255)

        self.x = 10
        self.y = 10
        self.message = "HEAPS BRO"
        # co-ordinates
        p = 128, 50

        l = 98, 60
        r = 158, 60

        ll = 68, 80
        lr = 108, 80

        rl = 148, 80
        rr = 188, 80

        lll = 58, 100
        llr = 78, 100

        lrl = 98, 100
        lrr = 118, 100

        rll = 138, 100
        rlr = 158, 100

        rrl = 178, 100
        rrr = 198, 100
        # parent
        self.n1 = Circle(p[0], p[1], 5, 1, LO[0])

        # layer2
        self.n2 = Circle(l[0], l[1], 5, 2, LO[1])
        self.n3 = Circle(r[0], r[1], 5, 3, LO[2])
        # layer 3
        self.n4 = Circle(ll[0], ll[1], 5, 4, LO[3])
        self.n5 = Circle(lr[0], lr[1], 5, 5, LO[4])

        self.n6 = Circle(rl[0], rl[1], 5, 6, LO[5])
        self.n7 = Circle(rr[0], rr[1], 5, 7, LO[6])
        # layer 4
        self.n8 = Circle(lll[0], lll[1], 5, 8, LO[7])
        self.n9 = Circle(llr[0], llr[1], 5, 9, LO[8])

        self.n10 = Circle(lrl[0], lrl[1], 5, 10, LO[9])
        self.n11 = Circle(lrr[0], lrr[1], 5, 11, LO[10])

        self.n12 = Circle(rll[0], rll[1], 5, 12, LO[11])
        self.n13 = Circle(rlr[0], rlr[1], 5, 13, LO[12])

        self.n14 = Circle(rrl[0], rrl[1], 5, 14, LO[13])
        self.n15 = Circle(rrr[0], rrr[1], 5, 15, LO[14])

        # Clear the screen with color 0 (black). Max color is 15.
        pyxel.cls(0)

        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.KEY_W):
            self.y -= 1
        if pyxel.btnp(pyxel.KEY_A):
            self.x -= 1
        if pyxel.btnp(pyxel.KEY_S):
            self.y += 1
        if pyxel.btnp(pyxel.KEY_D):
            self.x += 1

    def draw(self):
        # Always remember to clear the screen.
        pyxel.cls(0)

        pyxel.text(self.x, self.y, self.message, 7)
        self.n1.draw()
        self.n2.draw()
        self.n3.draw()
        self.n4.draw()
        self.n5.draw()
        self.n6.draw()
        self.n7.draw()
        self.n8.draw()
        self.n9.draw()
        self.n10.draw()
        self.n11.draw()
        self.n12.draw()
        self.n13.draw()
        self.n14.draw()
        self.n15.draw()


if __name__ == '__main__':
    App()

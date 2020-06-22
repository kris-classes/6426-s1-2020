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
    def __init__(self, x, y, radius=5, color=0, value=0):
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


isMinHeap = False


def minHeap(listObj, checker):
    def heapPush(listObj, checker):
        # checker = True
        heapObj = []
        heapq.heapify(heapObj)
        for i in listObj:
            heapq.heappush(heapObj, listObj[i])
            # print(listObj[i])
            heapq.heapify(heapObj)
            # print(heapObj)
        listObj = heapObj
        return listObj, checker

    def heapIT(listObj, checker):
        checker = True
        heapPush(listObj)
        heapq.heapify(listObj)
        return listObj, checker

    heapIT(listObj, isMinHeap)


def maxHeap(listObj):
    def heapify(listObj, n, i):
        biggest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and listObj[l] > listObj[biggest]:
            biggest = l

        if r < n and listObj[r] > listObj[biggest]:
            biggest = r

        if biggest != i:
            listObj[i], listObj[biggest] = listObj[biggest], listObj[i]

            heapify(listObj, n, biggest)

    def buildHeap(listObj, n):
        startIdx = n // 2 - 1
        checker = False
        for i in range(startIdx, -1, -1):
            heapify(listObj, n, i)

    n = len(listObj)
    buildHeap(listObj, n)
    return listObj


LO = randomList()

NL = []
for i in LO:
    NL.append(i)

x = random.randint(1, 100)
print(x)
if x // 2 == 0:
    LO = randomList()
    minHeap(LO)
    NL = []
    print(LO)
    for i in LO:
        NL.append(i)

elif x // 2 == 1:
    LO = randomList()
    maxHeap(LO)
    NL = []
    print(LO)
    for i in LO:
        NL.append(i)
print(LO)


class App:

    def __init__(self):
        # Initialize a window. Max size is 256x256 pixels.
        pyxel.init(255, 255)

        self.x = 10
        self.y = 10
        pyxel.mouse(True)

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
        self.n1 = Circle(p[0], p[1], 7, LO[0] + 1, LO[0])

        # layer2
        self.n2 = Circle(l[0], l[1], 7, LO[1] + 1, LO[1])
        self.n3 = Circle(r[0], r[1], 7, LO[2] + 1, LO[2])
        # layer 3
        self.n4 = Circle(ll[0], ll[1], 7, LO[3] + 1, LO[3])
        self.n5 = Circle(lr[0], lr[1], 7, LO[4] + 1, LO[4])

        self.n6 = Circle(rl[0], rl[1], 7, LO[5] + 1, LO[5])
        self.n7 = Circle(rr[0], rr[1], 7, LO[6] + 1, LO[6])
        # layer 4
        self.n8 = Circle(lll[0], lll[1], 7, LO[7] + 1, LO[7])
        self.n9 = Circle(llr[0], llr[1], 7, LO[8] + 1, LO[8])

        self.n10 = Circle(lrl[0], lrl[1], 7, LO[9] + 1, LO[9])
        self.n11 = Circle(lrr[0], lrr[1], 7, LO[10] + 1, LO[10])

        self.n12 = Circle(rll[0], rll[1], 7, LO[11] + 1, LO[11])
        self.n13 = Circle(rlr[0], rlr[1], 7, LO[12] + 1, LO[12])

        self.n14 = Circle(rrl[0], rrl[1], 7, LO[13] + 1, LO[13])
        self.n15 = Circle(rrr[0], rrr[1], 7, LO[14] + 1, LO[14])

        self.minButton = Circle(94, 158, 20, 8, 0)
        self.maxButton = Circle(164, 158, 20, 8, 0)

        # Clear the screen with color 0 (black). Max color is 15.
        pyxel.cls(0)

        pyxel.run(self.update, self.draw)

    def update(self):
        x = 0
        y = 0
        if pyxel.btnp(pyxel.KEY_W):
            self.y -= 1
        if pyxel.btnp(pyxel.KEY_A):
            self.x -= 1
        if pyxel.btnp(pyxel.KEY_S):
            self.y += 1
        if pyxel.btnp(pyxel.KEY_D):
            self.x += 1
            minHeap(LO)
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
        if 94 > x > 114 and 158 < y < 178:
            minHeap(LO)
            self.draw()
            print("click")
        if 164 > x > 184 and 158 < y < 178:
            maxHeap(LO)
            self.draw()
            print("click")

    def draw(self):
        # Always remember to clear the screen.
        pyxel.cls(0)

        # Line Structure
        # Parent
        pyxel.line(128, 50, 98, 60, 7)
        pyxel.line(128, 50, 158, 60, 7)

        # Left
        pyxel.line(98, 60, 68, 80, 7)
        pyxel.line(98, 60, 108, 80, 7)

        # Right
        pyxel.line(158, 60, 148, 80, 7)
        pyxel.line(158, 60, 188, 80, 7)

        # Left Left
        pyxel.line(68, 80, 58, 100, 7)
        pyxel.line(68, 80, 78, 100, 7)

        # Left Right
        pyxel.line(108, 80, 98, 100, 7)
        pyxel.line(108, 80, 118, 100, 7)

        # Right Left
        pyxel.line(148, 80, 138, 100, 7)
        pyxel.line(148, 80, 158, 100, 7)

        # Right Right
        pyxel.line(188, 80, 178, 100, 7)
        pyxel.line(188, 80, 198, 100, 7)

        # Nodes
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

        pyxel.text(125, 48, str(LO[0]), 0)

        pyxel.text(95, 58, str(LO[1]), 0)
        pyxel.text(155, 58, str(LO[2]), 0)

        pyxel.text(65, 78, str(LO[3]), 0)
        pyxel.text(105, 78, str(LO[4]), 0)
        pyxel.text(145, 78, str(LO[5]), 0)
        pyxel.text(185, 78, str(LO[6]), 0)

        pyxel.text(55, 98, str(LO[7]), 0)
        pyxel.text(75, 98, str(LO[8]), 0)
        pyxel.text(95, 98, str(LO[9]), 0)
        pyxel.text(115, 98, str(LO[10]), 0)
        pyxel.text(135, 98, str(LO[11]), 0)
        pyxel.text(155, 98, str(LO[12]), 0)
        pyxel.text(175, 98, str(LO[13]), 0)
        pyxel.text(195, 98, str(LO[14]), 0)

        # Text and buttons
        pyxel.text(80, 200, "This is the initial list", 7)
        pyxel.text(30, 210, str(NL), 7)
        if isMinHeap == True:
            self.minButton.draw()
            pyxel.text(80, 150, "THIS IS \n   A\nMIN HEAP", 7)
        if isMinHeap == False:
            self.maxButton.draw()
            pyxel.text(150, 150, "THIS IS \n   A\nMAX HEAP", 7)

        pyxel.text(10, 10, "HEAPS BRO", 7)

        # print(LO)
        # print(minHeap(LO))
        # print(maxHeap(LO))


if __name__ == '__main__':
    App()

"""
ISCG6426 Assignment

pip install --upgrade pyxel
See https://github.com/kitao/pyxel for library
Pyxel Discord: https://discord.gg/jNRYyXn
More examples: https://github.com/kris-classes/pyxel-snippets
"""
import pyxel
import random


class App:

    def __init__(self):
        # Initialize a window. Max size is 256x256 pixels.
        pyxel.init(250, 190, caption="QUEUE DATA STRUCTURE VISUALISATION")
        self.queue = Queue()
        pyxel.mouse(True)
        self.ENQUEUE = False
        self.DEQUEUE = False


        # Clear the screen with color 0 (black). Max color is 15.
        pyxel.cls(0)

        pyxel.run(self.update, self.draw)

    def update(self):
        # Put your logic in here.
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


        pyxel.rect(50, 100, 15, 15, 7)

        pyxel.rect(80, 100, 15, 15, 7)

        pyxel.rect(110, 100, 15, 15, 7)


        pyxel.rect(140, 100, 15, 15, 7)


        pyxel.rect(170, 100, 15, 15, 7)


        if self.ENQUEUE:
            pyxel.rect(20, 10, 64, 15, 6)
            pyxel.text(35, 15, "Enqueue", 9)
        else:
            pyxel.rect(20, 10, 64, 15, 9)
            pyxel.text(35, 15, "Enqueue", 6)

        if self.DEQUEUE:
            pyxel.rect(160, 10, 64, 15, 6)
            pyxel.text(180, 15, "Dequeue", 9)
        else:
            pyxel.rect(160, 10, 64, 15, 9)
            pyxel.text(180, 15, "Dequeue", 6)




class Queue:

    def __init__(self,  maxsize = 8):
        self.maxsize = maxsize
        self.queue =[]

    def isEmpty(self):
        return self.queue ==[]

    def isFull(self):
        if len(self.queue) == self.maxsize:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.isFull():
            print("Cannot add another item ; Use dequeue to pop something out of the queue")
        else:
            self.queue.append()

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue because there is no item in the queue")
        else:
            item = self.queue[0]
            del self.queue[0]
            return item

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()
    print(queue.sizeQueue())

    App()
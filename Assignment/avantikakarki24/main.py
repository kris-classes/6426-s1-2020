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
        pyxel.init(260, 120)

        self.queue = Queue()

        pyxel.run(self.update, self.draw)





class Queue:

    def __init__(self, maxsize = 8):
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
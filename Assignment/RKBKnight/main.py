"""
ISCG6426 Assignment

pip install --upgrade pyxel
See https://github.com/kitao/pyxel for library
Pyxel Discord: https://discord.gg/jNRYyXn
More examples: https://github.com/kris-classes/pyxel-snippets
"""
import pyxel
import heap_priority_queue

# Create additional classes here if you want.
priority_Queue = heap_priority_queue.PriorityQueue()

class App:

    def __init__(self):
        # Initialize a window. Max size is 256x256 pixels.
        pyxel.init(200,150, caption="Heap Priority Queue")
        self.newQueue = []
        self.exeList = []
        # Clear the screen with color 0 (black). Max color is 15.
        pyxel.cls(5)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_S):
            priority_Queue.queue = priority_Queue.setList(0)
            self.exeList = priority_Queue.queue
        if pyxel.btnp(pyxel.KEY_R):
            priority_Queue.queue = priority_Queue.setList(1)
            self.exeList = priority_Queue.queue
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.check_Pos()

    def check_Pos(self):
        if (77 > pyxel.mouse_x > 7) and (87 < pyxel.mouse_y < 97):
            self.newQueue = priority_Queue.runHeapify()

        if (136 > pyxel.mouse_x > 60) and (107 < pyxel.mouse_y < 117):
            priority_Queue.queue = priority_Queue.changeRandomList()
            self.exeList = priority_Queue.queue

    def draw(self):
        pyxel.cls(0)
        pyxel.text(25, 5, "Heap Priority Queue", 7)
        pyxel.text(10, 15, f" Press 'S'  for  sorted list  or \n Press 'R' for random list", 10)
        pyxel.text(10, 30, f"Press 'esc' to Quit", 8)
        pyxel.rectb(7, 87, 70, 10, 3)
        pyxel.text(10, 90, "Start Heapify", 1)
        pyxel.rectb(60, 107, 76, 13, 3)
        pyxel.text(63, 110, "Change random List", 1)
        counter = 0
        for i in self.exeList:
            counter = counter + 1
            text_x = 30 + 10 * counter
            text_y = 50
            pyxel.text(text_x, text_y, str(i), 7)
            pyxel.rectb(text_x - 3, text_y - 3, 10, 10, 7)

        if len(self.newQueue) > 0:
            counter = 0
            for i in self.newQueue:
                counter = counter + 1
                text_x = 30 + 10 * counter
                text_y = 70
                pyxel.text(text_x, text_y, str(i), 7)
                pyxel.rectb(text_x - 3, text_y - 3, 10, 10, 7)


if __name__ == '__main__':
    App()

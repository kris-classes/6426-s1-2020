"""
ISCG6426 Assignment

pip install --upgrade pyxel
See https://github.com/kitao/pyxel for library
Pyxel Discord: https://discord.gg/jNRYyXn
More examples: https://github.com/kris-classes/pyxel-snippets
"""
import pyxel
import random

class Arrow:
    def __init__(self, x, y, radius=5, color=8):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def update(self):
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)

random_list = [random.randint(0, 9) for i in range(10)]
random_list.sort()

class App:
    def __init__(self):
        pyxel.init(240, 200, caption = "Binary Search visualization")
        pyxel.mouse(True)
        pyxel.cls(0)
        pyxel.run(self.update, self.draw)

    def check_click(self,mouse_x,mouse_y):
        """check for mouse click"""
        text_x = 55
        text_y = 45
        if text_x < mouse_x < text_x + 100 and text_y < mouse_y < text_y + 10:
            search_for = (pyxel.mouse_x - 55) // 10
            return search_for

    def update(self):
        """check any button click"""
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            App.check_click(self,pyxel.mouse_x, pyxel.mouse_y)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        """draw the items on screen"""
        pyxel.cls(0)
        pyxel.text(165, 10, "press esc to quit", 6)
        pyxel.text(55, 35,"choose a number to search from list", 5)
        for i in range(10):
            text_x = 60 + 10 * i
            text_y = 50
            if text_x - 5 < pyxel.mouse_x < text_x + 5 and text_y -5 < pyxel.mouse_y < text_y + 5:
                text_col = 6
            else:
                text_col = 5
            pyxel.text(text_x, text_y, str(i), text_col)
            pyxel.rectb(text_x-3, text_y-3, 10, 10, text_col)
            pyxel.text(60, 80, str(App.check_click), 7)

        list_x = 50
        list_y = 130
        for i in range(len(random_list)): # draw the list
            pyxel.text(list_x + 15 * i, list_y, str(random_list[i]), 7)
            pyxel.rectb(list_x - 3 + 15 * i, list_y - 3, 10, 10, 7)
        pyxel.text(10, 10, "Binary Search", 7)


if __name__ == '__main__':
    App()

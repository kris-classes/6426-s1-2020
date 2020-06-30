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
class SomeCircle:
    def __init__(self, x, y, radius=5, color=8):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def update(self):
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)



class App:
    def __init__(self):
        # Initialize a window. Max size is 256x256 pixels.
        pyxel.init(160, 120)

        self.x = 50
        self.y = 50
        self.message = "ISCG 6426"
        self.circle1 = SomeCircle(100, 100, 5, 8)
        self.circle2 = SomeCircle(100, 25, 10, 12)

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

        pyxel.text(self.x, self.y, self.message, 7)
        self.circle1.draw()
        self.circle2.draw()

    def


if __name__ == '__main__':
    App()


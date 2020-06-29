"""
ISCG6426 Assignment

pip install --upgrade pyxel
See https://github.com/kitao/pyxel for library
Pyxel Discord: https://discord.gg/jNRYyXn
More examples: https://github.com/kris-classes/pyxel-snippets
"""
import pyxel
import random

# Initialize a window of width 160 x height 120
pyxel.init(200, 120)

pyxel.cls(0)


text_x = 10
text_y = 5
pyxel.text(text_x, text_y, "QUEUE DATA STRUCTURE VISUALISATION",1)  # Use color 8 (pink)

list =[]

def update():
    global list # globals are bad practice but are ok for this example.
    if pyxel.btnp(pyxel.KEY_R):
        a = random.randint(0,100)
        list.append(a)
    print(list)

# Define a function responsible for drawing.
def draw():
    global list  # globals are bad practice but are ok for this example.
    pyxel.cls(0)

    print(f'color: {list}')

pyxel.run(update, draw)



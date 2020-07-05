"""
###############################
ISCG6426 Assignment
Jack Marshall-Young
Conway's Game Of Life
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
###############################
Controls:
Space to start/pause simulation
Click to place a pixel, works best when simulation is paused
Up and down arrows to speed up and slow down simulation
###############################
Presets: (Num keys)
1: Glider
2: Small exploder
3: Exploder
4: Lightweight space ship
5: Blinker
Warning: It's possible to spawn multiple presets ontop of each other, which means they will vanish right away.
###############################
Game rules/logic:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
More simply:
1. any live cell with two or three neighbors lives
2. any dead cell with three live neighbors becomes a live cell
###############################
"""
import pyxel
import time

alive_cells = []
dead_cell_scans = [] # keeps track of all tested dead cells, reset every simulation tick
test_cells = [] # test ONLY, used here so the test cells redraw
reviving_cells = []
dying_cells = []
lastupdate = 0.0
cellID = 0
gameActive = False
debug = False
sim_frame_active = False
sim_speed = 8

# code used for anything
def getNeighbors(cell, all_living_cells, test=False, test_color=8):
    """ Returns all alive neighbors for a given pixel """

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

# additional data structure
class Set:
    """
    Basic implementation of a set.
    Set must NOT contain duplicates.
    """

    def __init__(self, initial_data=[]):
        # NOTE: I've done this for you to show how it's done.
        # self.data MUST remain a list throughout.
        unique_only = []
        self.current = 0
        for element in initial_data:
            if element not in unique_only:
                unique_only.append(element)
        self.data = unique_only

    def __str__(self):
        return f'<Set __str__: {self.data}>'

    def __repr__(self):
        # Used when you type my_set into the shell.
        return f'<Set __repr__: {self.data}>'

    def __add__(self, other):
        result = []
        for new_item in other:
            if new_item not in self.data:
                result.append(new_item)
        return self.data+result

    def __contains__(self, element): # used default contains for the list
        if hasattr(self.data[0], "__contains__"):
            return self.data[0].__contains__(element)
        return self.data.__contains__(element)

    def __iter__(self): # uses default iterator for the list
        if hasattr(self.data[0], "__iter__"):
            return self.data[0].__iter__()
        return self.data.__iter__()

    def append(self, new_item):
        if new_item not in self.data:
            self.data.append(new_item)

    def remove(self, element):
        # Remove an element from a set. Raise an exception if it does not exist
        if element in self.data:
            self.data.remove(element)
        else:
            raise Exception("Element not found in set")

# define some variables
alive_cells = Set()
dead_cell_scans = [] # keeps track of all tested dead cells, reset every simulation tick
test_cells = [] # test ONLY, used here so the test cells redraw
reviving_cells = []
dying_cells = []
lastupdate = 0.0
cellID = 0
gameActive = False
debug = False
sim_speed = 8

# code used for anything
def getNeighbors(cell, all_living_cells, test=False, test_color=8):
    """ Returns all alive neighbors for a given pixel """
    neighbors = []
    NeighborCellGrid = [  # all possible neighbor positions
        [cell.x - 1, cell.y - 1],  # top left
        [cell.x, cell.y - 1],  # top
        [cell.x + 1, cell.y - 1],  # top right
        [cell.x - 1, cell.y],  # left
        [cell.x + 1, cell.y],  # right
        [cell.x - 1, cell.y + 1],  # bottom left
        [cell.x, cell.y + 1],  # bottom
        [cell.x + 1, cell.y + 1]  # bottom right
    ]
    for i in all_living_cells:
        if i.id != cell.id and i.alive == True:  # not self and pixel is alive
            if [i.x, i.y] in NeighborCellGrid:  # next to
                neighbors.append(i)
    if test:
        for i in NeighborCellGrid:
            g = simCell(i[0], i[1], color=test_color)
            test_cells.append(g)

    return neighbors

def getNeighborCount(sim, all_sims, test=False, test_color=8):
    return len(getNeighbors(sim, all_sims, test, test_color))

class simCell():
    def __init__(self, x, y, color=5, alive=True):
        global cellID
        self.x = x
        self.y = y
        self.alive = alive
        self.color = color
        self.id=cellID+1
        cellID+=1

    def __repr__(self):
        return f"(Sim at (x: {self.x}, y: {self.y}) Color: {self.color})"

    def draw(self):
        pyxel.pset(self.x, self.y, self.color)

    def deadPixel(self): # removes cells that are marked for deletion
        if self in alive_cells: # confirm that pixel hasn't died already
            alive_cells.remove(self)

class App:
    def __init__(self):
        global alive_cells
        # create a glider on start
        alive_cells = Set([simCell(25,25), simCell(26,26), simCell(24,27), simCell(25,27), simCell(26,27)])  # x, y, alive
        # Initialize a window. Max size is 256x256 pixels.
        pyxel.init(50, 50)
        self.x = 50
        self.y = 50
        pyxel.mouse(False)
        pyxel.pal(12, pyxel.COLOR_RED) # set 12 to "red"
        pyxel.pal(5, pyxel.COLOR_WHITE) # is the set color of the living cells
        pyxel.cls(0)
        pyxel.run(self.update, self.draw)

    def update(self):
        global gameActive
        global debug
        global sim_speed
        global alive_cells
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            # check to see if there is a pixel there already
            np = simCell(x=pyxel.mouse_x, y=pyxel.mouse_y, alive=True)
            alive_cells.append(np)
            np.draw()
            if debug:
                print(f"MouseX: {pyxel.mouse_x}, MouseY {pyxel.mouse_y}")
        if pyxel.btnp(pyxel.KEY_SPACE): # start the simulation
            if not gameActive:
                gameActive = True
            else:
                gameActive = False
        if pyxel.btnp(pyxel.KEY_M): # debug mode
            if not debug:
                debug = True
            else:
                debug = False

        if pyxel.btnp(pyxel.KEY_UP): # speed up simulation
            if sim_speed > 5:
                sim_speed = sim_speed - 5

        if pyxel.btnp(pyxel.KEY_DOWN): # slow down simulation
            sim_speed = sim_speed + 5



        if pyxel.btnp(pyxel.KEY_1): # glider preset
            startPosX = 18  # top left
            startPosY = 18  # top left
            # glider
            glider = [simCell(startPosX+1, startPosY), # row 1
                      simCell(startPosX+2, startPosY+1), # row 2
                      simCell(startPosX, startPosY+2), simCell(startPosX+1, startPosY+2), simCell(startPosX+2, startPosY+2)] # row 3
            alive_cells+=glider

        if pyxel.btnp(pyxel.KEY_2):  # small exploder
            startPosX = 30
            startPosY = 10
            quadBlinker = [simCell(startPosX + 1, startPosY),  # row 1
                      simCell(startPosX, startPosY + 1), simCell(startPosX + 1, startPosY + 1), simCell(startPosX + 2, startPosY + 1),  # row 2
                      simCell(startPosX, startPosY + 2), simCell(startPosX + 2, startPosY + 2), # row 3
                      simCell(startPosX+1, startPosY + 3)] # row 4
            alive_cells+=quadBlinker

        if pyxel.btnp(pyxel.KEY_3):  # exploder
            startPosX = 10
            startPosY = 22
            exploder = [simCell(startPosX, startPosY), simCell(startPosX+2, startPosY), simCell(startPosX+4, startPosY),  # row 1
                      simCell(startPosX, startPosY + 1), simCell(startPosX + 4, startPosY + 1),  # row 2
                      simCell(startPosX, startPosY + 2), simCell(startPosX + 4, startPosY + 2), # row 3
                      simCell(startPosX, startPosY + 3), simCell(startPosX + 4, startPosY + 3),  # row 4
                      simCell(startPosX, startPosY+4), simCell(startPosX+2, startPosY+4), simCell(startPosX+4, startPosY+4)]  # row 5
            alive_cells += exploder

        if pyxel.btnp(pyxel.KEY_4):  # lightweight space ship
            startPosX = 5
            startPosY = 35
            spaceShip = [simCell(startPosX+1, startPosY), simCell(startPosX+2, startPosY), simCell(startPosX+3, startPosY), simCell(startPosX+4, startPosY),  # row 1
                      simCell(startPosX, startPosY + 1), simCell(startPosX + 4, startPosY + 1),  # row 2
                      simCell(startPosX + 4, startPosY + 2), # row 3
                      simCell(startPosX, startPosY + 3), simCell(startPosX + 3, startPosY + 3)]  # row 4
            alive_cells += spaceShip

        if pyxel.btnp(pyxel.KEY_5):  # blinker
            startPosX = 50
            startPosY = 20
            blinker = [simCell(startPosX, startPosY),  # row 1
                      simCell(startPosX, startPosY + 1),  # row 2
                      simCell(startPosX, startPosY + 2)]  # row 3
            alive_cells += blinker

    def draw(self): # main loop
        global gameActive
        global alive_cells
        global test_cells
        global dead_cell_scans
        global debug
        global sim_speed
        pyxel.cls(0) # clear the screen

        # press M to activate debug, shows where dead cells are about to be revived on next tick. Originally showed all attempts to revive a dead cell.
        if debug:
            for i in dead_cell_scans:  # TESTING ONLY
                g = simCell(i[0], i[1], 9)
                g.draw()

        # draw all simCells that are alive
        for sim in alive_cells:
            sim.draw()

        # draw mouse cursor
        pyxel.pset(pyxel.mouse_x, pyxel.mouse_y, pyxel.COLOR_CYAN)

        # draw simulation status bar
        if gameActive:
            for x in range(0,50):
                pyxel.pset(x, 0, 11) # kinda green
        else:
            for x in range(0, 50):
                pyxel.pset(x, 0, 12)

        if gameActive:
            global lastupdate
            global new_pixels
            global reviving_cells
            global dying_cells

            # The following code handles all of the simulation logic. Referred to as a tick.
            if pyxel.frame_count%sim_speed == 1: # causes simulation to only update every x number of frames, otherwise it's too fast
                lastupdate = time.time()
                dead_cell_scans = [] # reset the dead cell scans
                alive_cells = alive_cells + reviving_cells # add reviving simCells to the alive simCells list
                reviving_cells = [] # remove reviving simCells from the revive list

                # kill/revive cells HERE. Any pixel adding or removing MUST happen outside the main for loop that checks for live cells
                for sim in dying_cells: # remove any simCells marked for deletion in the last cycle
                    sim.deadPixel()

                # revive dead cells if they have exactly 3 neighbors
                # we do this check only around living cells, otherwise we'd have to check the whole board
                for sim2 in alive_cells:
                    self.reprod(sim2)  # only a check

                for sim in alive_cells: # main for loop that checks living cell status
                    pixCount = getNeighborCount(sim, alive_cells)  # get surrounding pixels
                    if pixCount < 2 or pixCount > 3: # less than two or greater than 3
                        dying_cells.append(sim)  # cell dies from either over population or under population

    # code to figure out reproduction of dead cells
    def reprod(self, sim):
        global dead_cell_scans
        # scan around sim to find the cell where three other cells are alive
        NeighborCellGrid = [  # all possible neighbor positions
            [sim.x - 1, sim.y - 1],  # top left
            [sim.x, sim.y - 1],  # top
            [sim.x + 1, sim.y - 1],  # top right
            [sim.x - 1, sim.y],  # left
            [sim.x + 1, sim.y],  # right
            [sim.x - 1, sim.y + 1],  # bottom left
            [sim.x, sim.y + 1],  # bottom
            [sim.x + 1, sim.y + 1]  # bottom right
        ]
        for g in NeighborCellGrid:
            aliveSims = [[aliveSim.x, aliveSim.y] for aliveSim in alive_cells]
            if [g[0], g[1]] not in dead_cell_scans and [g[0], g[1]] not in aliveSims: # check if this dead cell has already been scanned this tick
                deadCell = simCell(g[0], g[1], alive=False, color=5)
                aliveCellNum = getNeighborCount(deadCell, alive_cells, True, test_color=11) # get number of neighbors to dead cell
                if aliveCellNum == 3: # any cell with exactly 3 live neighbors becomes a live cell
                    deadCell.alive=True
                    dead_cell_scans.append([g[0], g[1]]) # stops the code from re-checking this cell, otherwise it'll be revived multiple times
                    reviving_cells.append(deadCell) # mark the dead cell to be revived

if __name__ == '__main__':
    App()

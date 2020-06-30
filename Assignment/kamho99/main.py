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
        pyxel.init(240, 200, caption = "Binary Search visualization")
        pyxel.mouse(True)
        pyxel.cls(0)
        pyxel.run(self.update, self.draw)
        self.search_for = 0

    def check_click(self,mouse_x,mouse_y):
        """check for mouse click"""
        text_x = 55
        text_y = 45
        if text_x < mouse_x < text_x + 100 and text_y < mouse_y < text_y + 10 and App.running == False and App.finish == True:
            App.running = True
            App.finish = False
            App.search_for = (pyxel.mouse_x - 55) // 10
            App.search(App.random_list, App.search_for,len(App.random_list)//2)

    def update(self):
        """check any button click"""
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            App.check_click(self,pyxel.mouse_x, pyxel.mouse_y)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        """draw all items on screen"""
        pyxel.cls(0)
        pyxel.text(10, 10, "Binary Search", 7)
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
            if App.search_for != None:
                pyxel.text(55, 65,'search for number:{}'.format(App.search_for), 7)
                pyxel.text(55, 75, 'current node index:{}'.format(App.mid_index), 7)
                pyxel.text(55, 85, 'current node:{}'.format(App.mid_node), 7)

        list_x = 50
        list_y = 130
        for i in range(len(App.random_list)): # draw the list
            pyxel.text(list_x + 15 * i, list_y, str(App.random_list[i]), 7)
            pyxel.rectb(list_x - 3 + 15 * i, list_y - 3, 10, 10, 7)
        if App.finish == True and App.list_index != None:
            if App.list_index == 'not in list':
                pyxel.text(40, 150, 'number is not in the list', 6)
            else:
                pyxel.text(40, 150, 'your number is found at index {} of the list'.format(App.list_index), 6)

    def search(current_list, search_for, position_in_list):
        """check if the searching value is higher or lower than the mid point"""
        midpoint_index = len(current_list) // 2
        mid_var = current_list[midpoint_index]
        App.mid_index = midpoint_index
        App.mid_node = mid_var
        if search_for < mid_var:
            search_from_list = current_list[:midpoint_index]
            position_in_list -= len(search_from_list) - len(search_from_list) // 2

        elif search_for > mid_var:
            search_from_list = current_list[midpoint_index + 1:]
            position_in_list += len(search_from_list) // 2 + 1

        else:
            App.list_index = position_in_list
            App.running = False
            App.finish = True
            return

        if search_for != mid_var and len(search_from_list) > 0:
            App.search(search_from_list, search_for, position_in_list)
        else:  # if the searching number is not in the list, stop recursion
            App.list_index = 'not in list'
            App.running = False
            App.finish = True
            return

    random_list = [random.randint(0, 9) for i in range(10)]
    random_list.sort()
    running = False
    finish = True
    search_for = None
    mid_node = None
    mid_index = None
    list_index = None


if __name__ == '__main__':
    App()

import pyxel
import random


# Node class to creat a node
class Node:
    def __init__(self, value, x, y):
        self.left = None
        self.right = None
        self.value = value
        self.x = x
        self.y = y
        self.radius = 8
        self.selected = False

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_value(self):
        return self.value

    def get_radius(self):
        return self.radius

    def set_selected(self, selected):
        self.selected = selected

    def get_selected(self):
        return self.selected

    # check if clicked inside the node
    def inside(self, x, y):
        right = self.x + self.radius
        left = self.x - self.radius
        up = self.y - self.radius
        down = self.y + self.radius
        if left < x < right and up < y < down:
            return True
        else:
            return False


class App:
    def __init__(self):
        pyxel.init(256, 180, caption="Binary Tree Depth First Search Traversals")
        pyxel.mouse(True)
        pyxel.load("assets/sound_and_images.pyxres")
        pyxel.image(1).load(0, 0, "assets/game_over.png")
        pyxel.image(2).load(0, 0, "assets/winner.jpg")
        self.nodes = []
        self.mode_pre_order = False
        self.mode_in_order = False
        self.mode_post_order = False
        self.list_of_orders = []
        self.index_to_check = -1
        self.num_of_lives = 3
        self.root = None
        self.start_music_game_over = False
        self.start_music_game_won = False
        self.generate_tree()

        pyxel.sound(6).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )

        pyxel.sound(7).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )

        pyxel.run(self.update, self.draw)

    def generate_tree(self):
        self.nodes.clear()

        # tree level 1 (root)
        n1 = Node(random.randint(45, 55), 128, 30)
        self.root = n1

        # tree level 2
        n2 = Node(random.randint(30, 34), 70, 65)
        n3 = Node(random.randint(71, 75), 186, 65)

        # tree level 3
        n4 = Node(random.randint(20, 26), 35, 100)
        n5 = Node(random.randint(39, 41), 100, 100)
        n6 = Node(random.randint(61, 65), 155, 100)
        n7 = Node(random.randint(86, 90), 220, 100)

        # tree level 4
        n8 = Node(random.randint(10, 19), 20, 135)
        n9 = Node(random.randint(27, 29), 50, 135)
        n10 = Node(random.randint(35, 38), 85, 135)
        n11 = Node(random.randint(42, 44), 115, 135)
        n12 = Node(random.randint(56, 60), 140, 135)
        n13 = Node(random.randint(66, 70), 170, 135)
        n14 = Node(random.randint(76, 85), 205, 135)
        n15 = Node(random.randint(91, 99), 235, 135)

        # always have nodes n1, n2, n3
        n1.set_left(n2)
        n1.set_right(n3)
        self.nodes.append(n1)
        self.nodes.append(n2)
        self.nodes.append(n3)

        # randomly decide about n4 (and n8 and n9)
        if self.add_child():
            n2.set_left(n4)
            self.nodes.append(n4)

            if self.add_child():
                n4.set_left(n8)
                self.nodes.append(n8)

            if self.add_child():
                n4.set_right(n9)
                self.nodes.append(n9)

        # randomly decide about n5 (and n10 and n11)
        if self.add_child():
            n2.set_right(n5)
            self.nodes.append(n5)

            if self.add_child():
                n5.set_left(n10)
                self.nodes.append(n10)

            if self.add_child():
                n5.set_right(n11)
                self.nodes.append(n11)

        # randomly decide about n6 (and n12 and n13)
        if self.add_child():
            n3.set_left(n6)
            self.nodes.append(n6)

            if self.add_child():
                n6.set_left(n12)
                self.nodes.append(n12)

            if self.add_child():
                n6.set_right(n13)
                self.nodes.append(n13)

        # randomly decide about n7 (and n14 and n15)
        if self.add_child():
            n3.set_right(n7)
            self.nodes.append(n7)

            if self.add_child():
                n7.set_left(n14)
                self.nodes.append(n14)

            if self.add_child():
                n7.set_right(n15)
                self.nodes.append(n15)

    # randomly decide if to add child or not
    def add_child(self):
        if random.randint(1, 10) <= 8:   # 80% yes, 20% no
            return True
        else:
            return False

    # reset the tree for a new game
    def reset(self):
        self.list_of_orders.clear()
        self.index_to_check = 0
        self.num_of_lives = 3
        for node in self.nodes:
            node.set_selected(False)

    def update(self):
        # checking if need to start game over music
        if self.start_music_game_over:
            pyxel.play(0, 6)
            self.start_music_game_over = False

        # checking if need to start game won music
        if self.start_music_game_won:
            pyxel.play(0, 7)
            self.start_music_game_won = False

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            x = pyxel.mouse_x
            y = pyxel.mouse_y

            # clicked generate tree button
            if x < 64 and y < 15:
                self.reset()
                self.index_to_check = -1
                self.mode_pre_order = False
                self.mode_post_order = False
                self.mode_in_order = False
                self.generate_tree()
                pyxel.play(0, 1)

            # clicked pre-order button
            elif 64 <= x < 128 and y < 15:
                self.reset()
                self.mode_pre_order = True
                self.mode_post_order = False
                self.mode_in_order = False
                self.pre_order(self.root)
                pyxel.play(0, 3)

            # clicked in-order button
            elif 128 <= x < 192 and y < 15:
                self.reset()
                self.mode_in_order = True
                self.mode_post_order = False
                self.mode_pre_order = False
                self.in_order(self.root)
                pyxel.play(0, 3)

            # clicked post-order button
            elif 192 <= x and y < 15:
                self.reset()
                self.mode_post_order = True
                self.mode_pre_order = False
                self.mode_in_order = False
                self.post_order(self.root)
                pyxel.play(0, 3)

            # check if clicked on a node
            for node in self.nodes:
                if node.inside(x, y) and len(self.list_of_orders) != 0 and self.index_to_check < len(self.list_of_orders):

                    # check if correct node
                    if node == self.list_of_orders[self.index_to_check]:
                        node.set_selected(True)
                        self.index_to_check += 1
                        pyxel.play(0, 4)

                        # check if this was the last node needed
                        if self.index_to_check >= len(self.list_of_orders):
                            self.start_music_game_won = True

                    # else wrong node
                    else:
                        pyxel.play(0, 0)
                        self.num_of_lives -= 1

                        # check if this was the last live
                        if self.num_of_lives == 0:
                            self.start_music_game_over = True

    def draw(self):
        pyxel.cls(7)

        # draw the navigation menu (generate new tree)
        pyxel.rectb(0, 0, 64, 15, 12)
        pyxel.text(16, 5, "New Tree", 12)

        # draw the navigation menu (traversal options)
        if self.mode_pre_order:
            pyxel.rect(64, 0, 64, 15, 8)
            pyxel.text(78, 5, "Pre-order", 7)
        else:
            pyxel.rectb(64, 0, 64, 15, 8)
            pyxel.text(78, 5, "Pre-order", 8)

        if self.mode_in_order:
            pyxel.rect(128, 0, 64, 15, 8)
            pyxel.text(143, 5, "In-order", 7)
        else:
            pyxel.rectb(128, 0, 64, 15, 8)
            pyxel.text(143, 5, "In-order", 8)

        if self.mode_post_order:
            pyxel.rect(192, 0, 64, 15, 8)
            pyxel.text(205, 5, "Post-order", 7)
        else:
            pyxel.rectb(192, 0, 64, 15, 8)
            pyxel.text(205, 5, "Post-order", 8)

        # checking if game over
        if self.num_of_lives <= 0:
            # game over
            pyxel.blt(78, 50, 1, 0, 0, 100, 53)

        elif self.index_to_check == len(self.list_of_orders):
            # game won
            pyxel.blt(78, 50, 2, 0, 0, 100, 75)

        else:
            # print instructions
            if self.mode_in_order or self.mode_post_order or self.mode_pre_order:
                pyxel.text(5, 20, "Click on the nodes", 8)
                pyxel.text(5, 30, "in the correct order ", 8)
            else:
                pyxel.text(5, 20, "Select one of the tree", 8)
                pyxel.text(5, 30, "traversal options above", 8)

            # draw lives remaining
            pyxel.text(190, 20, "Lives remaining: ", 8)
            for i in range(self.num_of_lives):
                pyxel.blt(200 + i * 18, 30, 0, 0, 0, 20, 20, 0)

            # drawing the tree
            for node in self.nodes:

                # draw the line to the left child
                if node.get_left() is not None:
                    left_child = node.get_left()
                    pyxel.line(node.get_x(), node.get_y(), left_child.get_x(), left_child.get_y(), 8)

                # draw the line to the right child
                if node.get_right() is not None:
                    right_child = node.get_right()
                    pyxel.line(node.get_x(), node.get_y(), right_child.get_x(), right_child.get_y(), 8)

                # draw the node
                if node.get_selected():
                    pyxel.circ(node.get_x(), node.get_y(), node.get_radius(), 8)
                    pyxel.text(node.get_x() - 3, node.get_y() - 2, str(node.get_value()), 7)
                else:
                    pyxel.circ(node.get_x(), node.get_y(), node.get_radius(), 7)
                    pyxel.circb(node.get_x(), node.get_y(), node.get_radius(), 8)
                    pyxel.text(node.get_x() - 3, node.get_y() - 2, str(node.get_value()), 8)

            # Line at the bottom to print the text inside
            pyxel.line(0, 160, 256, 160, 8)

            #  print the node order at the bottom when they have been selected
            x = 5
            y = 168
            for n in self.list_of_orders:
                if n.get_selected():
                    pyxel.text(x, y, str(n.get_value()), 8)
                    x += 15

    # find out the pre-order
    def pre_order(self, node):
        if node is not None:
            self.list_of_orders.append(node)
            self.pre_order(node.get_left())
            self.pre_order(node.get_right())

    # find out the post-order
    def post_order(self, node):
        if node is not None:
            self.post_order(node.get_left())
            self.post_order(node.get_right())
            self.list_of_orders.append(node)

    # find out the in-order
    def in_order(self, node):
        if node is not None:
            self.in_order(node.get_left())
            self.list_of_orders.append(node)
            self.in_order(node.get_right())


App()


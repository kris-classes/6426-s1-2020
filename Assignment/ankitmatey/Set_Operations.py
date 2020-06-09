import random
import pyxel


class randomsets:

    def __init__(self):
        self.s1 = {random.randint(1, 15) for i in range(8)}
        self.s2 = {random.randint(1, 15) for i in range(8)}

    def __repr__(self):
        return repr([(self.s1),(self.s2)])

    def __str__(self):
        return str([(self.s1),(self.s2)])

    def union(self):        #union of the 2 random sets
        self.union_set = set()
        for i in self.s1:
            self.union_set.add(i)
        for j in self.s2:
            self.union_set.add(j)
        return self.union_set

    def intersection(self):     #intersection of the 2 random sets
        self.common_values = set()
        for i in self.s1:
            if i in self.s2:
                self.common_values.add(i)
        return self.common_values

    def difference(self):       # difference between 2 random sets a-b
        self.a = self.s1.copy()
        self.common_numbers = self.intersection()
        self.diff = set()
        for i in self.a:
            if i not in self.common_numbers:
                self.diff.add(i)
        return self.diff

    def symm_diff(self): #symmetric difference between 2 random sets except common all the elements
        self.full_set = self.union()
        self.common_set = self.intersection()
        self.unique_values = set()
        for i in self.full_set:
            if i not in self.common_set:
                self.unique_values.add(i)
        return self.unique_values


class App:

    def __init__(self):
        pyxel.init(250, 170, caption="SET OPERATIONS")
        self.head = "Random Sets Operations"
        self.op1 = ">>> Press [N] to generate 2 new random Set"
        self.op2 = ">>> Press [U] to see the Union"
        self.op3 = ">>> Press [I] to see the Intersection"
        self.op4 = ">>> Press [D] to see the Difference"
        self.op5 = ">>> Press [S] to see the Symmetric Difference"
        self.sets = randomsets()
        self.uni = self.sets.union()
        self.inter = self.sets.intersection()
        self.diff = self.sets.difference()
        self.symmdiff = self.sets.symm_diff()
        self.u = 0
        self.i = 0
        self.d = 0
        self.s = 0


        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_N):
            self.sets = randomsets()
            self.uni = self.sets.union()
            self.inter = self.sets.intersection()
            self.diff = self.sets.difference()
            self.symmdiff = self.sets.symm_diff()
            self.u = 0
            self.i = 0
            self.d = 0
            self.s = 0
        if pyxel.btnp(pyxel.KEY_U):
            self.u = 3
        if pyxel.btnp(pyxel.KEY_I):
            self.i = 5
        if pyxel.btnp(pyxel.KEY_D):
            self.d = 6
        if pyxel.btnp(pyxel.KEY_S):
            self.s = 8

    def draw(self):

        pyxel.cls(0)
        pyxel.text(75, 1, self.head, 12)
        pyxel.text(5, 10, self.op1, 11)
        pyxel.text(5, 20, self.op2, 3)
        pyxel.text(5, 30, self.op3, 5)
        pyxel.text(5, 40, self.op4, 6)
        pyxel.text(5, 50, self.op5, 8)
        pyxel.text(5, 60, "A,B = ", 14)
        pyxel.text(25, 60, str(self.sets), 14)
        pyxel.rectb(5, 70, 235, 20, 2)
        pyxel.text(10, 75, "A U B = ", 2)
        pyxel.text(40, 75, str(self.uni), self.u)
        pyxel.rectb(5, 95, 235, 20, 8)
        pyxel.text(10, 100, "A ∩ B = ", 8)
        pyxel.text(40, 100, str(self.inter), self.i)
        pyxel.rectb(5, 120, 235, 20, 6)
        pyxel.text(10, 125, "A - B = ", 6)
        pyxel.text(40, 125, str(self.diff), self.d)
        pyxel.rectb(5, 145, 235, 20, 10)
        pyxel.text(10, 150, "A ∆ B = ", 10)
        pyxel.text(40, 150, str(self.symmdiff), self.s)




App()
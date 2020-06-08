import random
import pyxel


class randomsets:
    def __init__(self):
        self.s1 = {random.randint(1, 1000) for i in range(19)}
        self.s2 = {random.randint(1, 1000) for i in range(19)}
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


r = randomsets()
r
print(r)
r.union()
r.intersection()
r.difference()
r.symm_diff()

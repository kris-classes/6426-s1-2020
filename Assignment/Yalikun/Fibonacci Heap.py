import math



class FibonacciHeapNode:
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority
        self.parent = None
        self.left = self
        self.right = self
        self.child = None
        self.degree = 0
        self.marked = False







class FibonacciHeap:
    LOG_PHI = math.log((1 + math.sqrt(5)) / 2)

    def __init__(self):
        self.minimum_node = None
        self.array = []
        self.map = dict()



    def __len__(self):
        return len(self.map)


    def add(self, element, priority):
        if element in self.map:
            return False

        node = FibonacciHeapNode(element, priority)

        if self.minimum_node:
            node.left = self.minimum_node
            node.right = self.minimum_node.right
            self.minimum_node.right = node
            node.right.left = node

            if priority < self.minimum_node.priority:
                self.minimum_node = node
        else:
            self.minimum_node = node

        self.map[element] = node
        return True


    def decrease_key(self, element, priority):
        target_node = self.map[element]

        if not target_node:
            return False

        if target_node.priority <= priority:
            return False

        target_node.priority = priority
        y = target_node.parent
        x = target_node

        if y and x.priority < y.priority:
            self.cut(x, y)
            self.cascading_cut(y)

        if self.minimum_node.priority > x.priority:
            self.minimum_node = x

        return True


    def extract_minimum(self):
        if len(self.map) == 0:
            raise ValueError("Extracting from empty Fibonacci heap")

        z = self.minimum_node
        number_of_children = z.degree
        x = z.child
        tmp_right = None

        while number_of_children:
            tmp_right = x.right

            x.left.right = x.right
            x.right.left = x.left

            x.left = self.minimum_node
            x.right = self.minimum_node.right
            self.minimum_node.right = x
            x.right.left = x

            x.parent = None
            x = tmp_right
            number_of_children -= 1

        z.left.right = z.right
        z.right.left = z.left

        if z == z.right:
            self.minimum_node = None
        else:
            self.minimum_node = z.right
            self.consolidate()

        element = z.element
        del self.map[element]
        return element


    def wipe_array(self):
        for i in range(len(self.array)):
            self.array[i] = None


    def consolidate(self):
        array_size = math.floor(math.log(len(self.map)) / self.LOG_PHI) + 1
        self.wipe_array()
        self.ensure_array_size(array_size)
        x = self.minimum_node
        root_list_size = 0

        if x:
            root_list_size = 1
            x = x.right

            while x != self.minimum_node:
                root_list_size += 1
                x = x.right

        while root_list_size:
            degree = x.degree
            next = x.right

            while self.array[degree]:
                y = self.array[degree]

                if x.priority > y.priority:
                    tmp = y
                    y = x
                    x = tmp

                self.link(y, x)
                self.array[degree] = None
                degree += 1

            self.array[degree] = x
            x = next
            root_list_size -= 1

        self.minimum_node = None

        for y in self.array:
            if y:
                if not self.minimum_node:
                    self.minimum_node = y
                else:
                    self.move_to_root_list(y)


    def move_to_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

        node.left = self.minimum_node
        node.right = self.minimum_node.right
        self.minimum_node.right = node
        node.right.left = node

        if self.minimum_node.priority > node.priority:
            self.minimum_node = node


    def link(self, y, x):
        y.left.right = y.right
        y.right.left = y.left

        y.parent = x

        if not x.child:
            x.child = y
            y.right = y
            y.left = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right = y
            y.right.left = y

        x.degree += 1


    def cut(self, x, y):
        x.left.right = x.right
        x.right.left = x.left
        y.degree -= 1

        if y.child == x:
            y.child = x.right

        if y.degree == 0:
            y.child = None

        x.left = self.minimum_node
        x.right = self.minimum_node.right
        self.minimum_node.right = x
        x.right.left = x

        x.parent = None
        x.marked = False


    def cascading_cut(self, y):
        z = y.parent

        if z:
            if not y.marked:
                y.marked = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)


    def ensure_array_size(self, array_size):
        while len(self.array) < array_size:
            self.array.append(None)





def main():
    heap = FibonacciHeap()

    for i in range(10):
        heap.add(i, 10 - i)

    heap.decrease_key(5, 15)
    heap.decrease_key(4, -1)

    while heap:
        print(heap.extract_minimum())


if __name__ == "__main__":
    main()




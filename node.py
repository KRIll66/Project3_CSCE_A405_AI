class Node:

    def __init__(self, parent, c0, c1, c2, c3, c4, c5):
        self.parent = parent
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5

    def __init__(self, parent):
        self.parent = parent
        self.c0 = None
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.c5 = None

    def set_parent(self, parent):
        self.parent = parent

    def set_c1(self, c1):
        self.c1 = c1

    def set_c2(self, c2):
        self.c2 = c2

    def set_c3(self, c3):
        self.c3 = c3

    def set_c4(self, c4):
        self.c4 = c4

    def set_c5(self, c5):
        self.c5 = c5

    def get_parent(self):
        return self.parent

    def get_c1(self):
        return self.c1

    def get_c2(self):
        return self.c2

    def get_c3(self):
        return self.c3

    def get_c4(self):
        return self.c4

    def get_c5(self):
        return self.c5




from potatoTokens import *


class Parser:
    def __init__(self, i: tuple):
        self.p1: tuple = i
        self.p2: int = 0
        self.p3 = False

    def next(self):
        if self.p2 < len(self.p1):
            self.p3 = self.p1[self.p2]
            self.p2 += 1
        else:
            self.p3 = False

    def potato(self):
        return self.p1

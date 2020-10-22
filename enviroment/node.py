import random
from enum import Enum


class Node:
    def __init__(self, coefficient_left=None, coefficient_top=None, coefficient_right=None, coefficient_down=None):
        pass


class Edge:
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.is_closed = None
        self.update()

    def update(self):
        if self.coefficient > random.random():
            self.is_closed = False
        else:
            self.is_closed = True


# use this in Node to somehow
class Direction(Enum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    DOWN = 3

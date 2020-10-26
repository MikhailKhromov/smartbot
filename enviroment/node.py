import random
from enum import Enum
import config


class Node:
    def __init__(self, coefficient, x, y):
        self.x = x
        self.y = y
        self.coefficient = coefficient
        self.LEFT = False
        self.TOP = False
        self.RIGHT = False
        self.BOTTOM = False
        if y != 0:
            self.LEFT = self.true_or_false()
        if x != 0:
            self.TOP = self.true_or_false()
        if y != config.WIDTH - 1:
            self.RIGHT = self.true_or_false()
        if x != config.HEIGHT - 1:
            self.BOTTOM = self.true_or_false()

    def true_or_false(self):
        if self.coefficient > random.random():
            return False
        return True

    def __repr__(self):
        return str(self.LEFT) + " " + str(self.TOP) + " " + str(self.RIGHT) + " " + str(self.BOTTOM)

    def __str__(self):
        return str(self.LEFT) + " " + str(self.TOP) + " " + str(self.RIGHT) + " " + str(self.BOTTOM)


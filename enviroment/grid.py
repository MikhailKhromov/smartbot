from .node import Node
import random


class Grid:
    def __init__(self, height, width, ):
        self.height = height
        self.width = width
        self.node_list = [[Node(self.get_random_coeff(i, j)) for j in range(width)] for i in range(height)]
        node_amount = width * height
        # matrix of the whole grid, 1 = can go through, -1 = can't
        # TODO: redo this, because this is not efficient, since there may be only up to 4 "ones" in a whole row
        self.matrix = [[0 for j in range(4)] for i in range(node_amount)]

    def get_random_coeff(self, i, j):
        # TODO: use seeding or something with those 2 values
        return random.random()


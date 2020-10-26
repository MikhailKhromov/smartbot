from .node import Node
import random


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = None

    def get_random_coeff(self, i, j):
        # TODO: use seeding or something with those 2 values
        return random.random()

    def generate_matrix(self):
        self.matrix = [[Node(self.get_random_coeff(i, j), i, j) for j in range(self.width)] for i in range(self.height)]

    def check_path(self, coords_from, coords_to):
        pass
        # Tries to find path from coords_from to coords_to
        # dfs or something



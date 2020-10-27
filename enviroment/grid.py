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

    def convert_coords_to_id(self, coords):
        return coords[0] * self.width + coords[1]

    def check_path(self, coords_from, coords_to):
        items = []
        def update_items():
            if self.matrix[curr_coords[0]][curr_coords[1]].LEFT:
                if visited.count((curr_coords[0], curr_coords[1] - 1)) == 0:
                    items.append((curr_coords[0], curr_coords[1] - 1))
            if self.matrix[curr_coords[0]][curr_coords[1]].TOP:
                if visited.count((curr_coords[0] - 1, curr_coords[1])) == 0:
                    items.append((curr_coords[0] - 1, curr_coords[1]))
            if self.matrix[curr_coords[0]][curr_coords[1]].RIGHT:
                if visited.count((curr_coords[0], curr_coords[1] + 1)) == 0:
                    items.append((curr_coords[0], curr_coords[1] + 1))
            if self.matrix[curr_coords[0]][curr_coords[1]].BOTTOM:
                if visited.count((curr_coords[0] + 1, curr_coords[1])) == 0:
                    items.append((curr_coords[0] + 1, curr_coords[1]))

        dfs_nodes = [-1 for _ in range(self.width * self.height)]
        dfs_nodes[self.convert_coords_to_id(coords_from)] = 1
        # TODO: fix a bug, place where we start at isnt visited by default
        visited = []
        curr_coords = coords_from
        update_items()
        while len(items) != 0:
            coords_to_check = items.pop()
            curr_coords = coords_to_check
            visited.append(coords_to_check)
            dfs_nodes[self.convert_coords_to_id(coords_to_check)] = 1
            update_items()
        if dfs_nodes[self.convert_coords_to_id(coords_to)] == 1:
            return True
        return False



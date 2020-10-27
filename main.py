from enviroment.grid import Grid
import config

grid = Grid(config.HEIGHT, config.WIDTH)
print("starting")
grid.generate_matrix()
while not grid.check_path(config.COORDS_FROM, config.COORDS_TO):
    # TODO: fix the matrix, not redo it, since with big numbers it just dies
    print("trying again")
    grid.generate_matrix()
print(grid.matrix)




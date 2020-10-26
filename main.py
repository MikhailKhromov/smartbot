from enviroment.grid import Grid
import config

grid = Grid(config.HEIGHT, config.WIDTH)
while not grid.check_path(config.COORDS_FROM, config.COORDS_TO):
    grid.generate_matrix()
print(grid.matrix)


# a = [(35000 if (usl or usl2) else -10000) for i in range(amount)]


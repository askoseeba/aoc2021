import aocutils as aoc
import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

fname = 'test-input.txt'
fname = 'input.txt'

data = np.array(aoc.load_2D(fname, symbols_to_int = True))

def find_path(cave):
    grid       = Grid(matrix = cave)
    start      = grid.node(0, 0)
    end        = grid.node(len(cave) - 1, len(cave[0]) - 1)
    finder     = DijkstraFinder()
    path, runs = finder.find_path(start, end, grid)
    return path

path = find_path(data)
print('Part 1:', sum([data[loc[1]][loc[0]] for loc in path]) - data[0][0])

for tile_row in range(5):
    for tile_col in range(5):
        tile = (data + tile_row + tile_col - 1) % 9 + 1
        row = tile if tile_col == 0 else np.append(row, tile, axis = 1)
    cave = row if tile_row == 0 else np.append(cave, row, axis = 0)
path = find_path(cave)
print('Part 2:', sum([cave[loc[1]][loc[0]] for loc in path]) - cave[0][0])

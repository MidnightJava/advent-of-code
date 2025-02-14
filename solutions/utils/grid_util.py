import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.vectors import IntVector2

def grid_walk(grid: list[list]):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield IntVector2(x, y)

def grid_walk_val(grid: list[list]):
    for pos in grid_walk(grid):
        yield pos, pos.of_grid(grid)
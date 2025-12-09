# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from ...base import StrSplitSolution, answer
from ...utils.graphs import neighbors, parse_grid, Direction, GridPoint, add_points
from collections import Counter
import json

""" PART 1

You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location
marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam
encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the
immediate right of the splitter.

How many times will the beam be split?
"""

""" PART 2

With a quantum tachyon manifold, only a single tachyon particle is sent through the manifold. A tachyon particle takes both
the left and right path of each splitter encountered.

Since this is impossible, the manual recommends the many-worlds interpretation of quantum tachyon splitting: each time a
particle reaches a splitter, it's actually time itself which splits. In one timeline, the particle went left, and in the
other timeline, the particle went right.

In total, how many different timelines would a single tachyon particle end up on?
"""

class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    def move(self):
        moved = False
        for row in range(self.h):
            for col in range(self.w):
                if self.grid[(row,col)] == 'S': self.start = (row,col)
                if self.grid[(row,col)] in 'S|':
                    nxt = add_points((row, col), Direction.offset(Direction.DOWN))
                    if nxt in self.grid:
                        if self.grid[nxt] == '.':
                            self.grid[nxt] = '|'
                            moved = True
                        elif self.grid[nxt] == '^' and nxt not in self.visited_splitters:
                            self.visited_splitters.add(nxt)
                            for nbr in neighbors(nxt,4,max_x_size=self.w, max_y_size=self.h,diagonals=True):
                                split = False
                                if nbr[0] > nxt[0]:
                                    self.grid[nbr] = '|'
                                    split = True
                                    moved = True
                            if split: self.count += 1
        return not moved                    

    @answer(1518)
    def part_1(self) -> int:
        self.grid = parse_grid(self.input)
        self.w = len(self.input[0])
        self.h = len(self.input)
        self.count = 0
        self.visited_splitters = set()
        done = False
        while not done:
            done = self.move()
        return self.count

    def print_grid(self):
        for row in range(self.h):
            for col in range(self.w):
                print(f"{(row,col)}: {self.grid[(row, col)]}")

    
    @answer(25489586715621)
    def part_2(self,) -> int:
        # Pascal's Triangle solution, copied from the reddit thread
        paths = Counter()
        for line in self.input:
            for (i, c) in enumerate(line.strip()):
                match c:
                    case 'S':
                        paths[i] = 1
                    case '^':
                        if i in paths:
                            paths[i-1] += paths[i]
                            paths[i+1] += paths[i]
                            del paths[i]

        return paths.total()

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

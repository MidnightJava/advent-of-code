# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer
from ...utils.graphs import neighbors, parse_grid, Direction, GridPoint, add_points
from ...utils.transformations import parse_ints
import re

""" PART 1

The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the
square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles
for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?
"""

""" PART 2

The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the
first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the
same column.

In addition, all of the tiles inside this loop of red and green tiles are also green. The rectangle you choose still must have red tiles
in opposite corners, but any other tiles it includes must now be red or green. Using two red tiles as opposite corners, what is the largest
area of any rectangle you can make using only red and green tiles?
"""


class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    # @answer(1234)
    def part_1(self) -> int:
        pts = []
        for line in self.input:
            pts.append(tuple([ i for i in parse_ints(re.findall(r"\d+", line))]))
        max_area = 0
        for i in range(len(pts)):
            for j in range(len(pts)):
                if i == j: continue
                area = abs(pts[i][0] - pts[j][0] + 1) * abs(pts[i][1] - pts[j][1] + 1)
                if area > max_area:
                    max_area = area
        return max_area


    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

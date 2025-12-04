# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from ...base import StrSplitSolution, answer
from ...utils.graphs import Grid, GridPoint, neighbors, parse_grid


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    @answer(1537)
    def part_1(self) -> int:
        """
        The rolls of paper (@) are arranged on a large grid. The forklifts can only access a roll of paper if there are
        fewer than four rolls of paper in the eight adjacent positions. How many rolls of paper can be accessed by a forklift?
        """
        count = 0
        grid = parse_grid(self.input)
        for pnt in grid.keys():
            if grid[pnt] != '@': continue
            nbs = neighbors(
                pnt,
                num_directions=8,
                max_x_size=len(self.input[0]) - 1,
                max_y_size=len(self.input) - 1,
            )
            rolls = 0
            for nb in nbs:
                if grid[nb] == '@': rolls += 1
            if rolls < 4:
                count += 1
        return count
    
    @answer(8707)
    def part_2(self) -> int:
        """
        Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts
        might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper
        could the Elves remove if they keep repeating this process?
        """
        count = 0
        grid = parse_grid(self.input)
        while True:
            removed = False
            for pnt in grid.keys():
                if grid[pnt] != '@': continue
                nbs = neighbors(
                    pnt,
                    num_directions=8,
                    max_x_size=len(self.input[0]) - 1,
                    max_y_size=len(self.input) - 1,
                )
                rolls = 0
                for nb in nbs:
                    if grid[nb] == '@': rolls += 1
                if rolls < 4:
                    count += 1
                    grid[pnt] = '#'
                    removed = True
            if not removed: break
        return count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13

from ...base import StrSplitSolution, answer
from itertools import islice, product
import re
from ...utils.transformations import parse_ints
from pathlib import Path

part_two_increase = 10000000000000


class Solution(StrSplitSolution):
    _year = 2024
    _day = 13
    separator = "\n\n"
    
    def _solve(
      self, a_x: int, a_y: int, b_x: int, b_y: int, x_prize: int, y_prize: int
    ) -> tuple[float, float]:
          """
          this solves:
          - a_x * a + b_x * b = x_prize
          - a_y * a + b_y * b = y_prize
          """

          # multiply out b_y and b_x (the coefficients of B for the other equation)
          a_x_with_b_y = a_x * b_y
          x_prize_with_b_y = x_prize * b_y

          a_y_with_b_x = a_y * b_x
          y_prize_with_b_x = y_prize * b_x

          a = (x_prize_with_b_y - y_prize_with_b_x) / (a_x_with_b_y - a_y_with_b_x)

          b = (y_prize - a_y * a) / b_y

          return a, b

    @answer(29877)
    def part_1(self) -> int:
      # Brute force solution:
      # For each machine, consider as coefficients all permutations of 1 through 100 taken 2 at a time.
      # Keep the pair that repreaents the lowest token usage.
      total = 0
      for block in self.input:
        vals =  parse_ints(re.findall(r"\d+", block))
        perms = product(range(100), repeat=2)
        scores = []
        for perm in perms:
          x = vals[0] * perm[0] + vals[2] * perm[1]
          y = vals[1] * perm[0] + vals[3] * perm[1]
          if (x,y) == (vals[4], vals[5]):
            score = 3 * perm[0] + perm[1]
            scores.append(score)
        if len(scores): total += min(scores)
      return total
    """
    Part 2 solution copied from https://github.com/xavdid/advent-of-code/blob/main/solutions/2024/day_13/solution.py
    """
    @answer(99423413811305)
    def part_2(self) -> int:
        total = 0
        for block in self.input:
          vals = parse_ints(re.findall(r"\d+", block))
          vals[4] += part_two_increase
          vals[5] += part_two_increase
          sol = self._solve(*vals)
          if sol[0].is_integer() and sol[1].is_integer():
            total += (3 * sol[0] + sol[1])
        return int(total)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

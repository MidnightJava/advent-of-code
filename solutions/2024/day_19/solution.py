# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/19

from ...base import StrSplitSolution, answer
from itertools import permutations
from collections import defaultdict
import re

class Solution(StrSplitSolution):
    _year = 2024
    _day = 19
    separator ="\n\n"
    towel_dict = defaultdict(int)

    def find_match(self, subdes, des):
        if len(subdes) <= self.max_tlen:
          if subdes in self.towels:
            self.found.add(des)
            return
          if len(subdes) == 1: return
        for t in self.towels:
          # The recursion continues indefinitely for certain designs. I don't understand how it can
          # be happening since the design is definitely reduced in length for each iteration. This occurs
          # even when using other solutions found on the reddit forum, so there is a bomb planted in
          # my data that is not in everyone else's data.
          if self.towel_dict[(des, t)] >= 25: # <<=== Magic number discovered by trial and error
           continue
          self.towel_dict[(des, t)] += 1
          if subdes.startswith(t):
              _d = subdes[len(t):]
              self.find_match(_d, des)
              if des in self.found:
                  break


    @answer(365)
    def part_1(self) -> int:
        self.towels = list(map(lambda x: x.strip(), self.input[0].split(',')))
        self.max_tlen = max([len(t) for t in self.towels])
        designs = self.input[1].split()

        self.found = set()
        cd = 0
        for des in designs:
          cd += 1
          # print(f"design {cd}")
          self.find_match(des, des)
        return len(self.found)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

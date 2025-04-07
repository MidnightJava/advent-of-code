# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/19

from ...base import StrSplitSolution, answer
from collections import defaultdict

class Solution(StrSplitSolution):
    _year = 2024
    _day = 19
    separator ="\n\n"
    towel_dict = defaultdict(int)
                
    def find_matches(self, subdes, des):
      if len(subdes) == 0:
         return 1
      if subdes in self.match_cache:
         return self.match_cache[subdes]
      matches = 0
      for t in self.towels:
        if subdes.startswith(t):
          matches += self.find_matches( subdes[len(t):], des)
      self.match_cache[subdes] = matches
      return matches
    
    @answer(365)
    def part_1(self) -> int:
        self.towels = list(map(lambda x: x.strip(), self.input[0].split(',')))
        self.max_tlen = max([len(t) for t in self.towels])
        self.designs = self.input[1].split()
        self.match_cache = {}
        count_1 = 0
        self.count_2 = 0
        for des in self.designs:
          res = self.find_matches(des, des)
          count_1 +=  1 if res else 0
          self.count_2 += res
        return count_1

    @answer(730121486795169)
    def part_2(self) -> int:
      return self.count_2
     
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

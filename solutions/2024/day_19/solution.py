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
    c0 = 0
    c1 = 0
    towel_dict = defaultdict(int)
    towel_path_dict = defaultdict(list)

    def find_match(self, d, des, path, towel):
        # print(f"towel {towel}")
        # print(len(d))
        # print(d, des)
        if len(d) < self.max_tlen:
          if d in self.towels:
            self.found.add(des)
            return True
        if des in self.found: return
        if len(d) == 0:
            self.found.add(des)
            # print(f"found {des} path: {path}")
            return True
        elif len(d) == 1:
          # for t in self.towels:
          #   if d == t:
          #     self.found.add(des)
          #     break
          if d in self.towels:
             self.found.add(des)
             return True
          # self.found.add(des)# <== wrong, but needed to make the recursion close
          return
        found = False
        ct = 0
        towel_path = []
        for t in self.towels:
          if t == towel:
             continue
          if self.towel_dict[(des, t)] >= 25:
           continue
          self.towel_dict[(des, t)] += 1
          # self.towel_path_dict[des].append(t)
          # towel_path.append(t)
          # if self.towel_path_dict[des] == towel_path:
          #    continue
          ct += 1
          # print(f"l: {l}   t: {ct}")
          if found: break
          if d.startswith(t) and des not in self.found:
              # print(f"d {d};   t {t}")
              _d = d[len(t):]
              if not len(_d) < len(d):
                 print("TOWEL FAULT")
              if self.find_match(_d, des, path + [_d], t):
                 break
              if des in self.found:
                  found = True
                  break


    # @answer(365)
    def part_1(self) -> int:
        self.towels = list(map(lambda x: x.strip(), self.input[0].split(',')))
        self.max_tlen = max([len(t) for t in self.towels])
        self.min_tlen = min([len(t) for t in self.towels])
        designs = self.input[1].split()

        self.found = set()
        cd = 0
        for d in designs:
          cd += 1
          print(f"design {cd}")
          if cd  in [8,39,67, 81, 86, 92, 95, 118, 127, 128, 146, 178, 184, 189, 200, 228, 235, 240, 242, 249, 252, 285,291, 298, 299, 304, 305, 341, 346, 375, 390, 391, 393, 395, 396]:
            # continue
            pass
          self.find_match(d, d, [], '')
        print(self.c0, self.c1)
        # print(self.found)
        # for f in self.found:
        #     print(f)
        return len(self.found)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

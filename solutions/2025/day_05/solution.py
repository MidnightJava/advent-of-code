# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2025
    _day = 5
    separator = "\n\n"

    def merge_fresh_ids(self, new_range: list[int]) -> None:
        i = 0
        while i < len(self.fresh_list):
            r = self.fresh_list[i]
            if not (new_range[1] < r[0] or new_range[0] > r[1]):
                new_range = [min(new_range[0], r[0]),
                             max(new_range[1], r[1])]
                self.fresh_list.pop(i)
                continue
            i += 1
        self.fresh_list.append(new_range)

    @answer(661)
    def part_1(self) -> int:
        self.fresh_ids = self.input[0]
        self.avail_ids = self.input[1]
        self.fresh_list = []

        for id in self.fresh_ids.splitlines():
            m = re.match(r"(\d+)-(\d+)", id)
            if m:
                l = [int(m.group(1)), int(m.group(2))]
                self.merge_fresh_ids(l)
            else:
                print("No match")
        
        fresh = 0
        for id in self.avail_ids.splitlines():
            found = False
            for l in self.fresh_list:
                if found:
                    break
                if int(id) >= l[0] and int(id) <= l[1]:
                    fresh+= 1
                    found = True
                    break

        return fresh
        
    @answer(359526404143208)
    def part_2(self) -> int:
        count = 0
        for l in self.fresh_list:
            count += (l[1] - l[0]+1)
        return count

    # Part 2 X < 362982296500252
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

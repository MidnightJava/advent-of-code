# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer
import re

""" PART 1

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line,
and a list of available ingredient IDs. For example:

    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges
can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh.
"""

""" PART 2

the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh.
An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant.
"""

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

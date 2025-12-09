# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer
import re
""" PART 1

Input is product ID ranges separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice),
6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges.
"""

""" PART 2

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times),
123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
"""
class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ","

    def is_invalid(self, n):
        if len(str(n)) % 2 != 0: return False
        idx = int(len(str(n)) / 2)
        if str(n)[:idx] == str(n)[idx:]: return True
        return False
    
    def is_invalid2(self, n):
        n = str(n)
        max_l = int(len(n) / 2)
        for l in range(1, max_l + 1):
            s = n[:l]
            pattern = f"^({s})" + "{2,}$"
            m = re.match(pattern, n)
            if m:
                return True
        return False

    @answer(24043483400)
    def part_1(self) -> int:
        score = 0
        for l in self.input:
            idx = l.index('-')
            n1 = int(l[:idx])
            n2 = int(l[idx+1:])
            for n in range(n1, n2+1):
                if self.is_invalid(n):
                    score += n
        return score
    
    # @answer(1234)
    def part_2(self) -> int:
        score = 0
        for l in self.input:
            idx = l.index('-')
            n1 = int(l[:idx])
            n2 = int(l[idx+1:])
            for n in range(n1, n2+1):
                if self.is_invalid2(n):
                    score += n
        return score

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

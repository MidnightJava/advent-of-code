# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer
import re


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

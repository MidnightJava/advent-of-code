# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    def find_joltage(self, line: str) -> int:
        digits = list(map(lambda d: int(d), line.strip()))
        _max = max(digits)
        _max2 = max([d for d in digits if d != int(_max)])
        first_digit = str(_max)
        if line.index(first_digit) == len(line) -1:
           first_digit = str(_max2)
        start_idx = line.index(first_digit)
        next_max = 0
        for i in range(start_idx +1, len(line)):
            next_max = max(next_max, int(line[i]))
        return int(first_digit + str(next_max))
    
    def find_joltage2(self, line: str) -> int:
        digits_orig = list(map(lambda d: int(d), line.strip()))
        result = []
        i = 0
        k = 11
        j = len(line) - k
        while len(result) < 12:
            digits = digits_orig[i:j]
            _max = max(digits)
            next_digit = str(_max)
            result.append(next_digit)
            i = digits.index(_max) + i + 1
            k -= 1
            j = len(line) - k
        return int("".join(result))
           
    @answer(17554)
    def part_1(self) -> int:
        joltage = 0
        for line in self.input:
            j = self.find_joltage(line)
            joltage += j
        return joltage
    
    @answer(175053592950232)
    def part_2(self) -> int:
        i = 1
        joltage = 0
        for line in self.input:
            j = self.find_joltage2(line)
            print(i, j)
            i += 1
            joltage += j
        return joltage

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

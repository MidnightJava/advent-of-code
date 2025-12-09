# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer

""" PART 1

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are
each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input).

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within
each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by
the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4,
the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce.
"""

""" PART 2

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference
is that now there will be 12 digits in each bank's joltage output instead of two.
"""

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
        j = len(line) - 11
        while len(result) < 12:
            digits = digits_orig[i:j]
            _max = max(digits)
            next_digit = str(_max)
            result.append(next_digit)
            i += (digits.index(_max) + 1)
            j += 1
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
            i += 1
            joltage += j
        return joltage

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

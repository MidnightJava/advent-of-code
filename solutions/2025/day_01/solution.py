# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer

import re

class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    modulus = 100 
    REGEX = re.compile(r"(R|L)(\d+)")

    @answer(1059)
    def part_1(self) -> int:
        count  = 0
        ptr = 50
        for l in self.input:
            m = self.REGEX.match(l)
            dir = m.group(1)
            mag = int(m.group(2))
            if dir == 'L':
                ptr = (ptr - mag) % self.modulus
            else:
                ptr = (ptr + mag) % self.modulus
            
            if ptr == 0: count += 1
        return count



    @answer(6305)
    def part_2(self) -> int:
        count  = 0
        ptr = 50
        for l in self.input:
            m = self.REGEX.match(l)
            dir = m.group(1)
            mag = int(m.group(2))
            if dir == 'L':
                if ptr - mag == 0:
                    count+= 1
                elif ptr - mag < 0:
                    if ptr != 0: count += 1
                    remaining = mag - ptr
                    num_hits = abs(remaining) // self.modulus
                    count += num_hits
                ptr = (ptr - mag) % self.modulus
            else:
                if ptr + mag == self.modulus:
                    count += 1
                elif ptr + mag > self.modulus:
                    count += 1
                    remaining = mag - (self.modulus -ptr)
                    num_hits = remaining // self.modulus
                    count += num_hits
                ptr = (ptr + mag) % self.modulus
           
        return count
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

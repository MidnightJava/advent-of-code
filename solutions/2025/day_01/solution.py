# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer

import re

""" PART 1

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe.
A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the
right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be
rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19
would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right
from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause
it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught
you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any
rotation in the sequence.
"""

""" PART 2

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of
times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
"""

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

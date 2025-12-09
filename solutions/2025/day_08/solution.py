# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/8

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
import re
from itertools import combinations
from math import sqrt
from operator import mul
from functools import reduce

""" PART 1

This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates.
By connecting these two junction boxes together, because electricity can flow between them, they become part of
the same circuit.

Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together.
Afterward, what do you get if you multiply together the sizes of the three largest circuits?
"""

""" PART 2

The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes
together until they're all in one large circuit. Continue connecting the closest unconnected pairs of junction boxes 
ogether until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last
two junction boxes you need to connect?
"""

class Solution(StrSplitSolution):
    _year = 2025
    _day = 8

    boxes = []
    box_dict = {}
    circuits = []

    NUM_LOOPS = 10

    def distance(self, t1, t2):
        return sqrt((t1[0]-t2[0]) **2 + (t1[1]-t2[1])**2 + (t1[2]-t2[2])**2)
    
    def connected(self, b1, b2):
        pass

    def add_box_pair(self, b1, b2):
        for c in self.circuits:
            if b1 in c and b2 in c:
                return False
        for c in self.circuits:
            if b1 in c or b2 in c:
                c.add(b2)
                c.add(b1)
                return True
        self.circuits.append(set([b1, b2]))
        return True
    
    def merge_circuits(self):
        done = False
        while not done:
            done = True
            for i in range(len(self.circuits)):
                for j in range(i +1, len(self.circuits)):
                    if self.circuits[i].intersection(self.circuits[j]):
                        self.circuits[i] = self.circuits[i].union(self.circuits[j])
                        self.circuits.pop(j)
                        done = False
                        break
                if not done:
                    break

    def next_box_pair(self):
        for k,v in self.box_dict.items():
            yield k,v

    # @answer(67488)
    def part_1(self) -> int:
        for line in self.input:
            self.boxes.append(tuple([ i for i in parse_ints(re.findall(r"\d+", line))]))

        combos = combinations(self.boxes, 2)
        for combo in combos:
            self.box_dict[self.distance(combo[0], combo[1])] = (combo[0], combo[1])

        self.box_dict = dict(sorted(self.box_dict.items()))
        connections = 0
        for k,v in self.next_box_pair():
            if connections >= self.NUM_LOOPS: break
            self.add_box_pair(v[0], v[1])
            connections += 1
        self.merge_circuits()
        circuits = sorted(self.circuits, key= lambda x: len(x), reverse=True)
        return reduce(mul, map(lambda c: len(c), circuits[:3]))
                        

    @answer(3767453340)
    def part_2(self) -> int:
        self.boxes = []
        self.box_dict = {}
        self.circuits = []
        for line in self.input:
            self.boxes.append(tuple([ i for i in parse_ints(re.findall(r"\d+", line))]))

        combos = combinations(self.boxes, 2)
        for combo in combos:
            self.box_dict[self.distance(combo[0], combo[1])] = (combo[0], combo[1])

        self.box_dict = dict(sorted(self.box_dict.items()))
        last = None
        n= 0
        for k,v in self.box_dict.items():
            self.add_box_pair(v[0], v[1])
            self.merge_circuits()
            if len(self.circuits) == 1 and len(self.circuits[0]) == len(self.input):
                last = v
                break   
           
        return last[0][0] * last[1][0]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/17

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
import re
from itertools import product
from collections import defaultdict


class Solution(StrSplitSolution):
    _year = 2024
    _day = 17
    separator ="\n\n"
    
    def execute(self, idx, op, operand):
        if op == 0:
            self.a = int(self.a / 2**self.combo_op(operand))
            return idx + 2
        elif op == 1:
            self.b = self.b ^ int(operand)
            return idx + 2
        elif op == 2:
            val = bin(self.combo_op(operand)).replace('b','')[-3:]
            self.b = int(val, 2)
            return idx + 2
        elif op == 3:
            if self.a == 0:
                return idx  +2
            return int(operand)
        elif op == 4:
            self.b = self.b ^ self.c
            return idx + 2
        elif op == 5:
             val = bin(self.combo_op(operand)).replace('b','')[-3:]
             self.res.append(int(val,2))
             return idx + 2
        elif op == 6:
            self.b =  int(self.a / 2**self.combo_op(operand))
            return idx + 2
        elif op == 7:
            self.c = int(self.a / 2**self.combo_op(operand))
            return idx + 2
        else:
            print(f"Invalid op code {op}")
    
    def combo_op(self, op):
        if op in range(4):
            return op
        return self.a if op == 4 else self.b if op == 5 else self.c
      
    def init(self):
      regs = self.input[0].split('\n')
      self.a = parse_ints(re.findall(r"\d+", regs[0]))[0]
      self.b = parse_ints(re.findall(r"\d+", regs[1]))[0]
      self.c = parse_ints(re.findall(r"\d+", regs[2]))[0]
      self.prog = parse_ints(re.findall(r"\d+", self.input[1]))
      
    def _solve(self):
      idx = 0
      while idx is not None and idx < len(self.prog) - 1:
          idx = self.execute(idx, self.prog[idx], self.prog[idx+1])

      return self.res

    @answer('6,0,6,3,0,2,3,1,6')
    def part_1(self) -> int:
        self.init()
        self.res = []
        res =  self._solve()
        return ','.join(map(lambda x: str(x), res))

    def test_output(self, a, n):
        self.res = []
        self.a = a
        self._solve()
        return self.res[-n:] == self.prog[-n:]
    
    def bfs(self) -> int:
        a_parts = defaultdict(set)
        a_min = None
        for a_idx in range(len(self.prog)):
            if a_idx == 0:
                for n in range(8):
                    if self.test_output(n, a_idx+1):
                        a_parts[a_idx].add(n)
            else:
                for p in product(*a_parts.values()):
                    a = 0
                    for i in list(range(len(p))):
                        a += (p[i] * (8**(len(p) - i)))
                    for n in range(8):
                        if self.test_output(a+n, a_idx+1):
                            if a_idx == len(self.prog) - 1:
                                a_min = a+n if a_min is None else min(a+n, a_min)
                            a_parts[a_idx].add(n)
        return a_min
    
    # 200x faster solution
    def dfs(self, a: int, idx: int) -> int:
        if idx == len(self.prog):
            self.min_a = a if self.min_a is None else min(self.min_a, a)
            return
        for n in range(8):
          if self.test_output(a * 8 + n, idx+1):
            self.dfs(a * 8 + n, idx+1)
        return self.min_a


    @answer(236539226447469)
    def part_2(self) -> int:
    #    return self.bfs()
        self.min_a = None
        return self.dfs(0, 0)
        
"""
What the program is doing:

while a != 0:
  B = A % 8
  B ^= 3
  C = A / 2**B
  A  /= 8 (truncate)
  B ^= 5
  B ^= C
  Output B % 8

Solution inspired by explanation here: https://www.reddit.com/r/adventofcode/comments/1hhtc6g/comment/m2u1fjh
    EThe first n octal digits in a will determine the last n values in the output
    So if the program is X_16,X_15,X_14,...,X_0
    look for all a0s which f(a0) outputs X_0
    look for all a1s which f(a0 * 8 + a1) outputs X_1,X_0
    look for all a2s which f(a0 * 8 * 8 + a1 * 8 + a2) outputs X_2,X_1,X_0
    ...
    On the last program input, capture the a value and save it if it's the minimum
"""

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

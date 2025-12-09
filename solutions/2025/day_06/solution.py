# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

from ...base import StrSplitSolution, answer
from operator import mul
from functools import reduce

""" PART 1

While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists
of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*)
together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long
horizontal list. For example:

123 328  51 64 
45 64  387 23 
6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that
needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers
within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the
individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.
"""

""" PART 2

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most
significant digit at the top and the least significant digit at the bottom. (Problems are still separated
with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
45 64  387 23 
6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827."""

class Solution(StrSplitSolution):
    _year = 2025
    _day = 6
    separator = "\n"
    matrix = []

    @answer(6171290547579)
    def part_1(self) -> int:
        answer = 0
        for line in self.input:
            self.matrix.append(line.split())
        # Transpose the matrix
        self.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]   

        for prob in self.matrix:
            op = prob.pop()
            if op.strip() == '+':
                answer += sum(map(lambda x: int(x.strip()), prob))
            elif op.strip() == "*":
                answer += reduce(mul,  map(lambda x: int(x.strip()), prob))
        return answer
    
    @answer(8811937976367)
    def part_2(self) -> int:
        self.matrix = []
        for line in self.input:
            #Make the line a list of single charatcers, so we can detect spaces by column number
            self.matrix.append(list(line))

        # Zero-fill all spaces when any row above or below at the same column has a number (i.e. not a space).
        w = len(self.matrix[0])
        h = len(self.matrix)
        for i in range(w):
            for j in range(h):
                if self.matrix[j][i] == ' ':
                    for x in range(h):
                        if self.matrix[x][i] != ' ':
                            self.matrix[j][i] = '0'
        # Now join the list and then split it by spaces
        for i, row in enumerate(self.matrix):
            self.matrix[i] = ''.join(row).split()

        # Transpose the matrix
        self.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]   
        answer = 0
        
        # Form operands top-down for each column, i.gnoring zeros
        for prob in self.matrix:
            op = prob.pop()
            if '+' in op:
                l = max([len(x) for x in prob])
                for i in range(l):
                    ns = ''
                    for n in prob:
                       ns+= n[i]  if n[i] != '0' else ''
                    answer += int(ns)
            elif "*" in op:
                l = max([len(x) for x in prob])
                m = []
                for i in range(l):
                    ns = ''
                    for n in prob:
                       ns+= n[i] if n[i] != '0' else ''
                    m.append(int(ns))
                answer += reduce(mul, m)
        return answer


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

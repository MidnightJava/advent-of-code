# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/14

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
from re import findall
from collections import defaultdict
import time



class Solution(StrSplitSolution):
    _year = 2024
    _day = 14
    separator ="\n"
    grid = defaultdict(list)
    num_moves = 100
    width = 0
    height = 0
    score = 1
    
    def get_score(self):
      ul = ur = ll = lr = 0
      score = 1
      for loc in self.grid:
        if loc[0] < self.width // 2: #left
          if loc[1] < self.height // 2: #upper
            ul += len(self.grid[loc])
          elif loc[1] > self.height //2: #lower
            ll += len(self.grid[loc])
        elif loc[0] > self.width //2: #right
          if loc[1] < self.height // 2: #upper
            ur += len(self.grid[loc])
          elif loc[1] > self.height //2: #lower
            lr += len(self.grid[loc])
      for q in [ul, ur, ll, lr]:
       score *= q
      return score
    
    def next_loc(self, loc, vel):
      loc = ((loc[0] + vel[0]) % (self.width), (loc[1] + vel[1]) % (self.height))
      return loc
    
    def move(self):
      new_grid = defaultdict(list)
      for loc in self.grid:
        vels = self.grid[loc]
        for vel in vels:
          next_loc = self.next_loc(loc, vel)
          new_grid[next_loc].append(vel)
      self.grid = new_grid
        

    # @answer(1234)
    def part_1(self) -> int:
      for block in self.input:
        px, py, vx, vy = parse_ints(findall(r"[+-]*\d+", block))
        pos = (px, py)
        vel = (vx, vy)
        self.grid[pos].append(vel)
        self.width = max(self.width, px)
        self.height = max(self.height, py)
      self.height += 1
      self.width += 1
      self.grid_copy = self.grid.copy()
      
      for _ in range(self.num_moves):
        self.move()
      return self.get_score()

    @answer(226179492)
    def part_2(self) -> int:
      self.grid = self.grid_copy
      i = 0
      while True:
        self.move()
        i += 1
        for y in range(self.height):
          for x in range(self.width):
            print("o" if len(self.grid[(x,y)]) else " ", end="")
          print()
        # input("Continue:")
        print(f"MOVE {i}")
        # time.sleep(.3)
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/14

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
from re import findall
from collections import defaultdict, Counter
from math import prod
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Robot():
  x: int
  y: int
  vx: int
  vy: int
  
  @property
  def position(self) -> tuple[int, int]:
      return self.x, self.y



class Solution(StrSplitSolution):
    _year = 2024
    _day = 14
    separator ="\n"
    grid = defaultdict(list)
    robots = []
    num_moves = 100
    score = 1
    START = 28
    
    def get_score(self):
      ul = ur = ll = lr = 0
      for robot in self.robots:
        if robot.x < self.num_cols // 2: #left
          if robot.y < self. num_rows // 2: #upper
            ul += 1
          elif robot.y > self.num_rows //2: #lower
            ll += 1
        elif robot.x > self.num_cols //2: #right
          if robot.y < self.num_rows // 2: #upper
            ur += 1
          elif robot.y > self.num_rows //2: #lower
            lr += 1
      return prod([ul, ur, ll, lr])
    
    def move(self, n = 1):
      for robot in self.robots:
        robot.x = (robot.x + n * robot.vx) % self.num_cols
        robot.y = (robot.y + n * robot.vy) % self.num_rows

    @answer(226179492)
    def part_1(self) -> int:
      if self.use_test_data:
            self.num_cols = 11
            self.num_rows = 7
      else:
          self.num_cols = 101
          self.num_rows = 103
      for block in self.input:
        self.robots.append(Robot(*parse_ints(findall(r"-?\d+", block))))
      self.move(self.num_moves)
      return self.get_score()

    @answer(7502)
    def part_2(self) -> int:
      # pass
      self.robots.clear()
      for block in self.input:
        self.robots.append(Robot(*parse_ints(findall(r"-?\d+", block))))
      
      images = []
      self.move(self.START)
      for i in range(1,150):
        self.move(self.num_cols)
        locations = [r.position for r in self.robots]
        grid = Counter(locations)
        # images.append(f"MOVE {self.START + self.num_cols * i}")
        # images.append(f"Move {i+ 1}")
        # images.extend(
        #         "".join(str(grid.get((c, r), ".")) for c in range(self.num_cols))
        #         for r in range(self.num_rows)
        #     )
        if len(self.robots) == len(set(locations)):
          self.debug(
                    "\n".join(
                        "".join(str(grid.get((c, r), ".")) for c in range(self.num_cols))
                        for r in range(self.num_rows)
                    )
                )
          
          return self.START + self.num_cols * i
       
      # Path(__file__, "..", "output.txt").resolve().write_text("\n".join(images))

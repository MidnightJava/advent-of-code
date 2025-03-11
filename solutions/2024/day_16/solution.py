# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

from ...base import StrSplitSolution, answer
from ...utils.grid_util import grid_walk, grid_walk_val
from ...utils.vectors import IntVector2

from collections import deque
import heapq


class Solution(StrSplitSolution):
    _year = 2024
    _day = 16
    
    dirs = {
      0: (1,0), #E
      1: (0,1), #S
      2: (-1,0),#W
      3: (0,-1) #N
    }
    
    def get_start_pos(self, v):
      for pos, val in grid_walk_val(self.grid):
        if val == v: return pos
    
    def bfs(self, start, dir):
      min_score = None
      x,y = start.x, start.y
      path = [start]
      queue = [(0,x,y,dir,path)]
      while len(queue)>0:
        score,x,y,dir,path = heapq.heappop(queue)
        if IntVector2(x,y).of_grid(self.grid) == "E":
              return score
        for _dir, _score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001)]:
          move = self.dirs[_dir]
          next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
          # print(f"{_dir} => {next_pos}")
          if not next_pos in path and next_pos.of_grid(self.grid) != '#':
            path.append(next_pos)
            score += _score
            heapq.heappush(queue, (score,next_pos.x,next_pos.y,_dir,path[::]))
            # print(len(queue))
            
      return min_score

    # @answer(1234)
    def part_1(self) -> int:
      self.grid = []
      for line in self.input:
        self.grid.append(list(line))
      s = self.get_start_pos('S')
      print(f"Start at {s}")
      return self.bfs(s, 0)
      

        
    # @answer(1234)
    def part_2(self) -> int:
      pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

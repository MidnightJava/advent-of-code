# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

from ...base import StrSplitSolution, answer
from ...utils.grid_util import grid_walk, grid_walk_val
from ...utils.vectors import IntVector2

from collections import deque
import heapq

class Node:
  def __init__(self, position, dir, g, h):
      self.position = position
      self.dir = dir
      self.g = g
      self.h = h
      self.f = g + h
      self.parent = None

  def __lt__(self, other):
      return self.f < other.f

class Solution(StrSplitSolution):
    _year = 2024
    _day = 16
    
    dirs = {
      0: (1,0), #E
      1: (0,1), #S
      2: (-1,0),#W
      3: (0,-1) #N
    }
    
    def get_goal_pos(self, v: str):
      for pos, val in grid_walk_val(self.grid):
        if val == v:
          return pos
    
    def get_start_node(self, v: str, goal: IntVector2):
      for pos, val in grid_walk_val(self.grid):
        if val == v:
          return Node(pos, 0, 0, abs(pos.x - goal.x) + abs(pos.y - goal.y))
    
    def a_star(self, start: Node, goal: IntVector2):
      open_list = []
      closed_list = set()

      heapq.heappush(open_list, start)

      while open_list:
          current_node = heapq.heappop(open_list)
          x,y,dir = current_node.position.x, current_node.position.y, current_node.dir

          if current_node.position == goal:
              path = []
              g = current_node.g
              while current_node:
                  path.append(current_node.position)
                  current_node = current_node.parent
              return len(path), g

          closed_list.add(current_node.position)

          for _dir, score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001), ((dir+2)%4, 2001)]:
            move = self.dirs[_dir]
            next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
            if next_pos.of_grid(self.grid) != '#' and next_pos not in closed_list:
              g = current_node.g + score
              h = abs(next_pos.x - goal.x) + abs(next_pos.y - goal.y)
              neighbor_node = Node(next_pos, _dir, g, h)
              neighbor_node.parent = current_node
              heapq.heappush(open_list, neighbor_node)
                  
      return None
    
    def a_star2(self, start: Node, goal: IntVector2, shortest: int, paths: list[list]):
      open_list = []
      closed_list = set()

      heapq.heappush(open_list, start)

      while open_list:
          current_node = heapq.heappop(open_list)
          x,y,dir = current_node.position.x, current_node.position.y, current_node.dir

          if current_node.position == goal:
              path = []
              while current_node:
                  path.append(current_node.position)
                  current_node = current_node.parent
              paths.append(path)
              open_list = []
              closed_list = set()
              heapq.heappush(open_list, start)
              continue

          closed_list.add(current_node.position)

          for _dir, score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001), ((dir+2)%4, 2001)]:
            move = self.dirs[_dir]
            next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
            if next_pos.of_grid(self.grid) != '#' and next_pos not in closed_list:
              g = current_node.g + score
              h = abs(next_pos.x - goal.x) + abs(next_pos.y - goal.y)
              neighbor_node = Node(next_pos, _dir, g, h)
              neighbor_node.parent = current_node
              heapq.heappush(open_list, neighbor_node)
                  
      return paths
    
    def bfs(self, start, dir, s):
      paths = []
      x,y = start.x, start.y
      path = [start]
      queue = [(0,x,y,dir,path)]
      while len(queue)>0:
        score,x,y,dir,path = heapq.heappop(queue)
        if IntVector2(x,y).of_grid(self.grid) == "E":
              if score == s:
                paths.append(path)
        for _dir, _score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001)]:
          move = self.dirs[_dir]
          next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
          # print(f"{_dir} => {next_pos}")
          if not next_pos in path and next_pos.of_grid(self.grid) != '#':
            if score == s and path not in paths:
              path.append(next_pos)
              score += _score
              heapq.heappush(queue, (score,next_pos.x,next_pos.y,_dir,path[::]))
              # print(len(queue))
            
      return paths

    # @answer(1234)
    def part_1(self) -> int:
      self.grid = []
      for line in self.input:
        self.grid.append(list(line))
      g = self.get_goal_pos('E')
      s = self.get_start_node('S', g)
      print(f"Start at {s}")
      l, score = self.a_star(s, g)
      print(f"length {l}")
      return score
      

        
    # @answer(1234)
    def part_2(self) -> int:
      g = self.get_goal_pos('E')
      s = self.get_start_node('S', g)
      print(f"Start at {s}")
      l, score = self.a_star(s, g)
      paths = self.bfs(s.position, 0, score)
      print(f"{len(paths)} paths")
      flattened = [item for sublist in paths for item in sublist]
      return len(set(flattened))
      

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

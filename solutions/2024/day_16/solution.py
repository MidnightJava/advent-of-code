# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

from ...base import StrSplitSolution, answer
from ...utils.grid_util import grid_walk, grid_walk_val
from ...utils.vectors import IntVector2

import heapq
import time

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
    
    moves = {
      0: (1,0), #E
      1: (0,1), #S
      2: (-1,0),#W
      3: (0,-1) #N
    }
    
    start_time = time.time()
    best_path_nodes = set()
        
    def get_goal_pos(self, v: str):
      for pos, val in grid_walk_val(self.grid):
        if val == v:
          return pos
    
    def get_start_node(self, v: str, goal: IntVector2):
      for pos, val in grid_walk_val(self.grid):
        if val == v:
          return Node(pos, 0, 0, abs(pos.x - goal.x) + abs(pos.y - goal.y))
        
    def get_start_pos(self, v: str):
      for pos, val in grid_walk_val(self.grid):
        if val == v:
          return pos
    
    def get_best_path(self, start: Node, goal: IntVector2):
      open_list = []
      closed_list = set()

      heapq.heappush(open_list, start)

      while open_list:
          current_node = heapq.heappop(open_list)
          x,y,dir = current_node.position.x, current_node.position.y, current_node.dir

          if current_node.position == goal:
              return current_node.g

          closed_list.add(current_node.position)

          for _dir, score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001), ((dir+2)%4, 2001)]:
            move = self.moves[_dir]
            next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
            if next_pos.of_grid(self.grid) != '#' and next_pos not in closed_list:
              g = current_node.g + score
              h = abs(next_pos.x - goal.x) + abs(next_pos.y - goal.y)
              neighbor_node = Node(next_pos, _dir, g, h)
              neighbor_node.parent = current_node
              heapq.heappush(open_list, neighbor_node)
                  
      return None
    
    def get_all_best_paths(self, start: Node, goal: IntVector2, min_score: int):
      open_list = []
      visited = {(start.position, start.dir): start.g}      
      heapq.heappush(open_list, start)

      while open_list:
          current_node = heapq.heappop(open_list)
          x,y,dir = current_node.position.x, current_node.position.y, current_node.dir

          if current_node.position == goal:
            if current_node.g == min_score:
                path = []
                g = current_node.g
                while current_node:
                  path.append(current_node.position)
                  current_node = current_node.parent
                self.best_path_nodes.update(path)
            continue
                
          if current_node.g >= min_score:
            continue 

          for _dir, score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001)]:
            move = self.moves[_dir]
            next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
            if next_pos.of_grid(self.grid) != '#':
              g = current_node.g + score
              if (next_pos, _dir) not in visited or visited[(next_pos, _dir)] >= g:
                if g <= min_score:
                  visited[(next_pos, _dir)] = g
                  h = abs(next_pos.x - goal.x) + abs(next_pos.y - goal.y)
                  nb = Node(next_pos, _dir, g, h)
                  nb.parent = current_node
                  heapq.heappush(open_list, nb)
                  
      return self.best_path_nodes
            
    @answer(115500)
    def part_1(self) -> int:
      self.grid = []
      for line in self.input:
        self.grid.append(list(line))
      g = self.get_goal_pos('E')
      s = self.get_start_node('S', g)
      self.debug(f"Part 1 time: {(time.time() - self.start_time):.2f} sec")
      return self.get_best_path(s, g)
      

        
    @answer(679)
    def part_2(self) -> int:
      g = self.get_goal_pos('E')
      s = self.get_start_node('S', g)
      score = self.get_best_path(s, g)
      nodes = self.get_all_best_paths(s, g, score)
      self.debug(f"Part 2 time: {(time.time() - self.start_time):.2f} sec")
      return len(nodes)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

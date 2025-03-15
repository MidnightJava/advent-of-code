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
    
    paths = []
        
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
    
    def a_star2(self, start: Node, goal: IntVector2, min_score: int):
      open_list = []
      closed_list = {start.position: 0}
      pos = (start.position.x, start.position.y)
      
      heapq.heappush(open_list, (start, [start.position]))

      while open_list:
          current_node, path = heapq.heappop(open_list)
          x,y,dir = current_node.position.x, current_node.position.y, current_node.dir

          if current_node.position == goal:
            if current_node.g == min_score:
                self.paths.append(path)
                
          if current_node.g > min_score:
            continue 

          for _dir, score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001), ((dir+2)%4, 2001)]:
            move = self.dirs[_dir]
            next_pos = IntVector2(x,y) + IntVector2(move[0], move[1])
            if next_pos.of_grid(self.grid) != '#':
              g = current_node.g + score
              if next_pos not in closed_list or closed_list[next_pos] <= min_score:
                if g <= min_score:
                  closed_list[next_pos] = g
                  h = abs(next_pos.x - goal.x) + abs(next_pos.y - goal.y)
                  neighbor_node = Node(next_pos, _dir, g, h)
                  neighbor_node.parent = current_node
                  path.append(neighbor_node.position)
                  heapq.heappush(open_list, (neighbor_node, path[::]))
                  
      return self.paths
    
    def dfs(self, current: IntVector2, goal: IntVector2, dir: int, score: int, min_score: int, path: list, seen: dict):

      # print(f"Current pos {current}")
      if current == goal:
        print("Reached goal")
        if score == min_score:
          self.paths.append(path)
       
      if score == min_score:
        return
          
      for _dir, _score in [(dir,1), ((dir+1)%4, 1001), ((dir-1)%4, 1001), ((dir+2)%4, 2001)]:
        move = self.dirs[_dir]
        next_pos = IntVector2(current.x, current.y) + IntVector2(move[0], move[1])
        if next_pos.of_grid(self.grid) != '#':
          score += _score
          if score > min_score:
            continue
          if next_pos not in seen or seen[next_pos] > score:
            path.append(next_pos)
            seen[next_pos] = score
            self.dfs(next_pos, goal, _dir, score, min_score, path[::], seen.copy())
            
    # @answer(1234)
    def part_1(self) -> int:
      self.grid = []
      for line in self.input:
        self.grid.append(list(line))
      g = self.get_goal_pos('E')
      s = self.get_start_node('S', g)
      print(f"Start at {s}")
      l, score = self.a_star(s, g)
      print(f"part 1 path length {l}")
      return score
      

        
    # @answer(1234)
    def part_2(self) -> int:
      g = self.get_goal_pos('E')
      s = self.get_start_node('S', g)
      print(f"Start at {s}")
      l, score = self.a_star(s, g)
      print(f"start at {s} goal is {g}")
      paths = self.a_star2(s, g, score)
      print(f"{len(paths)} paths")
      unique_nodes = set()
      for path in paths:
        for node in path:
          unique_nodes.add(node)
      for node in unique_nodes:
        node.set_grid(self.grid, 'O')
      for line in self.grid:
        print("".join(line))
      return len(unique_nodes)
      
      # s2 = self.get_start_pos('S')
      # print(f"start at {s2} goal is {g}")
      # self.dfs(current=s2, goal=g, dir=0, score=0, min_score=score, path=[s2], seen={s2:0})
      # flattened = [item for sublist in self.paths for item in sublist]
      # for pos in flattened:
      #   IntVector2(pos[0], pos[1]).set_grid(self.grid, 'O')
      # for line in self.grid:
      #   print("".join(line))
      # return len(flattened)
      

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

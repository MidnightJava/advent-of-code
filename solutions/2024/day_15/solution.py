# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/15

from ...base import StrSplitSolution, answer
from typing import List
from ...utils.vectors import IntVector2 as Iv
from ...utils.grid_util import grid_walk_val

class Grid():
    x: int = 0
    y: int = 0
    robot_pos = None

    def __init__(self, data: List[str]):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])
        for i, line in enumerate(data):
            if "@" in line:
                x = line.index("@")
                data[i] = line.replace("@", ".")
                self.robot_pos = (x, i)
                break
              
    @staticmethod
    def peek(x, y, grid):
        return grid[y][x]
      
    @staticmethod
    def set(x, y, ch, grid):
      line = grid[y]
      line = line[:x] + ch + line[x + 1:]
      grid[y] = line
      
    def score(self):
      total = 0
      for y, line in enumerate(self.data):
        total += sum([y*100 + x for x, c in enumerate(line) if c == 'O' ])
      return total

class Solution(StrSplitSolution):
    _year = 2024
    _day = 15
    separator = "\n\n"

    def print_grid(self, robot):
      lines = []
      for i, line in enumerate(self.grid.data):
          if i == robot[1]:
              line = line[:robot[0]] +  "@" + line[robot[0] + 1:]
          lines.append(line)
      return lines

    def shove_box(self, pos, ch, move, grid):
        """ 
        Attempt to shove the box at pos in the indicated direction. If successful,
        put the character ch in its place
        """
        y = pos[1] -1 if move == '^' else pos[1] + 1 if move == 'v' else pos[1]
        x = pos[0] -1 if move == '<' else pos[0] + 1 if move == '>' else pos[0]
        c = grid[y][x]
        if c == "#": return None
        elif c == "O":
          Grid.set(pos[0], pos[1], ch, grid)
          new_grid = self.shove_box((x,y), 'O', move, grid)
          if not new_grid: return None
          else:
            Grid.set(x,y , c, new_grid)
            return new_grid[::]
        else:
            new_grid = grid[::]
            Grid.set(x, y, 'O', new_grid)
            Grid.set(pos[0], pos[1], ch, new_grid)
            return new_grid


    @answer(1414416)
    def part_1(self) -> int:
        self.grid = Grid(self.input[0].split())
        robot = self.grid.robot_pos
        moves = self.input[1].replace('\n', '')
        # for line in self.print_grid(robot):
        #   self.debug(line)
        for move in moves:
            # self.debug(f"Move {move}:")
            y = robot[1] -1 if move == '^' else robot[1] + 1 if move == 'v' else robot[1]
            x = robot[0] -1 if move == '<' else robot[0] + 1 if move == '>' else robot[0]
            c = Grid.peek(x,y, self.grid.data)
            if c == 'O':
                new_grid = self.shove_box((x,y), '.', move, self.grid.data[::])
                if new_grid:
                    self.grid.data = new_grid
                    robot = (x, y)
            elif c == '.':
                robot = (x, y)
        #     # self.debug(self.print_grid(robot))
        # for line in self.print_grid(robot):
        #   self.debug(line)
        return self.grid.score()
    
    def do_move(self, v_pos: list, v_dir):
      next_pos = [ v + v_dir for v in v_pos ]
      move = True
      push_move = []
      for i, nex_val in enumerate([ v.of_grid(self.grid) for v in next_pos ]):
          if next_pos[i] in push_move:
              continue
          elif nex_val == '#':
              return False
          elif nex_val in '[]':
              push_move.append(next_pos[i])
              #vertical push also pushes other bracket of box
              if v_dir.y != 0:
                  push_move.append(next_pos[i] + self.dir_dict[nex_val])

      if move and push_move:
          move = self.do_move(push_move, v_dir)

      if move:
          for i, np in enumerate(next_pos):
              np.set_grid(self.grid, v_pos[i].of_grid(self.grid))
              v_pos[i].set_grid(self.grid, '.')

          return move
      
    # Part 2 solution copied from https://github.com/RichRat/pyxercise/blob/master/advent/adv15.py
    @answer(1386070)
    def part_2(self) -> int:
      
      map_map = {'#': '##', '.': '..', 'O': '[]', '@': '@.'}
      lines = [ line for line in self.input[0].split("\n")]
      self.grid = [ [c for c in "".join([ map_map[sc] for sc in line ])] for line in lines if line.startswith('#') ]
      
      bot_pos = None
      for pos, val in grid_walk_val(self.grid):
          if val == '@':
              bot_pos = pos
              break
      
      self.dir_dict = {
        '^': Iv(0, -1),
        '>': Iv(1, 0),
        'v': Iv(0, 1),
        '<': Iv(-1, 0),
        '[': Iv(1, 0),
        ']': Iv(-1, 0)
      }
    
      moves = self.input[1].replace('\n', '')
      for move in moves:
          v_direction = self.dir_dict[move]
          if self.do_move([bot_pos], v_direction):
              bot_pos += v_direction
          
      result = 0
      for pos, val in grid_walk_val(self.grid):
        if val == '[':
            result += pos.x + pos.y * 100
            
      return result


    

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

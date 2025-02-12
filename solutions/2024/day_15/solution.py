# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/15

from ...base import StrSplitSolution, answer
from typing import List

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
                self.robot_pos = (i, x)
                break
              
    @staticmethod
    def peek(y, x, grid):
        return grid[y][x]
      
    @staticmethod
    def set(y, x, ch, grid):
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
          if i == robot[0]:
              line = line[:robot[1]] +  "@" + line[robot[1] + 1:]
          lines.append(line)
      return lines

    def shove_box(self, pos, ch, move, grid):
        """ 
        Attempt to shove the box at pos in the indicated direction. If successful,
        put the character ch in its place
        """
        y = pos[0] -1 if move == '^' else pos[0] + 1 if move == 'v' else pos[0]
        x = pos[1] -1 if move == '<' else pos[1] + 1 if move == '>' else pos[1]
        c = grid[y][x]
        if c == "#": return None
        elif c == "O":
          Grid.set(pos[0], pos[1], ch, grid)
          new_grid = self.shove_box((y,x), 'O', move, grid)
          if not new_grid: return None
          else:
            Grid.set(y,x , c, new_grid)
            return new_grid[::]
        else:
            new_grid = grid[::]
            Grid.set(y, x, 'O', new_grid)
            Grid.set(pos[0], pos[1], ch, new_grid)
            return new_grid


    @answer(1414416)
    def part_1(self) -> int:
        self.grid = Grid(self.input[0].split())
        robot = self.grid.robot_pos
        moves = self.input[1].replace('\n', '')
        self.print_grid(robot)
        for move in moves:
            self.debug(f"Move {move}:")
            y = robot[0] -1 if move == '^' else robot[0] + 1 if move == 'v' else robot[0]
            x = robot[1] -1 if move == '<' else robot[1] + 1 if move == '>' else robot[1]
            c = Grid.peek(y,x, self.grid.data)
            if c == 'O':
                new_grid = self.shove_box((y,x), '.', move, self.grid.data[::])
                if new_grid:
                    self.grid.data = new_grid
                    robot = (y, x)
            elif c == '.':
                robot = (y, x)
            self.debug(self.print_grid(robot))
        self.debug(self.print_grid(robot))
        return self.grid.score()

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

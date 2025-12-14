# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
import re

class Machine:

    def __init__(self, lights=[], buttons=[]):
        self.lights = lights
        self.buttons = buttons


class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    machines = []

    # @answer(1234)
    def part_1(self) -> int:
        for line in self.input:
            lights = re.findall(r'[\.#]', line)
            buttons = list(map(lambda b: re.sub(r'[()]', "", b), re.findall(r'\(\d+,?[\d,]*\d*\)', line)))
            buttons = [tuple(map(int, x.split(','))) for x in buttons]   
            machine = Machine(lights, buttons)
            self.machines.append(machine)
        for machine in self.machines:
            for light in machine.lights:
                print(light, end='')
            print("\n")
            for button in machine.buttons:
                print(button, type(button))
            print("-----------------")

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
import re
from itertools import product

class Machine:

    def __init__(self, lights=[], buttons=[], joltage=tuple()):
        self.lights = lights
        self.buttons = buttons
        self.joltage = joltage

    def __repr__(self):
        return ''.join(map(str, (self.buttons, self.joltage)))


class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    machines = []
    cache = {}

    def min_presses(self, configs, machine):
        min_count = None
        for config in configs:
            l = list('.' * len(machine.lights))
            for i, c in enumerate(config):
                #press buttons[i] c times
                btn = machine.buttons[i]
                if c % 2 != 0:
                    for b in btn:
                        l[b] = '.' if l[b] == '#' else '#'
            if l == machine.lights:
                num_presses = sum(config)
                min_count = num_presses if not min_count else min(num_presses, min_count)
        return min_count
    
    def min_presses2(self, configs, machine):
        min_count = None
        for config in configs:
            n = len(machine.joltage)
            counters = [0] * n
            for i, c in enumerate(config):
                #press buttons[i] c times
                if c != 0:
                    btn = machine.buttons[i]
                    for b in btn:
                        counters[b] += c
            if counters == list(machine.joltage):
                num_presses = sum(config)
                min_count = num_presses if not min_count else min(num_presses, min_count)
        self.cache[machine] = min_count
        return min_count
    
    @answer(514)
    def part_1(self) -> int:
        for line in self.input:
            lights = re.findall(r'[\.#]', line)
            buttons = list(map(lambda b: re.sub(r'[()]', "", b), re.findall(r'\(\d+,?[\d,]*\d*\)', line)))
            buttons = [tuple(map(int, x.split(','))) for x in buttons]
            joltage = tuple(
                int(x)
                for b in re.findall(r'\{[\d,]+\}', line)
                for x in b.strip('{}').split(',')
            )

            machine = Machine(lights, buttons, joltage)
            self.machines.append(machine)
        count = 0
        for machine in self.machines:
            n = len(machine.buttons)
            button_configs = product(range(2), repeat=n)
            count+= self.min_presses(list(button_configs), machine)
        return count

    # @answer(1234)
    def part_2(self) -> int:
        # for machine in self.machines:
        #     print(f"joltage: {machine.joltage}, class: {type(machine.joltage)}")
        count = 0
        for machine in self.machines:
            if machine in  self.cache:
                print("Using cache")
                count+= self.cache[machine]
            else:
                n = len(machine.buttons)
                button_configs = product(range(6), repeat=n)
                count += self.min_presses2(button_configs, machine)
        return count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

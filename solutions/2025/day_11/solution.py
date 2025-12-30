# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
import heapq
from functools import cache


class Solution(StrSplitSolution):
    _year = 2025
    _day = 11

    devices = {}

    def num_paths(self):
        queue = []
        paths = 0

        heapq.heappush(queue, (set(), "you", self.devices["you"]))
        while queue:
            visited, src, dests = heapq.heappop(queue)
            visited.add(src)
            if "out" in dests:
               paths += 1
               continue
            for dst in dests:
                if dst not in visited:
                    heapq.heappush(queue, (visited.copy(), dst, self.devices[dst]))
        return paths
    
    @cache
    def dfs(self, start, path_t, visited_t):
        path = list(path_t)
        visited = list(visited_t)
        # print(len(path))
        for dev in self.devices[start]:
            if dev == "out":
                if "fft" in path or "dac" in path:
                    self.paths += 1
            elif not dev in visited:
                visited.append(dev)
                path.append(dev)
                self.dfs(dev, tuple(path), tuple(visited))

    @answer(506)
    def part_1(self) -> int:
        for line in self.input:
            parts = line.split(":")
            self.devices[parts[0]] = parts[1].split()

        return self.num_paths()

    # @answer(1234)
    def part_2(self) -> int:
        self.paths = 0
        l = ['svr']
        self.dfs("svr", tuple(l), tuple(['svr']))
        return self.paths
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

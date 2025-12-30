# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
import heapq


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
    
    def num_paths2(self):
        queue = []
        path = ["svr"]
        num_paths = 0
        paths = set()

        heapq.heappush(queue, (set(), path, "svr"))
        while queue:
            # print(len(queue))
            visited, _path, src = heapq.heappop(queue)
            visited.add(src)
            if src == "out":
                if "dac" in _path and "fft" in _path:
                    num_paths += 1
                continue
            for dst in self.devices[src]:
                if not dst in visited and not dst in _path and not dst == "svr":
                    _path.append(dst)
                    if  not tuple(_path) in paths:
                        paths.add(tuple(_path))
                        heapq.heappush(queue, (visited.copy(), _path[::],  dst))
        return num_paths

    @answer(506)
    def part_1(self) -> int:
        for line in self.input:
            parts = line.split(":")
            self.devices[parts[0]] = parts[1].split()

        return self.num_paths()

    # @answer(1234)
    def part_2(self) -> int:
        return self.num_paths2()
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

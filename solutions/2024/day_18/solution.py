# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/18

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
from ...utils.graphs import neighbors, GridPoint, taxicab_distance
import re
import heapq

class Solution(StrSplitSolution):
    _year = 2024
    _day = 18
    separator = '\n'
    start = (0,0)
    min_cost = None
    
    # Recursion doesn't close. Not a good approach for shortest path
    def dfs(self, pos: GridPoint, end: GridPoint, cost: int, visited: dict[int]):
        print(pos)
        if pos == end:
            self.min_cost = cost if self.min_cost is None else min(cost, self.min_cost)
        for nb in neighbors(pos, num_directions=4, max_size=self.max_size):
            if not nb in self.bytes:
                if nb not in visited or visited[nb] > cost+1:
                    visited[nb] = cost + 1
                    self.dfs(nb, end, cost+1, visited.copy())
    
    def bfs(self, start: GridPoint, end: GridPoint):
        min_dst = None
        open_list = []
        path = []

        heapq.heappush(open_list, (0, start, [], set()))
        while open_list:
            dst, pos, _path, visited = heapq.heappop(open_list)
            if pos == end:
                if min_dst is None or dst < min_dst:
                  min_dst = dst
                  path = _path
                continue
            if pos in visited:
              continue
            visited.add(pos)
            for nb in neighbors(pos, num_directions=4, max_size=self.max_size):
                if nb not in self.bytes:
                    if nb not in visited:
                        heapq.heappush(open_list, (dst+1, nb, _path + [nb], visited))
        return min_dst, path
    
    def bfsa(self, start: GridPoint, end: GridPoint):
        seen = set([start])
        path = [start]
        queue = [(start, path)]
        while len(queue):
            next_q = []
            for pos, path in queue:
                if pos == end:
                    return path
                for nb in neighbors(pos, num_directions=4, max_size=self.max_size):
                    if nb not in self.bytes and nb not in seen:
                        seen.add(nb)
                        next_q.append((nb,  path + [nb]))
            queue = next_q
        return []

    @answer(298)
    def part_1(self) -> int:
        self.max_size = 6 if self.use_test_data else 70
        self.n = 12 if self.use_test_data else 1024
        self.end = (self.max_size, self.max_size)
        # convert input to (y,x) format
        self._bytes = list(map(lambda x: tuple(parse_ints(re.findall(r'\d+', x)))[::-1], self.input))
        self.bytes = self._bytes[:self.n]
        # self.dfs(self.start, self.end, 0, {})
        # return self.min_cost
        cost, _ =  self.bfs(self.start, self.end)
        return cost
    
    def find_breaking_idx(self, left, right):
        while left <= right:
            if left == right:
                return self._bytes[left][::-1]
            middle = (left + right) // 2
            self.bytes = self._bytes[0: middle+1]
            path = self.bfsa(self.start, self.end)
            if len(path) == 0:
                right = middle - 1
            else:
                left = middle + 1
        return None
      
    @answer((52,32))
    def part_2(self) -> int:
        return self.find_breaking_idx(0, len(self._bytes) -1)

        #This works, but it's a semi brute-force solution that takes 16 secs
        # path = None
        # for b in self._bytes[self.n:]:
        #     self.bytes.append(b)
        #     if path is None or b in path:
        #         path = self.bfsa(self.start, self.end)
        #         if not len(path):
        #             return b[::-1]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

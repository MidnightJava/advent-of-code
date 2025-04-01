# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/18

from ...base import StrSplitSolution, answer
from ...utils.transformations import parse_ints
from ...utils.graphs import neighbors, GridPoint, taxicab_distance
import re
import heapq
from collections import defaultdict

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
        min_cost = None
        open_list = []
        path = []

        heapq.heappush(open_list, (0, 0, start, [], set()))
        while open_list:
            dst, cost, pos, _path, visited = heapq.heappop(open_list)
            if pos == end:
                if min_cost is None or cost < min_cost:
                  min_cost = cost
                  path = _path
                continue
            if pos in visited:
              continue
            visited.add(pos)
            for nb in neighbors(pos, num_directions=4, max_size=self.max_size):
                if nb not in self.bytes:
                    if nb not in visited:
                        heapq.heappush(open_list, (dst + taxicab_distance(nb, end), cost+1, nb, _path + [nb], visited))
        return min_cost, path

    def bfs2(self, start: GridPoint, end: GridPoint):
      open_list = []
      paths = []

      heapq.heappush(open_list, (0, [], start, {}))
      while open_list:
          dst, path, pos, visited = heapq.heappop(open_list)
          if pos == end:
              paths.append(path)
              visited = set()
              continue
          if pos in visited:
            continue
          visited[pos] = dst
          for nb in neighbors(pos, num_directions=4, max_size=self.max_size):
              if nb not in self.bytes:
                  if nb not in visited or visited[nb] >= dst:
                    heapq.heappush(open_list, (dst + taxicab_distance(nb, end), path[::]+[nb], nb, visited))
      return paths

    # @answer(298)
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
            self.bytes = self._bytes[:self.n] + self._bytes[left: middle+1]
            paths = self.bfs2(self.start, self.end)
            if len(paths) == 0:
                print(self.bytes[self.n:])
                right = middle - 1
            else:
                left = middle + 1
        return None
      
    # @answer(52,32)
    def part_2(self) -> int:
        # This does not work, but seems like it should
        # return self.find_breaking_idx(0, len(self._bytes) -1)

        #This works, but it's a semi brute-force solution that takes 20 secs
        path = None
        for b in self._bytes[self.n:]:
            self.bytes.append(b)
            if path is None or b in path:
                _, path = self.bfs(self.start, self.end)
                if not len(path):
                    return b[::-1]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

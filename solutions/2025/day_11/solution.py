# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
import heapq
from functools import lru_cache
from collections import defaultdict, deque

#Graph pruning courtesy of CHat GPT

def tarjan_scc(graph):
    index = 0
    stack = []
    on_stack = set()
    ids = {}
    low = {}
    sccs = []

    def dfs(at):
        nonlocal index
        ids[at] = low[at] = index
        index += 1
        stack.append(at)
        on_stack.add(at)

        for to in graph.get(at, []):
            if to not in ids:
                dfs(to)
                low[at] = min(low[at], low[to])
            elif to in on_stack:
                low[at] = min(low[at], ids[to])

        if ids[at] == low[at]:
            comp = set()
            while True:
                n = stack.pop()
                on_stack.remove(n)
                comp.add(n)
                if n == at:
                    break
            sccs.append(comp)

    for n in graph:
        if n not in ids:
            dfs(n)

    return sccs

def build_scc_graph(devices, sccs):
    node_to_scc = {}
    for i, comp in enumerate(sccs):
        for n in comp:
            node_to_scc[n] = i

    dag = {i: set() for i in range(len(sccs))}
    for u, vs in devices.items():
        for v in vs:
            if node_to_scc[u] != node_to_scc[v]:
                dag[node_to_scc[u]].add(node_to_scc[v])

    return dag, node_to_scc

def scc_metadata(sccs):
    meta = []
    for comp in sccs:
        meta.append({
            'has_fft': 'fft' in comp,
            'has_dac': 'dac' in comp,
            'has_out': 'out' in comp
        })
    return meta

FFT, DAC = 1, 2
ALL = FFT | DAC

def count_paths_dag(dag, meta, start_scc, end_scc):
    @lru_cache(None)
    def dfs(scc, mask):
        if meta[scc]['has_fft']:
            mask |= FFT
        if meta[scc]['has_dac']:
            mask |= DAC

        if scc == end_scc:
            return 1 if mask == ALL else 0

        total = 0
        for nxt in dag[scc]:
            total += dfs(nxt, mask)
        return total

    return dfs(start_scc, 0)



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
    

    def count_paths(self, devices, start='svr', end='out', waypoints=('fft', 'dac')):
        if 'fft' not in self.from_svr or 'dac' not in self.can_reach_out:
            return 0

        # --- collect all nodes ---
        nodes = set(devices.keys())
        for nbrs in devices.values():
            nodes.update(nbrs)

        # --- assign node indices ---
        node_index = {node: i for i, node in enumerate(nodes)}

        # --- waypoint bitmask ---
        wp_index = {wp: i for i, wp in enumerate(waypoints)}
        ALL_WP_MASK = (1 << len(waypoints)) - 1

        @lru_cache(maxsize=None)
        def dfs(node, wp_mask, visited_mask):
            node_bit = 1 << node_index[node]
            if visited_mask & node_bit:
                return 0
            visited_mask |= node_bit

            if node in wp_index:
                wp_mask |= 1 << wp_index[node]

            if node == end:
                return 1 if wp_mask == ALL_WP_MASK else 0

            total = 0
            for nxt in devices.get(node, ()):
                total += dfs(nxt, wp_mask, visited_mask)

            return total

        return dfs(start, 0, 0)

    @answer(506)
    def part_1(self) -> int:
        for line in self.input:
            parts = line.split(":")
            self.devices[parts[0]] = parts[1].split()

        return self.num_paths()

    @answer(385912350172800)
    def part_2(self) -> int:
        sccs = tarjan_scc(self.devices)
        dag, node_to_scc = build_scc_graph(self.devices, sccs)

        start_scc = node_to_scc['svr']
        end_scc   = node_to_scc['out']

        meta = scc_metadata(sccs)

        result = count_paths_dag(dag, meta, start_scc, end_scc)
        return result

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

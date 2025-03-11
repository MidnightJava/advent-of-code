"""Explanation of the A* Algorithm Implementation
The A* algorithm is a pathfinding and graph traversal technique that finds the shortest path between a start node and a goal node by considering both the actual cost from the start node and an estimated cost to the goal. Here's a step-by-step breakdown of the implementation:

Node Class:
Attributes:
position: The coordinates of the node in the grid.
g: The actual cost from the start node to the current node.
h: The heuristic cost from the current node to the goal node.
f: The total cost, which is the sum of g and h.
parent: The parent node, used to reconstruct the path.
Methods:
__lt__(self, other): This method is used to compare nodes in the priority queue. It ensures that nodes with a lower f value are prioritized.
A Algorithm Function*:
Parameters:
grid: A 2D list representing the grid where 'X' indicates an obstacle.
start: The starting position as a tuple (x, y).
goal: The goal position as a tuple (x, y).
Steps:
Initialization:
Create an open list (priority queue) and a closed list (set).
Create the start node with g = 0 and h calculated using the Manhattan distance.
Push the start node onto the open list.
Main Loop:
While the open list is not empty:
Pop the node with the lowest f value from the open list.
If the current node is the goal node, reconstruct and return the path.
Add the current node to the closed list.
Generate the neighbors of the current node (up, down, left, right).
For each neighbor:
Ensure the neighbor is within the grid bounds, not an obstacle, and not in the closed list.
Calculate the g value (cost from start to neighbor).
Calculate the h value (heuristic cost from neighbor to goal).
Create a new node for the neighbor and set its parent to the current node.
Push the neighbor node onto the open list.
Path Reconstruction:
If the goal node is found, trace back from the goal node to the start node using the parent attribute to get the path.
If no path is found, return None.
"""

import heapq

class Node:
    def __init__(self, position, g, h):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def a_star(grid, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, 0, abs(start[0] - goal[0]) + abs(start[1] - goal[1]))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for neighbor in neighbors:
            neighbor_pos = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] != 'X' and
                neighbor_pos not in closed_list):
                g = current_node.g + 1
                h = abs(neighbor_pos[0] - goal[0]) + abs(neighbor_pos[1] - goal[1])
                neighbor_node = Node(neighbor_pos, g, h)
                neighbor_node.parent = current_node
                heapq.heappush(open_list, neighbor_node)
                
    return None
  
  
  # Example grid and usage
grid = [
    ['S', '1', '1', 'X', '1'],
    ['1', 'X', '1', '1', '1'],
    ['1', '1', '1', 'X', 'G']
]
start = (0, 0)
goal = (2, 4)
path = a_star(grid, start, goal)
print("Path found:", path)
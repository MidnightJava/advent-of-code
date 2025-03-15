from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])  # Queue stores (current position, current path)
    visited = set([start])
    shortest_paths = []

    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == end:
            shortest_paths.append(path)
            # Continue BFS to find other shortest paths
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return shortest_paths

# Example usage
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1]
]
start = (0, 0)
end = (4, 4)
shortest_paths = bfs(maze, start, end)
print(shortest_paths)
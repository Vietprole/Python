from collections import deque

def min_moves(maze, m, n):
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y, steps = queue.popleft()
        if x == m - 1 and y == n - 1:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))
                print(queue)
                print(visited)
    return -1

# m, n = map(int, input().split())
# maze = [list(input()) for _ in range(m)]
# test
m, n = 5, 5
maze = [
    ['.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.']
]
print(min_moves(maze, m, n))
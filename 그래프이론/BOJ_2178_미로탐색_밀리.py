from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = True
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze[nx][ny] == 0:
            continue
        if visited[nx][ny] == False:
            maze[nx][ny] = maze[x][y] + 1
            visited[nx][ny] = True
            q.append((nx, ny))

print(maze[n-1][m-1])
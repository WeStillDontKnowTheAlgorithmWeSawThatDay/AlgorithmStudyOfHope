from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

queue = deque([(0, 0)])

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if arr[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                arr[next_x][next_y] = arr[x][y] + 1

print(arr[n-1][m-1])

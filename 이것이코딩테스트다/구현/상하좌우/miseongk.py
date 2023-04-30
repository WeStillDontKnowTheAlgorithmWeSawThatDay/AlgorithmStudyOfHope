n = int(input())
direction = list(map(str, input().split()))

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

direction_index = {
    "L": 0,
    "R": 1,
    "U": 2,
    "D": 3
}

x, y = 1, 1

for d in direction:
    if d not in direction_index:
        continue
    index = direction_index.get(d)

    nx = x + dx[index]
    ny = y + dy[index]
    if nx < 1 or ny < 1 or nx >= n or ny >= n:
        continue

    x = nx
    y = ny

print(x, y)
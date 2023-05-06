n, m = map(int, input().split())

ice = []
for _ in range(n):
    ice.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(ice, x, y):
    if ice[x][y] == 1:
        return
    
    ice[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if ice[nx][ny] == 0:
            dfs(ice, nx, ny)

cnt = 0
for i in range(n):
    for j in range(m):
        if ice[i][j] == 1:
            continue
        dfs(ice, i, j)
        cnt += 1

print(cnt)

# 책 풀이
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
    
#     if ice[x][y] == 0:
#         ice[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
    
#     return False

# nt = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             cnt += 1
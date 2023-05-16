n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(visited, current_x, current_y):
    if not visited[current_x][current_y]:
        print(current_x, current_y, visited[current_x][current_y])

        visited[current_x][current_x] = 1
        for x, y in xy:
            new_x = current_x + x
            new_y = current_y + y
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue
            dfs(visited, new_x, new_y)



count = 0
for x in range(n):
    for y in range(m):
        if not graph[x][y]:
            dfs(graph, x, y)
            count += 1

print(count)


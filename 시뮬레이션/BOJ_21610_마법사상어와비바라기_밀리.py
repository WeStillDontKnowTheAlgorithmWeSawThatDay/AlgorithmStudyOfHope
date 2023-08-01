from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

flag = [[False] * n for _ in range(n)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

queue = deque()
# 초기 구름 위치
queue.append((n-1, 0))
queue.append((n-1, 1))
queue.append((n-2, 0))
queue.append((n-2, 1))
cloud_cnt = 4

for _ in range(m):
    d, s = map(int, input().split())
    # d 방향으로 s칸 이동
    for _ in range(cloud_cnt):
        q = queue.popleft()
        nx = (q[0] + dx[d] * s) % n
        ny = (q[1] + dy[d] * s) % n
        if nx < 0:
            nx += n
        if ny < 0:
            ny += n
        if nx >= n:
            nx -= n
        if ny >= n:
            ny -= n
        arr[nx][ny] += 1
        queue.append((nx, ny))
        # 구름이 사라진 칸 기록
        flag[nx][ny] = True

    for _ in range(cloud_cnt):
        cnt = 0
        q = queue.popleft()
        # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수 구하기
        for i in (-1, -1), (-1, 1), (1, -1), (1, 1):
            nx = q[0] + i[0]
            ny = q[1] + i[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] > 0:
                cnt += 1
        # 물이 있는 바구니 수 만큼 물의 양 증가
        arr[q[0]][q[1]] += cnt
    cloud_cnt = 0
    # 구름이 사라진 칸을 제외하고 물의 양이 2 이상인 모든 칸에 구름이 생김
    for i in range(n):
        for j in range(n):
            if flag[i][j] == True:
                flag[i][j] = False
            else:
                if arr[i][j] >= 2:
                    arr[i][j] -= 2
                    queue.append((i, j))
                    cloud_cnt += 1

s = 0
for i in range(n):
    s += sum(arr[i])
print(s)
n, m = map(int, input().split())
a, b, d = map(int, input().split())

place = []
for i in range(n):
    place.append(list(map(int, input().split())))

# 북, 동, 남, 서
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def turn_left(d):
    if d == 0:
        d = 3
    else:
        d -= 1

    return d

cnt = 1
while True:
    flag = 0
    place[a][b] = 1
    for i in range(4):
        d = turn_left(d)
        if place[a + direction[d][0]][b + direction[d][1]] == 0:
            a += direction[d][0]
            b += direction[d][1]
            cnt += 1
            flag = 1
            break

    # 한 바퀴 회전했는지 확인
    if flag == 1:
        continue

    # 뒤로 한 칸 이동할 때 갈 수 없으면 멈춤
    if place[a - direction[d][0]][b - direction[d][1]] == 1:
        break
    else:
        a -= direction[d][0]
        b -= direction[d][1]
        cnt += 1

print(cnt)

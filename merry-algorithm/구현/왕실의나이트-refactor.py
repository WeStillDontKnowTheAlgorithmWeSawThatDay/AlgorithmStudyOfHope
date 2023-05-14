steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]  # 이동 가능한 방향
location = input()
x = int(location[1])  # 현재 위치 (행)
y = int(ord(location[0])) - int(ord('a')) + 1  # 현재 위치 (열)

count = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)

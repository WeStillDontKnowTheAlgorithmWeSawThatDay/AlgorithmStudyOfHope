n = int(input())
arr = input().split(" ")

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
position = ['L', 'R', 'U', 'D']

currentX = 1
currentY = 1

for a in arr:
    idx = position.index(a)
    if 1 <= currentX + x[idx] <= n:
        currentX = currentX + x[idx]
    else:
        continue
    if 1 <= currentY + y[idx] <= n:
        currentY = currentY + y[idx]
    else:
        continue

print(currentY, currentX)

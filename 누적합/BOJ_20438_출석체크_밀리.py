import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = set(map(int, input().split()))
student = set(map(int, input().split()))

student = student - sleep

sum = [0] * (n + 3)
for i in range(3, n + 3):
    if i in sleep:
        sum[i] = sum[i-1] + 1
        continue

    sum[i] = sum[i-1] + 1
    for j in student:
        if i % j == 0:
            sum[i] -= 1
            break

for i in range(m):
    x, y = map(int, input().split())
    print(sum[y] - sum[x-1])

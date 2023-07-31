input = __import__('sys').stdin.readline
n, x = map(int, input().split())
arr = [*map(int, input().strip().split())]
count = 1

sum = sum(arr[0:x])
max = sum
for i in range(0, n - x):
    sum = sum - arr[i] + arr[i + x]
    if sum > max:
        max = sum
        count = 1
    elif max == sum:
        count += 1

res = str(max) + "\n" + str(count) if max > 0 else "SAD"
print(res)

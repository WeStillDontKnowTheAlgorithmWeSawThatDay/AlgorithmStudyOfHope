k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in arr:
        if x >= mid:
            total += x // mid

    if total < n:
        end = mid - 1
    else:
        result = max(result, mid)
        start = mid + 1

print(result)
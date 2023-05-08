n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

min_list = []
for i in range(n):
    arr[i].sort()
    min_list.append(arr[i][0])

print(max(min_list))

# 책 풀이
# result = 0
# for _ in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)

# print(result)
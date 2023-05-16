# 개선 - 배수가 될 때까지 빼는 작업을 제거하면 반복문을 줄일 수 있음

n, k = map(int, input().split())
count = 0

if n % k > 0:
    count += n % k
    n -= count

count += n // k

print(count)

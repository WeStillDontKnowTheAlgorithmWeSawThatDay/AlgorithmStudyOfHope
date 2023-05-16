n, k = map(int, input().split())
count = 0

while n != 1:
    count += 1
    if n % k == 0:
        n //= k
        continue
    n -= 1

print(count)

# 최소 횟수로 연산을 수행하여 n을 1로 만든다.
# n이 k의 배수일 때만 n//k
# n이 k의 배수가 아니라면 n -1 또는 n//k


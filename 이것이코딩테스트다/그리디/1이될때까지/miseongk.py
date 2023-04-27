n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    
    cnt += 1

print(cnt)

# 책 풀이 -> 시간 복잡도가 더 줄어든다. 나누어떨어지기 전까지 1씩 빼는것이 아니라 한번에 빼기 때문
# while True:
#     target = n - n % k
#     cnt += (n - target)
#     n = target

#     if n < k:
#         break

#     cnt += 1
#     n //= k

# cnt += (n - 1)
# print(cnt)
import math

n = int(input())

dp = [0] * 500001
dp[1] = 1
for i in range(1, n+1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
        current = i
        current_sqrt = math.sqrt(i)
    else:
        c = current_sqrt
        dp[i] = 1 + dp[i - current]
        while c > 0:
            c = c - 1
            dp[i] = min(dp[i], 1 + dp[int(i - c**2)])
            if dp[i] == 2:
                break

print(dp[n])


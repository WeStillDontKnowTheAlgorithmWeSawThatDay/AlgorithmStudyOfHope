n, x = map(int, input().split())
visitors = list(map(int, input().split()))

start, end = 0, x - 1
sum = sum(visitors[0:x])
max = sum
cnt = 1
for i in range(x, len(visitors)):
    sum -= visitors[i - x]
    sum += visitors[i]
    if sum == max:
        cnt +=1 
    elif sum > max:
        max = sum
        cnt = 1

if max == 0:
    print("SAD")
else:
    print(max)
    print(cnt)
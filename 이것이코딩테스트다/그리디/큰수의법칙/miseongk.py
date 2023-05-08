n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

max = numbers[0]
max_second = numbers[1]

count = int(m / (k + 1)) * k
count += m % (k + 1)

sum = count * max + (m - count) * max_second

# sum = (max * k + max_second) * (m // (k + 1)) + (m % (k + 1)) * max

print(sum)

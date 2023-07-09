import itertools

while True:
    numbers = list(map(str, input().split()))
    if numbers[0] == "0":
        break
    numbers = numbers[1:]

    for result in itertools.combinations(numbers, 6):
        print(' '.join(result))
    print()

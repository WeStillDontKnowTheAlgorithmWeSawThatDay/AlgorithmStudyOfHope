import itertools


def find_combinations(numbers):
    numbers = numbers[1:]

    for s in itertools.combinations(numbers, 6):
        print(*s)


while True:
    array = input()

    if array == '0':
        break

    find_combinations(list(array.split()))
    print()

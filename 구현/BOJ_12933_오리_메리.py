quack = ["q", "u", "a", "c", "k"]

count = []
indexToDelete = []

alphabet = input()
index = 0
hasAny = False
count = 0

for a in alphabet:
    if quack.index(index) == a:
        indexToDelete.append(alphabet.index(a))
    else:
        if hasAny:
            count += 1

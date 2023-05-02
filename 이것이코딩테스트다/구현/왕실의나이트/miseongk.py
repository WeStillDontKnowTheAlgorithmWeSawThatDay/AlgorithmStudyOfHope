pos = input()

column_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd':4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8 
}

column = column_dict.get(pos[0])
row = int(pos[1])

case_x = [1, 1, 2, 2, -1, -1, -2, -2]
case_y = [2, -2, 1, -1, 2, -2, 1, -1]

cnt = 0
for i in range(8):
    nx = case_x[i] + row
    ny = case_y[i] + column

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    cnt += 1

print(cnt)


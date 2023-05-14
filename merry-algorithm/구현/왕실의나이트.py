cols = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
location = input()
x, y = int(location[1]), cols.index(location[0])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_types = ['L', 'R', 'D', 'U']
cases = ['LLD', 'LLU', 'RRU', 'RRD', 'UUL', 'UUR', 'DDL', 'DDR']

count = 0
for case in cases:
    nx = x
    ny = y
    for c in case:
        for i in range(4):
            if c == move_types[i]:
                nx += dx[i]
                ny += dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)

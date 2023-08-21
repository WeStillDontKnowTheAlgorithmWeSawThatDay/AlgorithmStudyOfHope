n = int(input())
keys = []
options = []
completed = [False] * n
for i in range(n):
    options.append(list(map(str, input().split())))

for i in range(n):
    # 1단계
    for j in range(len(options[i])):
        if options[i][j][0].lower() in keys:
            continue
        else:
            keys.append(options[i][j][0].lower())
            options[i][j] =  '[' + options[i][j][0] + ']' + options[i][j][1:]
            completed[i] = True
            break
    # 2단계 
    for j in range(len(options[i])):
        if completed[i] == True:
            break
        for h in range(len(options[i][j])):
            if options[i][j][h].lower() in keys:
                continue
            else:
                keys.append(options[i][j][h].lower())
                options[i][j] = options[i][j][:h] + '[' + options[i][j][h] + ']' + options[i][j][h+1:]
                completed[i] = True
                break

for i in range(n):
    for j in options[i]:
        print(j, end=" ")
    print()
 
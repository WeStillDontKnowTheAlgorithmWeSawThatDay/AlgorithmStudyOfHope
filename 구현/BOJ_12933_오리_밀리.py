quack = input()

crying = {"q": "k","u": "q", "a": "u", "c": "a", "k": "c"}
duck = -1
duck_list = [[] for _ in range(len(quack))]
inValid = False
for i in quack:
    flag = 0
    if i == "q":
        for j in duck_list:
            if len(j) == 0:
                duck += 1
                duck_list[duck].append(i)
                break
            if j[-1] == crying.get(i):
                j.append(i)
                break
    elif i == "u" or i == "a" or i == "c" or i == "k":
        for j in duck_list:
            if len(j) == 0:
                continue
            if j[-1] == crying.get(i):
                j.append(i)
                flag = 1
                break
        if flag == 0:
            inValid = True
            break
            
for j in duck_list:
    if len(j) % 5 != 0:
        inValid = True
        
if inValid is True:
    print(-1)
else:    
    print(duck+1)

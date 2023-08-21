def findWinner():
    board = []
    for i in range(19):
        board.append(list(map(int, input().split())))

    # 동북, 동, 동남, 남
    dx = [-1, 0, 1, 1]
    dy = [1, 1, 1, 0]

    for x in range(19):
        for y in range(19):
            if board[x][y] == 0:
                continue
            current = board[x][y]
            # 총 4 방향에 대해서 확인
            for i in range(4):
                flag = 0
                nx, ny = x, y
                # 바둑알의 색이 현재 위치에서 총 5개까지 일치하는지 확인
                for _ in range(4):
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
                        flag = 1
                        break
                    if board[nx][ny] != current:
                        flag = 1
                        break
                # 다음 6번째 알이 일치하면 이긴 것이 아님
                nx = nx + dx[i]
                ny = ny + dy[i]
                if 0 <= nx < 19 and 0 <= ny < 19:
                    if board[nx][ny] == current:
                        flag = 1
                # 이전 알이 일치하면 이긴 것이 아님
                nx = x - dx[i]
                ny = y - dy[i]
                if 0 <= nx < 19 and 0 <= ny < 19:
                    if board[nx][ny] == current:
                        flag = 1
                if flag == 0:
                    print(current)
                    print(x+1, y+1)
                    return
    print(0)
                
findWinner()

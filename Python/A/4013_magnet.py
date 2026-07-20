T = int(input())
for test in range(1, T+1):
    K = int(input())
    mat = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        num, turn = map(int, input().split())
        num -= 1
        # 0 : N, 1: S
        # 2번 인덱스: 6번인덱스 비교

        # 톱날을 돌릴지 말지 판단.
        visited = [False]*4
        # 현재 톱날 회전
        visited[num] = True
        # 현재 톱날 기준 오른쪽 회전 여부
        for i in range(num, 3):
            if mat[i][2] != mat[i+1][6]:
                visited[i+1] = True
        # 현재 톱날 기준 왼쪽 회전 여부
        for i in range(num, 0, -1):
            if mat[i][6] != mat[i-1][2]:
                visited[i-1] = True
        
        # 현재 visited가 True이면 회전한다.  
        turn_now = turn
        # 현재 기준 오른쪽 회전시키기
        for i in range(num, 4):
            if visited[i]:
                # 시계방향
                if turn_now == 1:
                    temp = mat[i][7]
                    for j in range(1, 8):
                        mat[i][j] = mat[i][j-1]
                    mat[i][0] = temp
                # 반시계 방향
                else:
                    temp = mat[i][0]
                    for j in range(7):
                        mat[i][j] = mat[i][j-1]
                    mat[i][7] = temp
                turn_now = turn_now*(-1)
            else:
                break
        # 현재 기준 왼쪽 회전시키기
        turn_now = turn
        for i in range(num, -1, -1):
            if visited[i]:
                # 시계방향
                if turn_now == 1:
                    temp = mat[i][7]
                    for j in range(1, 8):
                        mat[i][j] = mat[i][j-1]
                    mat[i][0] = temp
                # 반시계 방향
                else:
                    temp = mat[i][0]
                    for j in range(7):
                        mat[i][j] = mat[i][j-1]
                    mat[i][7] = temp
                turn_now = turn_now*(-1)
            else:
                break
    ans = 0
    for i in range(4):
        if mat[i][0] == 1:
            ans += 2**i
    print(F"#{test} {ans}")


'''
1
2
1 0 0 1 0 0 0 0
0 1 1 1 1 1 1 1
0 1 0 1 0 0 1 0
0 1 0 0 1 1 0 1
3 1
1 1
'''
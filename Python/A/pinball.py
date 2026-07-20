# dfs

# 벽 바깥
def in_range(y, x):
    return 0<= y < N and 0<= x < N





T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 4방향 델타
    # 동 남 서 북
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    # 블록
    # 들어오는 방향 두개 입력
    dic = {
        1:[1, 2],
        2:[2, 3],
        3:[0, 3],
        4:[0, 1],
        5:[0, 1, 2, 3],
    }
    # 최대점수
    max_score = 0
    # 시작점 설정
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:

                for d in range(4):
                    cur_d = d
                    score = 0
                    s_i = i
                    s_j = j
                    while True:
                        ny = s_i + dy[cur_d]
                        nx = s_j + dx[cur_d]
                        # print(ny, nx)
                        # 벽에 닿을시 방향 전환
                    
                        if not in_range(ny, nx):
                            cur_d = (cur_d + 2) % 4
                            score += 1
                            # 벽에 닿았을 때 값 옮기면 이상해질까봐 냅뒀는데
                            # 오히려 이게 더 문제를 키웠음.
                            # 다음 시행에서 블럭의 진입 방향이 이상해졌다.
                            # 이외엔 AI 사용 X
                            s_i = ny
                            s_j = nx
                            continue
                        # 웜홀
                        elif mat[ny][nx] in (6, 7, 8, 9, 10):
                            hole_num = mat[ny][nx]
                            # valid = True
                            for y in range(N):
                                for x in range(N):
                                    # 웜홀 번호가 같으며 자기 자신 번호는 제외 해야한다.
                                    if mat[y][x] == hole_num and (ny, nx) != (y, x):
                                        s_i = y
                                        s_j = x
                                        valid = False
                                        break # for x
                            #     if not valid:
                            #         break # for y
                            # continue
                        # 사각 블럭에 닿을 시
                        elif mat[ny][nx] in (1, 2, 3, 4, 5):
                            # 무조건 벽에 닿이니 방향 저장 및 점수 +1
                            s_i = ny
                            s_j = nx
                            score += 1
                            if mat[ny][nx] == 5:
                                cur_d = (cur_d + 2) % 4
                                s_i = ny
                                s_j = nx
                            # 삼각 블럭에 닿을시
                            #1
                            elif mat[ny][nx] == 1:
                                # print('zz')
                                if cur_d in dic[1]:
                                    if cur_d == 1:
                                        cur_d = 0
                                    else: 
                                        cur_d = 3
                                else:
                                    cur_d = (cur_d +2) % 4
                            #2
                            elif mat[ny][nx] == 2:
                                if cur_d in dic[2]:
                                    if cur_d == 2:
                                        cur_d = 1
                                    else: 
                                        cur_d = 0
                                else:
                                    cur_d = (cur_d +2) % 4
                            #3
                            elif mat[ny][nx] == 3:
                                if cur_d in dic[3]:
                                    if cur_d == 3:
                                        cur_d = 2
                                    else: 
                                        cur_d = 1
                                else:
                                    cur_d = (cur_d +2) % 4
                            #4
                            elif mat[ny][nx] == 4:
                                if cur_d in dic[4]:
                                    if cur_d == 0:
                                        cur_d = 3
                                    else: 
                                        cur_d = 2
                                else:
                                    cur_d = (cur_d +2) % 4
                        else:
                            s_i = ny
                            s_j = nx
                        # 종료 조건
                        if (ny, nx) == (i, j) or mat[ny][nx] == -1:
                            break# while True
                    max_score = max(score, max_score)
                    # print(max_score)
    print(F"#{test} {max_score}")





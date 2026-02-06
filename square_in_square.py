T = int(input())
for test in range(1, T + 1):
    N, M =map(int, input().split())
    matrix = [[0]*N for _ in range(N)]

    # 완전 탐색
    cnt = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt += 1
            # 순회로 해당 영역 값 채우기
            for p in range(i, i + M):
                for q in range(j, j + M):
                    matrix[p][q] = cnt
            # for p in range(M):
            #     for q in range(M):
            #         matrix[i+p][j+q] = cnt
    print(f"#{test}")
    for i in range(N):
        print(*matrix[i])




    # 델타 이용 해당 방향에 일치하는 값이 있는지
    # N, M = map(int, input().split())
    # matrix = [[0] * N for _ in range(N)]]
    # 
    # dy = [0]*2* M
    # dx = [0]*2* M
    # for i in range(2*M):
    #
    # cnt = 0
    # #완전탐색
    # for i in range(N - M + 1):
    #     for j in range(N - M + 1):
    #         # 델타로 해당 방향 진행 후 탐색
    #         cnt += 1
    #         for ny, nx in zip(dy, dx):
    #             if
    #
    # print(ans)
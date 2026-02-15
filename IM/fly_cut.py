T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]


    # 델타 상하좌우
    dy1 = [1, -1, 0, 0]
    dx1 = [0, 0, 1, -1]
    # 델타 대각
    dy2 = [1, -1, 1, -1]
    dx2 = [1, -1, -1, 1]

    # 인덱스 밖 제외
    def in_range(y,x):
        return 0<=y < N and 0<= x <N
    
    # 최댓값 계산
    max_kill = 0
    # 완전 탐색
    for i in range(N):
        for j in range(N):
            # 가로세로
            s1 = matrix[i][j]
            # 대각 방향
            s2 = matrix[i][j]
            for d in range(4):
                for m in range(M):
                    #가로세로
                    ny1 = i + dy1[d]
                    nx1 = j + dx1[d]
                    #대각 방향
                    ny2 = i + dy2[d]
                    nx2 = j + dx2[d]
                #가로 세로
                if in_range(ny1, nx1):
                    s1 += matrix[ny1][nx1]
                # 대각
                if in_range(ny2, nx2):
                    s2 += matrix[ny2][nx2]
            if max_kill < s1 or max_kill < s2:
                max_kill = max(max_kill, s1, s2)
    print(F"#{test} {max_kill}")
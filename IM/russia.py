T = int(input())
for test in range(1, T +1):
    N, M = map(int, input().split())
    russia = [list(input()) for _ in range(N)]



    # 0: i 흰
    # i+1:j+1 파
    # j+1 : N  빨
    # 까지 3개구간 구분 
    min_cnt = float('inf')
    cnt = 0
    # 인덱스 생각하여 N - 2, N -1 로 범위 설정 
    # 마지막 j 번째 이후로 하나의 빨간색이 있어야 한다.
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for w in range(i+1):
                for m in range(M):
                    if russia[w][m] != 'W':
                        cnt += 1
            for b in range(i+1, j+1):
                for m in range(M):
                    if russia[b][m] != 'B':
                        cnt += 1
            for r in range(j+1, N):
                for m in range(M):
                    if russia[r][m] != 'R':
                        cnt += 1
            min_cnt = min(cnt, min_cnt)
            # print(cnt, min_cnt)
            # print(i, j)
    print(F"#{test} {min_cnt}")

def in_range(y, x):
    return 0<= y < N and 0<= x < M

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                d = 0
                cnt = 0
                # 오른쪽 행 탐색
                while in_range(i, j+d) and mat[i][j+d] == 1:
                    cnt += 1
                    d += 1
                max_cnt = max(max_cnt, cnt)

                d = 0
                cnt = 0
                # 세로 탐색
                while in_range(i+d, j) and mat[i+d][j] == 1:
                    cnt += 1
                    d += 1
                max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")

'''
원리는 가로로 행 우선 탐색 중 1을 발견하면 해당 1로부터 오른쪽과 아래로 탐색하여 최대 길이값이라면 갱신한다.
완전탐색을 왼쪽 위부터 오른쪽으로 이동하며 탐색하기 떄문에 가능하다.
'''


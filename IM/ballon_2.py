T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split()) # N M 행 렬
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dj = [1, 0, -1, 0]
    di = [0, 1, 0, -1]
    max_pollen = 0
    for i in range(N):
        for j in range(M):

            s = matrix[i][j]

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < M:
                    s += matrix[ni][nj]

            if max_pollen <= s:
                max_pollen = s
    print(f"#{test} {max_pollen}")
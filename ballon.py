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
            sum_ = matrix[i][j]

            for d in range(4): # 지금은 한쪽 방향으로 s칸 간 후 방향 변경
                for k in range(1,s+1): # 방향별로 한칸씩 가고 싶으면 두 for문 위치 변경
                    ni = i + di[d]*k
                    nj = j + dj[d]*k
                    if 0 <= ni < N and 0 <= nj < M:
                        sum_ += matrix[ni][nj]

            if max_pollen <= sum_:
                max_pollen = sum_
    print(f"#{test} {max_pollen}")
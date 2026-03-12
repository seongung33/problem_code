T = int(input())

# 델타
dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

# 인덱스 에러
def in_range(y, x):
    return 0 <= y < N and 0<=x < N



def dfs(i, j, d, cnt):
    global max_cnt
    if d == 3 and si== i and sj == j:
        max_cnt = max(cnt, max_cnt)
        return
    # print(i, j)

    if d > 3:
        return

    # for d in range(4):
    ny = i + dy[d]
    nx = j + dx[d]
    if in_range(ny, nx):
        if not mat[ny][nx] in visit:
            visit.append(mat[ny][nx])
            dfs(ny, nx, d+1, cnt + 1)
            dfs(ny, nx, d, cnt +1)
            visit.pop()

for test in range(1, T+1):
    N = int(input())
    mat =[list(map(int, input().split())) for _ in range(N)]

    max_cnt = -1

    for i in range(N):
        for j in range(N):
            si = i
            sj = j
            visit = []
            dfs(i, j, 0, 0)
    # si = 0
    # sj = 0
    # visit = []
    # dfs(0, 0, 0, 0)
    print(F"#{test} {max_cnt}")



    
T = int(input())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def starts():
    global h
    for i in range(N):
        for j in range(N):
            h = max(mat[i][j], h)

    for i in range(N):
        for j in range(N):
             if mat[i][j] == h:
                start.append((i, j))

def in_range(y, x):
    return 0 <= y < N and 0<= x < N

# 이 위로는 문제 없는듯 
# 예외 케이스가 있나?
def dfs(i, j, cnt, gongsa):
    # print(i, j, cnt)
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]

        if in_range(ny, nx):
            if mat[ny][nx] < mat[i][j] and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx, cnt+1, gongsa)
                visited[ny][nx] = False

            if gongsa and (mat[ny][nx] - K < mat[i][j]) and (not visited[ny][nx]):
                temp = mat[ny][nx]
                # mat[ny][nx] = mat[i][j] - 1
                for q in range(K+1):
                    if mat[ny][nx] - q < mat[i][j]:
                        a = q
                        break # for q
                mat[ny][nx] -= a
                visited[ny][nx] = True
                dfs(ny, nx, cnt + 1, False) 
                visited[ny][nx] = False
                # mat[ny][nx] = mat[i][j]
                mat[ny][nx] += a

for test in range(1, T+1):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0


    h = 0
    start = []
    starts()
    # print(start)
    for i, j in start:
        visited = [[False]*N for _ in range(N)]
        visited[i][j] = True
        dfs(i, j, 1, True)


    print(F"#{test} {max_cnt}")


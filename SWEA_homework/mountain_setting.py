T = int(input())

def in_range(y, x):
    return 0<= y < N and 0 <= x < N

def start():
    start_lst = []
    max_num = 0
    for i in range(N):
        for j in range(N):
            if max_num < mat[i][j]:
                max_num = mat[i][j]
    
    for i in range(N):
        for j in range(N):
            if mat[i][j] == max_num:
                start_lst.append((i, j))
    return start_lst

def dfs(y, x, cnt, valid):
    # print(y, x, cnt)
    global max_len
    if max_len < cnt:
        max_len = cnt

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx):
            if not visited[ny][nx]:
                if mat[ny][nx] < mat[y][x]:

                    visited[ny][nx] = 1
                    dfs(ny, nx, cnt+1, valid)
                    visited[ny][nx] = 0

                elif valid:
                    if mat[ny][nx] - mat[y][x] < K:
                        temp = mat[ny][nx]
                        mat[ny][nx] = mat[y][x] -1
                        visited[ny][nx] = 1
                        dfs(ny, nx, cnt +1, False)
                        mat[ny][nx] = temp
                        visited[ny][nx] = 0
    



dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for test in range(1, T+1):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    start_lst = start()


    max_len = 0
    for y, x in start_lst:
        visited = [[0]*(N) for _ in range(N)]
        visited[y][x] = 1
        dfs(y, x, 1, True)
        # print('최댓값', max_len)
    print(f"#{test} {max_len}")
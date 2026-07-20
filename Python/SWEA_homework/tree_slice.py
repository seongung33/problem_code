T = int(input())

def start():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'X':
                return i, j
def end():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'Y':
                return i, j

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0<= y < N and 0 <= x < N
# 좌표, 회전 수, 나무 베기 수
def dfs(y, x, cnt, k, nd):
    global min_cnt
    if cnt >=min_cnt:
        return
    
    if k > K:
        return

    if y == end_point[0] and  x == end_point[1]:
        min_cnt = min(cnt, min_cnt)
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx):
            if visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            if mat[ny][nx] == 'T':
                if nd == d:
                    dfs(ny, nx, cnt+1, k+1, d)
                elif (nd+2) % 4 == d:
                    dfs(ny, nx, cnt+3, k+1, d)
                else:
                    dfs(ny, nx, cnt+2, k+1, d)
            else:
                if nd == d:
                    dfs(ny, nx, cnt+1, k, d)
                elif (nd+2) % 4 == d:
                    dfs(ny, nx, cnt+3, k, d)
                else:
                    dfs(ny, nx, cnt+2, k, d)
            visited[ny][nx] = 0
                    
    

for test in range(1, T+1):
    N, K = map(int, input().split())
    mat = [list(input().strip()) for _ in range(N)]
    nd = 0
    min_cnt = float('inf')
    end_point = end()
    sy, sx = start()
    # print(dic[nd])
    visited = [[0]*N for _ in range(N)]
    dfs(sy, sx, 0, 0, 0)
    if min_cnt == float('inf'):
        min_cnt = -1
    print(F"#{test} {min_cnt}")

    # print(sy, sx)
    # print(end_point)
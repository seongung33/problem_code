
# 델타
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def dfs(si, sj):
    global cnt, max_cnt
    s= 0
    valid = True
    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0:
                valid = False
                break
        if not valid:
            break
    else:
        max_cnt = min(max_cnt, cnt)
        return
    for d in range(4):
        ny = si + dy[d]
        nx = sj + dx[d]
        if in_range(ny, nx):
            print(ny, nx)
            if mat[ny][nx] > 0:
                lst.append(mat[ny][nx])
                base = mat[ny][nx]
                mat[ny][nx] = 0
                cnt += 1
                dfs(ny, nx)
                cnt -= 1
                mat[ny][nx] = base
                lst.pop()

            elif mat[ny][nx] < 0:
                if mat[ny][nx] in lst:
                    base2 = mat[ny][nx]
                    mat[ny][nx] = 0
                    cnt += 1
                    dfs(ny, nx)
                    cnt -= 1
                    mat[ny][nx] = base2
            # else:
                # cnt += 1
                # dfs(ny, nx)
                # cnt -= 1




T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(mat)
    s = 0
    # 괴물 처치 리스트
    lst = []
    cnt = 0
    max_cnt = float('inf')
    dfs(0, 0)
    print(mat)
    print(F"#{test} {max_cnt}")


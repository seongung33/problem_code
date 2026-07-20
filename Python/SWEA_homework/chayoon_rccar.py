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


for test in range(1, T+1):
    # 크기
    N = int(input())
    #지도
    mat = [list(input().strip()) for _ in range(N)]
    #조종 횟수 Q
    Q = int(input())
    q_lst = [[] for _ in range(Q)]
    for i in range(Q):
        num, q_lst[i] =input().split()
    # print(q_lst)


    ans = []

    ey, ex = end()
    for i in q_lst:
        nd = 0
        sy, sx = start()
        for j in i:
            # print(sy, sx, nd, j)
            if j == 'R':
                nd = (nd + 1) % 4
            elif j == 'L':
                if nd == 0:
                    nd = 3
                else:
                    nd = nd - 1
            else:
                ny = sy + dy[nd]
                nx = sx + dx[nd]
                if in_range(ny, nx):
                    if mat[ny][nx] == 'T':
                        continue
                    sy, sx = ny, nx
        if sy == ey and sx == ex:
            ans.append(1)
        else:
            ans.append(0)
        # print("마지막", sy, sx)

    print(f"#{test}", *ans)

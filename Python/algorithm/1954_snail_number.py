T = int(input())

def in_range(y, x):
    return 0<= y < N and 0<= x < N


for test in range(1, T+1):
    N = int(input())
    mat = [[0]*N for _ in range(N)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y = 0
    x = 0
    d = 0
    cnt = 1
    mat[y][x] = cnt
    while cnt < N*N:
        ny = dy[d] + y 
        nx = dx[d] + x
        if not in_range(ny, nx) or mat[ny][nx] != 0:
            d += 1
            if d > 3:
                d = 0
        else:
            y = ny 
            x = nx 
            cnt += 1
            mat[y][x] = cnt
    
    print(F"#{test}")
    for i in range(N):
        print(*mat[i])
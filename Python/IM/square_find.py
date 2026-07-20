# 인덱스 범위 조정
def in_range(y, x):
    return 0<= y < N and 0<= x < N

T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    square = []
    y1 = x1 = -1
    for i in range(N):
        for j in range(N):
            if i <y1 and j < x1:
                continue

            if mat[i][j] == 1:
                square.append([i, j])
                d = 0
                # y1 = i
                # x1 = j
                while in_range(i,j+d) and mat[i][j+d] == 1:
                    x1 = j+d
                    if mat[i][j+d] != 1:
                        x1= j+d
                        break # while True
                    d += 1
                d = 0
                while in_range(i+d,j) and mat[i+d][j] ==1:
                    y1 = i+d
                    if mat[i+d][j] != 1:
                        mat[i+d][j] += 1
                        break # while True
                    d += 1
                square.append([y1, x1])
                
    # print(square)
    n = len(square)
    max_extent = 0
    extent = 0
    for i in range(0, n, 2):
        extent = (abs(square[i][0] -square[i+1][0])+1)*(abs(square[i][1] -square[i+1][1])+1)
        max_extent = max(max_extent, extent)
    print(F"#{test} {max_extent}")
  
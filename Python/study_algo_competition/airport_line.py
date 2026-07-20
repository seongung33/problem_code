T = int(input())

def in_range(y, x):
    return 0<= y < N and 0<=x < N

def gun_right(y, x, visited):
    base = mat[y][x]
    for i in range(X):
        if in_range(y, x+i):
            return False
        if visited[x+i]:
            return False
        if base != mat[y][x+i]:
            return False
    return True




for test in range(1, T+1):
    N, X = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]


    row_v = [False]*N
    cnt = 0

    # 가로 계산
    for i in range(N):
        visited = [False]*N
        ans = True
        for j in range(1, N):


            if abs(mat[i][j-1] - mat[i][j]) > 1:
                ans = False

            if mat[i][j-1] + 1 == mat[i][j] :
                # print(i, j, '오른쪽이 큼')
                p = mat[i][j-1]
                for q in range(j-1, j-1-X, -1):
                    if in_range(i, q) and not visited[q] and p ==mat[i][q]:
                        visited[q] = True
                    else:
                        ans = False
                        break

            if mat[i][j-1] == mat[i][j] + 1:
                # print(i, j, '왼쪽이 큼')
                p = mat[i][j]
                for q in range(j, j+X):
                    if in_range(i, q) and not visited[q] and p ==mat[i][q]:
                        visited[q] = True
                    else:
                        ans = False
                        break
        if ans:
            # print(i, '행')
            cnt += 1

    # 세로 계산
    for j in range(N):
        visited = [False]*N
        ans = True
        for i in range(1, N):

            if abs(mat[i-1][j] - mat[i][j]) > 1:
                ans = False

            if mat[i-1][j]+1 == mat[i][j]:
                p = mat[i-1][j]
                # print(i, j, '뒤쪽 탐색')
                for q in range(i-1, i-1-X, -1):
                    if in_range(j, q) and not visited[q] and p == mat[q][j]:
                        visited[q] = True
                    else:
                        ans = False
                        break

            if mat[i-1][j] == mat[i][j]+1:
                # print(i, j, '정면 탐색')
                p = mat[i][j]
                for q in range(i, i+X):
                    if in_range(j, q) and not visited[q] and p == mat[q][j]:
                        visited[q] = True
                    else:
                        ans = False
                        break
        if ans:
            # print(j, '열')
            cnt += 1
    print(F"#{test} {cnt}")
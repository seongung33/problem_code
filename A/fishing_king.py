import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# 방향: 위, 아래, 오른쪽, 왼쪽
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

# 상어 정보: [r, c, s, d, z]
shark_info = [[] for _ in range(M)]
mat = [[0] * C for _ in range(R)]

# 입력
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1 
    shark_info[i] = [r, c, s, d, z]
    mat[r][c] = (i, z)

answer = 0

# 낚시왕 이동
for fisher in range(C):

    #상어 잡기
    for row in range(R):
        if mat[row][fisher] != 0:
            idx, size = mat[row][fisher]
            answer += size
            shark_info[idx] = [-1, -1, 0, 0, 0]  # 제거
            mat[row][fisher] = 0
            break

    #상어 이동
    new_mat = [[0] * C for _ in range(R)]

    for i in range(M):
        r, c, s, d, z = shark_info[i]

        if r == -1:
            continue

        if d < 2:  
            move = s % (2 * (R - 1)) if R > 1 else 0
        else:   
            move = s % (2 * (C - 1)) if C > 1 else 0

        for _ in range(move):
            nr = r + dy[d]
            nc = c + dx[d]

            if not (0 <= nr < R and 0 <= nc < C):
                # 방향 반전
                if d == 0: d = 1
                elif d == 1: d = 0
                elif d == 2: d = 3
                else: d = 2

                nr = r + dy[d]
                nc = c + dx[d]

            r, c = nr, nc

        shark_info[i] = [r, c, s, d, z]

        if new_mat[r][c] == 0:
            new_mat[r][c] = (i, z)
        else:
            prev_i, prev_z = new_mat[r][c]
            if prev_z < z:
                shark_info[prev_i] = [-1, -1, 0, 0, 0]
                new_mat[r][c] = (i, z)
            else:
                shark_info[i] = [-1, -1, 0, 0, 0]

    mat = new_mat

print(answer)
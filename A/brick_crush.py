#5656 벽돌 깨기
import copy

# 델타
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
# 범위 제한
def in_range(y, x):
    return 0 <= y < H and 0<= x < W

# 블록 내리기
def gravity(matrix):

    for c in range(W):
        col_value = []
        for r in range(H):
            if matrix[r][c] != 0:
                col_value.append(matrix[r][c])
        empty_cnt = H - len(col_value)
        new_column = [0] * empty_cnt + col_value

        for  r in range(H):
            matrix[r][c] = new_column[r]


# 블럭을 하나하나 부수는 것과 연쇄 폭발을 분리하여 dfs 실행
# 재귀 카운팅 dfs
def dfs_shoot(matrix):
    global cnt, min_ans
    valid = True
    for i in range(W):
        for j in range(H):
            if matrix[j][i] != 0:
                valid = False
                break
        if not valid:
            break
    else:
        min_ans = 0
        

    if min_ans == 0:
        return
    if cnt == N:
        ans = 0

        for j in range(W):
            for i in range(H):
                if matrix[i][j] != 0:
                    ans += 1
        min_ans = min(ans, min_ans)
    else:
        for j in range(W):
            for i in range(H):
                if matrix[i][j] != 0:
                    # 블럭 부수기
                    curr_num = matrix[i][j]
                    cnt += 1
                    matrix2 = copy.deepcopy(matrix)
                    dfs_boom(i, j, curr_num, matrix2)
                    gravity(matrix2)
                    dfs_shoot(matrix2)
                    cnt -= 1
                    break




# 재귀? dfs 써서 해봐야 할듯
def dfs_boom(i, j, curr_num, matrix):
    if curr_num == 1:
        matrix[i][j] = 0
        return

    # 재귀
         # 부순 블럭 크기만큼 부수기
    else:
        matrix[i][j] = 0
        for k in range(1, curr_num):
        # 4방향 부수기
            for d in range(4):
                ny = i + dy[d]*k
                nx = j + dx[d]*k
                if in_range(ny, nx):
                    curr_num1 = matrix[ny][nx]
                    matrix[ny][nx] = 0
                    dfs_boom(ny, nx, curr_num1, matrix)

            

T = int(input())#
for test in range(1, T +1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    
    # 카운트 벽돌 날리는 횟수
    cnt = 0
    #남은 벽돌 수
    min_ans = W*H

    dfs_shoot(matrix)
    print(F"#{test} {min_ans}")
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
    # 가로
    for c in range(W):
        col_value = []
        # 세로 즉, 열 우선 순회 (세로)
        for r in range(H):
            # 0이 아니라면
            if matrix[r][c] != 0:
                # col_value에 저장
                col_value.append(matrix[r][c])
        # 0의 길이를 센다.
        empty_cnt = H - len(col_value)
        # 0을 먼저 추가하고 후에 0이 아닌 값을 이어준다.
        new_column = [0] * empty_cnt + col_value

        # 세로의 matrix 값을 위에서 새로만든 column 값으로 바꿔준다.
        # 0 0 0 1 3 4 같은 식으로 세로를 바꿔준다.
        for r in range(H):
            matrix[r][c] = new_column[r]


# 블럭을 하나하나 부수는 것과 연쇄 폭발을 분리하여 dfs 실행
# 재귀 카운팅 dfs
def dfs_shoot(matrix):#
    global cnt, min_ans
    valid = True
    # 모든 블럭을 부숴보며 dfs 탐색한다.

    # 만약 모든 값이 0 이라면 더 이상 부술 게 없기 때문에 재귀를 멈출 수 있다.
    # 또한 모든 블럭을 다 부순다면 N이 증가하지 않아 원하는 값을 출력할 수 없을 것이다.
    for i in range(W):
        for j in range(H):
            if matrix[j][i] != 0:
                valid = False
                break # for j
        if not valid:
            break # for i
    # 모든 값이 0이라면 min_ans를 0으로 바꾼다.
    else:
        min_ans = 0
    # 모든 블럭을 부쉈으면 return 한다.    
    if min_ans == 0:
        return
    # N번 부쉈다면 이 또한 종료조건이다.
    if cnt == N:
        ans = 0
        # 남아있는 블럭의 수를 센다. 이게 최솟값이 정답이다.
        for j in range(W):
            for i in range(H):
                if matrix[i][j] != 0:
                    ans += 1
        min_ans = min(ans, min_ans)
    else:
        # 모든 2차원을 열 우선순회로 돈다.
        for j in range(W):
            for i in range(H):
                # 블럭을 부술 수 있다면.
                if matrix[i][j] != 0:
                    # 블럭 부수기
                    curr_num = matrix[i][j]
                    cnt += 1
                    # 백트레킹시 돌아올 수 없기 때문에 deepcopy로 원본 자료를 살려둔다.
                    matrix2 = copy.deepcopy(matrix)
                    # 연쇄 폭발을 dfs로 구현한다.
                    dfs_boom(i, j, curr_num, matrix2)
                    # 연쇄폭발이 끝났다면 중력을 적용한다.
                    gravity(matrix2)
                    # 다시 재귀한다.
                    dfs_shoot(matrix2)
                    cnt -= 1
                    # 백트레킹 했다면 다음 열로 넘어가야 하기 때문에 break 한다.
                    break




# 재귀? dfs 써서 해봐야 할듯
def dfs_boom(i, j, curr_num, matrix):
    # 1이라면 자기 자신만 부수기 때문에 return 
    # 즉 종료조건이다.
    if curr_num == 1:
        matrix[i][j] = 0
        return

    # 재귀
    # 부순 블럭 크기만큼 부수기
    else:
        matrix[i][j] = 0
        # k 만큼 이동하며 부숴야 한다.
        for k in range(1, curr_num):
            # 4방향 부수기
            for d in range(4):
                ny = i + dy[d]*k
                nx = j + dx[d]*k
                if in_range(ny, nx):
                    curr_num1 = matrix[ny][nx]
                    matrix[ny][nx] = 0
                    # 재귀한다.
                    dfs_boom(ny, nx, curr_num1, matrix)

T = int(input())
for test in range(1, T +1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    
    # 카운트 벽돌 날리는 횟수
    cnt = 0
    #남은 벽돌 수
    min_ans = float('inf')
    # dfs 탐색
    dfs_shoot(matrix)
    print(F"#{test} {min_ans}")
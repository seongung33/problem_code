## 시작지점 탐색
def start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
                return r, c

#인덱스 바깥 제한
def in_range(y, x):
    return 0 <= y <N and 0<= x < N
#델타
# 동 남 서 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


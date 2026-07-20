from collections import deque

N, Q = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(2**N)]
L_lst = list(map(int, input().split()))
n = 2**N

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def rotate(L):
    new_mat= [[0] * n for _ in range(n)]

    s = 2**L
    for i in range(0, n ,s):
        for j in range(0, n, s):
            for x in range(s):
                for y in range(s):
                    new_mat[i + y][j + s - 1 - x] = mat[i + x][j + y]
        
    return new_mat


def melt():
    to_reduce = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                cnt = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] > 0:
                        cnt += 1
                
                # 인접한 얼음이 3개 미만이면 녹을 후보로 등록
                if cnt < 3:
                    to_reduce.append((i, j))

    # 모아둔 좌표의 얼음을 한 번에 감소
    for x, y in to_reduce:
        mat[x][y] -= 1


def bfs():
    visited = [[False] * n for _ in range(n)]
    max_block = 0

    for i in range(n):
        for j in range(n):
            # 얼음이 있고, 아직 방문하지 않은 곳에서 탐색 시작
            if mat[i][j] > 0 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                block_size = 1

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if mat[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                block_size += 1

                max_block = max(max_block, block_size)

    return max_block


for L in L_lst:
    mat = rotate(L)
    melt()

# 결과 출력
total_ice = sum(sum(row) for row in mat)
print(total_ice)
print(bfs())
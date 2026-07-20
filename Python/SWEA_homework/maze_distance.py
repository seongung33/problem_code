# 미로 시작점 찾기
def start():
    for i in range(N):
        for j in range(N):
            if 2 == maze[i][j]:
                return i, j
# 델타
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 인덱스 바깥
def in_range(y, x):
    return 0 <= y < N and 0 <= x < N
#bfs
def bfs(si, sj, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j] - 1 - 1# 경로의 빈 칸 수, -1 추가
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if in_range(ny, nx) and not visited[ny][nx] and maze[ny][nx] != 1:
                q.append([ny, nx])
                visited[ny][nx] = visited[i][j] + 1
    return 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 0은 통로 1은 벽 2는 출발 3은 도착
    si, sj = start()
    ans = bfs(si, sj, N)
    print(F"#{test} {ans}")
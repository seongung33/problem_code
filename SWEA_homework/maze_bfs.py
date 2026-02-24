from collections import deque
N, M = map(int ,input().split())
maze = [input() for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    return 0<= y < N and 0<= x < M

q = deque()
visited = [[0]*M for _ in range(N)]
q.append([0, 0])
visited[0][0] = 1
while q:
    y, x = q.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx) and maze[ny][nx] == '1' and not visited[ny][nx]:
            q.append([ny, nx])
            visited[ny][nx] = visited[y][x] + 1
print(visited[N-1][M-1])


visited = [[0]*M for _ in range(N)]
min_vis = float('inf')
def dfs(i, j):
    if visited[N-1][M-1]:
        visit = visited[N-1][M-1]
        min_vis = min(min_vis, visit)
        return
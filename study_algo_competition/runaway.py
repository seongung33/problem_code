from collections import deque


# 동 서 북 남
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]



T = int(input())
for test in range(1, T+1):
    #세로, 가로, 시작 세로, 시작 가로, 시간
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited[r][c] = 1
        while q:
            y, x = q.popleft()


            for d in range(4):
                
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < M:
                    if mat[ny][nx] == 0:
                        continue
                    if visited[ny][nx] > 0:
                        continue

                    if d == 0 and mat[y][x] in (1, 3, 4, 5) and mat[ny][nx] in (1, 3, 6, 7):
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1    
                    if d == 1 and mat[y][x] in (1, 3, 6, 7) and mat[ny][nx] in (1, 3, 4, 5):
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1
                    if d == 3 and mat[y][x] in (1, 2, 5, 6) and mat[ny][nx] in (1, 2, 4, 7):
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1
                    if d == 2 and mat[y][x] in (1, 2, 4, 7) and mat[ny][nx] in (1, 2, 5, 6):
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1

    bfs(R, C)

    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                continue
            if visited[i][j] <= L:
                ans += 1
    print(f"#{test} {ans}")

    # for i in range(N):
    #     print(visited[i])
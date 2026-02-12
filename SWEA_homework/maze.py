## 시작지점 탐색
def start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
                return r, c

# 도차지점 탐색
# def end():
#     for i in range(N):
#         for j in range(N):
#             if int(maze[i][j]) == 3:
#                 r, c = i, j
#                 return r, c

#인덱스 바깥 제한
def in_range(y, x):
    return 0 <= y <N and 0<= x < N
#델타
# 동 남 서 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# backtracking
# 실패
# 재귀를 쓸 때에는 재귀 자체가 스택이 된다.
# 즉 스택을 쓸필요가 없다.
# 되돌아가는 상황에서는 해당 함수를 종료하라.

# 재귀: 덜어냄의 미학.
# 부족한 점을
# for 문 안의 if visited가 가지치기 중 하나.
# 단 목적지에 도달해도 for문 안에서 다른 방향으로 진입한다.
def maze_runner(r, c):
    global ans
    print(r,c, maze[r][c])
    # 도착했다면 1을 반환하라
    if maze[r][c] ==3:
        ans = 1
        return #ans
    #방향 탐색
    for d in range(4):
        ny = r + dy[d]
        nx = c + dx[d]
        # 인덱스를 벗어나지 않고 벽이 아닌 길이고 방문한 적 없으면
        if in_range(ny, nx) and not visited[ny][nx] and maze[ny][nx] != 1 :
            visited[ny][nx] = 1 # 방문# ny, nx가 아닌 기존 위치를 넣어야 하므로 r, c를 넣어야 한다.
            maze_runner(ny, nx) # 재귀
    # return ans
T = int(input())
for test in range(1, T+1):
    N = int(input()) # 미로 크기 NxN
    # 2 출발 3 도착,
    #0 이 길이고 1이 벽이다.
    maze = [[int(i) for i in input()] for _ in range(N)] # 미로 구현
    visited = [[0] * N for _ in range(N)] #방문지도
    start_R, start_C = start() # 시작지점
    # end_r, end_c = end()
    # print(maze)

    ans = 0
    maze_runner(start_R, start_C) # 도착점 찾기
    print(F"#{test} {ans}")
    # print(visited)
## 10개 중 7개 맞음...
######################################################################

# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
#
# T = int(input())
# for test in range(1, T + 1):
#     N = int(input()) # 미로의 크키
#     maze = [list(map(int, input())) for _ in range(N)]

#     si, sj = start()
#     def dfs(si, sj):
#         visited = [[0] * N for _ in range(N)]
#         stack = []
#         stack.append([si, sj])
#         visited[si][sj] = 1
#         i, j = si, sj
#         while True:
#             # 출구
#             if maze[i][j] == 3:
#                 return 1

#             for d in range(4):
#                 ni = i + di[d]
#                 nj = j + dj[d]
#                 if in_range(ni, nj) and not visited[ni][nj] and maze[ni][nj] != 1:
#                     visited[ni][nj] = 1
#                     stack.append([i, j])
#                     i, j =ni, nj
#                     break
# #
#             else:
#                 if stack:
#                     i, j = stack.pop()
#                 else:
#                     break
#         return 0
#     print(f"#{test} {dfs(si, sj)}")





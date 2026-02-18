'''
블록 별 이동 가능 방향을 dict를 이용해 구현 하였다. 이를 통해 탐색가능한 곳을 이동하며 탐색하였다 
갈 수 있는 곳이 여러군데가 있자 이를 어떻게 해결해야 하는지 고민하였고 
동시에 진행하는 식으로 구현하고 싶었지만 불가능 했다. 
이후 스택을 도입하여 진행하였는데 시간이 문제였다. dfs는 이동가능 거리 측정 기반이었고
이 문제는 특정 시간동안 어디까지 갈 수 있는가 였기 때문이다. 
---- AI사용 ---
AI가 시간 변수까지 추가한다면 스택으로 할 수 있다고했다.
하지만 많이 어려워 보여 포기하였고 다시 스택 없이 진행하였다.
그 결과 두번째 반복문 부터 시작지점을 여러군데 지정하여 이를 기반으로 모두 탐색하고 
탐색한 곳을 다시 시작 지점에 추가하여 진행하였다.
AI가 원래는 이 문제가 bfs를 사용하는 문제라 하였지만 
쓸줄 모르니 일단 그냥 되는대로 풀어보았다.  
전체적인 틀은 직접 만들었고 AI를 통해 오류나는 부분이나 고쳐야 하는 점들을 수정하며 풀이하였다.  

어려웠던 점: 여러 군데를 동시에 방문한다 생각하고 시간대별 이동 가능한 모든 구역 찾기 구현, 
두 파이프가 엇갈려서 지나가지 못 할 경우 이를 못 지나가게 하기
'''

# 인덱스 범위 넘어갈시 x
# def in_range(y, x):
#     return 0<= y < N and 0<= x < M


# T = int(input())
# for test in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     under = [list(map(int, input().split())) for _ in range(N)]

#     # 동 남 서 북
#     dy = [0, 1, 0, -1]
#     dx = [1, 0, -1, 0]
#     way = {
#         # 동 남 서 북
#         1:[4, dy, dx],
#         # 남 북
#         2:[2, dy[1:4:2], dx[1:4:2]],
#         # 동 서
#         3:[2, dy[0:4:2], dx[0:4:2]],
#         # 동 북
#         4:[2, dy[0:4:3], dx[0:4:3]],
#         # 동 남
#         5:[2, dy[0:2], dx[0:2]],
#         # 남 서
#         6:[2, dy[1:3], dx[1:3]],
#         # 서 북
#         7:[2, dy[2:4], dx[2:4]],
#     }

#     #방문한 곳을 저장해둔다.
#     visited = [[0]*M for _ in range(N)] 
#     # 현재 위치에서 다음으로 갈 위치

#     # 들어갔을 때 입구의 위치
#     current = [[R, C]]
#     visited[R][C] = 1
#     # 시간만큼 이동하므로 반복문을 돌린다.
#     for i in range(L-1):
#         next_position = []
#         for y, x in current:
#             # 해당 위치에서 갈 수 있는 방향
#             dir = under[y][x]
#             # 갈 수 있는 방향의 숫자에 일치하는 dic의 첫 값으로 방향의 수가 정해져 있으므로
#             # 해당 수만큼 여러 방면을 탐색한다.
#             for j in range(way[dir][0]):
#                 # 해당 방면으로 이동한다.
#                 ny = y + way[dir][1][j]
#                 nx = x + way[dir][2][j]

#                 # 내가 가는 방향을 검색한다.
#                 dir_y, dir_x = way[dir][1][j], way[dir][2][j]
#                 for k in range(4):
#                     if dy[k] == dir_y and dx[k] == dir_x:
#                         d = k
#                         break # for k
                
#                 # 범위 밖 제거 and 해당 위치의 값이 0이면 갈 수 없다.
#                 # 추가로 방문한 곳은 가지 않는다.
#                 if in_range(ny, nx) and under[ny][nx] and not visited[ny][nx]:

#                     # 이동한 칸이 d 와 반대방향을 가리키고 있어야 한다.
#                     op = (d + 2) % 4    
#                     if (dy[op], dx[op]) in zip(way[under[ny][nx]][1], way[under[ny][nx]][2]):

#                         # 방문한 곳을 기록한다.
#                         visited[ny][nx] = 1
#                         # 다음 시간대에 존재할 수 있는 위치를 기록해둔다.
#                         next_position.append([ny, nx])
#                         # stack.append([ny, nx])
#                         # now_y, now_x = ny, nx
#         current = next_position


#     visit = 0
#     # print(visited)
#     for i in range(N):
#         visit += sum(visited[i])
#     print(F"#{test} {visit}")


###############################################
# bfs 로 풀어보기
def in_range(y, x):
    return 0<= y < N and 0<= x < M

from collections import deque
# 아래 위 동 서
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())
for test in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]


    q = deque()
    q.append([R, C])
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            ny = r + dy[d]
            nx = c + dx[d]
            if in_range(ny, nx) and not visited[ny][nx]:
                if under[ny][nx] != 0:
                    if under[r][c] == 1:
                        q.append([ny, nx])
                        visited[ny][nx] = visited[r][c] + 1
                    elif d == 1 and under[r][c] == 2 and under[ny][nx] in (1, 2, 5, 6):
                        q.append([ny, nx])
                        visited[ny][nx] = visited[r][c] + 1
                    elif d == 2 and under[r][c] == 3 and under[ny][nx] in (1, 3, 6, 7):
                        q.append([ny, nx])
                        visited[ny][nx] = visited[r][c] + 1

    print(visited)
                    

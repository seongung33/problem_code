"""
swea 2105
디저트 카페
 NxN 정사각형 디저트 카페 수 N**2
 원 안의 숫자는 해당 카페의 디저트 수
 조건 1. 카페들간의 이동은 대각선만 가능하다. 
 조건 2.사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
 조건 3. 같은 숫자의 디저트를 판매하는 곳은 갈 수 없다.
 조건 4. 두 곳 이상의 디저트 카페를 방문해야 한다. ( 사각형을 그리므로 네곳 이상 방문)
 조건 5. 갔던 곳은 다시 갈 수 없다.
 조건 6. 해당 사각형이 그리는 최댓값을 구하라.
"""
# T = int(input())
# for test in range(1, T + 1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

#     # 디저트를 못 먹을 경우
#     ans = -1
#     max_cnt = 0
#     # 방향이동 델타
#     # 남동, 남서, 북서, 북동(시계 방향)
#     dy = [1, 1, -1, -1]
#     dx = [1, -1, -1, 1]
#     #범위를 벗어날 경우 인덱스 에러 방지
#     def in_range(y, x, N):
#         return 0<= x < N and 0 <= y < N

#     # 완전 탐색
#     for i in range(N):
#         for j in range(N):
#             # 해당 위치에서 반복문
#             # for dir in range(4): # 첫 대각
#                 for a in range(1, N): # 이동 길이
#                     for b in range(1, N): # 이동 길이 2
                        
#                         ny = i
#                         nx = j
#                         s = 0
#                         cnt = 0
#                         visited = set()
#                         # visited.add(matrix[ny][nx])
#                         valid = True

#                         lenghts = [a, b, a, b] # 같은 길이만큼 이동해야 함
#                         # 방향전환과 이동하며 누적합 구하기
#                         for d in range(4):
#                             D = (d) % 4
                        
#                             for _ in range(1, lenghts[d]+1):
#                                 ny = ny +dy[D]
#                                 nx = nx +dx[D]
#                                 # 인덱스 벙뮈 밖이면 break
#                                 if in_range(ny, nx, N):
#                                     pass
#                                 else:
#                                     valid = False
#                                     break
#                                 # 방문한 카페일시  break
#                                 if matrix[ny][nx] in visited:
#                                     valid = False
#                                     break
#                                 # 모두 통과시 방문 기록을남긴다.
#                                 visited.add(matrix[ny][nx])
#                                 cnt += 1
#                             # 반복문이 2개이므로 break시 두개를 break 하여야 한다.
#                             if not valid:
#                                 break
#                         # break가 되지 않았고 원위치로 돌아왔으며 4개의 카페를 들렸을 경우
#                         if valid and ny ==i and nx == j and cnt >= 4:
#                             # 방문한 카페수가 가장 많은 경우
#                             if max_cnt < cnt:
#                                 max_cnt = cnt
#     if max_cnt > 3:
#         ans = max_cnt
 
#     print(f"#{test} {ans}")



####################################################################################
# dfs로 풀어보기

# 델타
# 오른 아래 왼 아래 왼 위 오 위
# dy = [1, 1, -1, -1]
# dx = [1, -1, -1, 1]

# def in_range(y, x):
#     return 0<= y < N and 0<= x < N

# # dfs
# def dfs(i, j, d):
#     global max_cnt
#     if d >= 4:
#         return
#     # if d == 3 and (ci, cj) == (i, j):
#     #    max_cnt = max(max_cnt, len(visited))
#     #    return
#     else:
#         # for k in range(4):
#         ny = i + dy[d]
#         nx = j + dx[d]
#         if in_range(ny, nx): 
#             if d == 3 and (ci, cj) == (ny, nx):
#                     max_cnt = max(max_cnt, len(visited))
#                     return
#             if mat[ny][nx] not in visited:
#                 visited.append(mat[ny][nx])
#                 dfs(ny, nx, d)
#                 visited.pop()
#         if d < 3:
#             ny = i + dy[d+1]
#             nx = j + dx[d+1]
#             if in_range(ny, nx):
#                 if d+1 == 3 and (ci, cj) == (ny, nx):
#                     max_cnt = max(max_cnt, len(visited))
#                     return
#                 if mat[ny][nx] not in visited:
#                     visited.append(mat[ny][nx])
#                     dfs(ny, nx, d+1)
#                     visited.pop()

# T = int(input())
# for test in range(1, T + 1):
#     N = int(input())
#     mat = [list(map(int, input().split())) for _ in range(N)]

#     d = 0
#     max_cnt = -1
#     cnt = 0
#     for y in range(N):
#         for x in range(N):
#             visited = []
#             ci, cj = y, x
#             visited.append(mat[ci][cj])
#             dfs(y, x, 0)
#     print(F"#{test} {max_cnt}")




#########################################################
dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

def in_range(y, x):
    return 0<= y < N and 0<= x < N

def dfs(i, j, d):
    global max_cnt
    if d >= 4:
        return
    else:
        ny = i +dy[d]
        nx = j + dx[d]
        if in_range(ny, nx):
            if d == 3 and (ci, cj) == (ny, nx):
                max_cnt = max(max_cnt, len(v))
                return
            else:
                if mat[ny][nx] not in v:
                    v.append(mat[ny][nx])
                    dfs(ny, nx, d)
                    v.pop()
        if d < 3:
            ny = i +dy[d+1]
            nx = j + dx[d+1]
            if in_range(ny, nx):
                if d+1 == 3 and (ci, cj) == (ny, nx):
                    max_cnt = max(max_cnt, len(v))
                    return
                if mat[ny][nx] not in v:
                    v.append(mat[ny][nx])
                    dfs(ny, nx, d+1)
                    v.pop()

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]


    max_cnt = -1
    for i in range(N):
        for j in range(N):
            ci, cj = i, j
            v = [mat[ci][cj]]
            dfs(i, j, 0)
    print(F"#{test} {max_cnt}")
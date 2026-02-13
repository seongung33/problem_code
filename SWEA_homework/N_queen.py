# 인덱스 범위 벗어나지 않기
def in_range(y, x):
    return 0 <= y < N and 0 <= x < N



# 재귀함수 구성
def queen(i, j, N):
    #글로벌 변수 선언
    global cnt
    # print(i, j, cnt)
    # 종료조건
    if j == N:
        cnt += 1
        return
    else:
        for d in range(N):
            # 갈 수 있는 조건
            if in_range(d, j) and not visited[d][j]:
                
            # 방문한 곳 기록 퀸은 가로세로 모든 대각을 막는다.
                #가로 막기
                for y in range(N):
                    #가로 오른쪽
                    if in_range(d, j+y):
                        visited[d][j+y] += 1
                    # 가로 왼쪽
                    if in_range(d, j-y):
                        visited[d][j-y] += 1
                    # #세로 아래
                    # if in_range(i+y+d, j):
                    #     visited[i+y+d][j] += 1
                    # #세로 위
                    # if in_range(i-y+d, j):
                    #     visited[i-y+d][j] += 1
                    #대각 오른 아래
                    if in_range(y+d, j+y):
                        visited[y+d][j+y] += 1
                     #대각 왼쪽 위
                    if in_range(d-y, j-y):
                        visited[d-y][j-y] += 1    
                    #반대 대각 왼쪽 아래
                    if in_range(y+d, j-y):    
                        visited[y+d][j-y] += 1
                    # 반대 대각 오른쪽 위
                    if in_range(d-y, j+y):    
                        visited[d-y][j+y] += 1
                
                queen(d, j+1, N)

                # 방문 취소
                # 방문한 곳 기록 퀸은 가로세로 모든 대각을 막는다.
                for y in range(N):
                    #가로 오른쪽
                    if in_range(d, j+y):
                        visited[d][j+y] -= 1
                    # 가로 왼쪽
                    if in_range(d, j-y):
                        visited[d][j-y] -= 1
                    # #세로 아래
                    # if in_range(i+y+d, j):
                    #     visited[i+y+d][j] -= 1
                    # #세로 위
                    # if in_range(i-y+d, j):
                    #     visited[i-y+d][j] -= 1
                    #대각 오른 아래
                    if in_range(y+d, j+y):
                        visited[y+d][j+y] -= 1
                     #대각 왼쪽 위
                    if in_range(d-y, j-y):
                        visited[d-y][j-y] -= 1    
                    #반대 대각 왼쪽 아래
                    if in_range(y+d, j-y):    
                        visited[y+d][j-y] -= 1
                    # 반대 대각 오른쪽 위
                    if in_range(d-y, j+y):    
                        visited[d-y][j+y] -= 1
                
                


    

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    cnt = 0
    visited = [[0]*N for _ in range(N)]

    queen(0, 0, N)
    print(f"#{test} {cnt}")
"""
문제내용 하나도 못 알아듣겠네
시작점은 사무실이고 관리구역은 시작점 제외 전부
모든 관리구역을 방문하고 사무실로 돌아와야 한다.
표에서 말하는 것은 i -> j로의 이동비용이다. 
즉 1 - 2 - 3 - 1은 사무실 출발 -> 관리구역 2 -> 관리구역 3 -> 시작점 1 이다.
e[1][2]: 사무실 -> 관리구역 2로 이동
y축은 출발점
x 축은 도착점이다. 
"""


# 재귀
def recur(i, s):
    global min_s

    # 모든 곳 방문 했으면 최솟값 계산
    if sum(visited) == N:
        min_s = min(min_s, s)
        return

    # 가지치기
    if s >=min_s:
        return
    
    # 처음을 제외한 위치 방문하는 재귀
    for j in range(1, N):
        if visited[j]:
            continue
        visited[j] = True
        recur(j, s+mat[i][j])
        visited[j] = False

    # 처음 제외 모두 방문했으면 처음 방문
    if sum(visited) == N-1:
        if not visited[0]:     
            visited[0] = True
            recur(0, s+mat[i][0])
            visited[0] = False
    
T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    #최솟값
    min_s = float("inf")

    visited = [False]*(N)

    # 사무실 출발
    recur(0, 0)
    print(F"#{test} {min_s}")



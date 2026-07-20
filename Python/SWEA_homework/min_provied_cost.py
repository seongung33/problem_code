T = int(input())

# cost는 비용, i는 행 내려가기(제품선택)
def dfs(cost, i):
    global min_cost
    # 모든 제품 선택함
    if i == N:
        min_cost = min(cost, min_cost)

    # 가지치기
    # 현재 비용이 최소비용보다 크면 탐색 X
    if cost >= min_cost:
        return

    # 재귀
    for d in range(N):
        if not visited[d]:
            # 방문은 같은 공장을 선택하지 않는 것
            visited[d] = True
            # 비용추가 + 행 내려가기(다음 제품 선택)
            dfs(cost + mat[i][d], i+1)
            visited[d] = False

for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')
    visited= [False]*N

    dfs(0, 0)

    print(F"#{test} {min_cost}")
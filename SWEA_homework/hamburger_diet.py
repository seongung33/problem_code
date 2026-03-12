T = int(input())
# 칼로리 합, 점수 합
def dfs(sumation, score, prev):
    global max_score
    # 칼로리를 초과하지 않으면 최댓값 비교
    if sumation <= L:
        max_score = max(score, max_score)
    # 종료조건 칼로리가 제한 칼로리에 도달했을 때
    if sumation >= L:
        return
    # 가지치기
    # 하나로 안됨...
    if ((sumation, score)) in sett:
        return

    sett.add((sumation, score))
    # 처음부터 탐색이니 조합처럼 처음 이후만을 본다면?
    for i in range(prev+1, N):
        if visited[i]:
            continue
        # 포함한 재료 제외 visited
        visited[i] = True
        dfs(sumation+ lst[i][1], score + lst[i][0], i)
        visited[i] = False


for test in range(1, T+1):
    N, L = map(int, input().split())
    lst = [[0, 0] for _ in range(N)]
    for i in range(N):
        num, cal = map(int, input().split())
        lst[i][0] = num
        lst[i][1] = cal
    sett = set()
    visited =[False]*N
    max_score = 0
    dfs(0, 0, -1)
    print(F"#{test} {max_score}")


######################################################
T = int(input())

# dp도 되지 않을까?
for test in range(1, T+1):
    N, L = map(int, input().split())
    lst = [[0, 0] for _ in range(N)]
    for i in range(N):
        num, cal = map(int, input().split())
        lst[i][0] = num
        lst[i][1] = cal

    dp = [0]*(L+1)

    for score, cal in lst:
        for i in range(L, cal-1, -1):
            if dp[i] < dp[i-cal]+score:
                dp[i] = dp[i-cal]+score
    print(F"#{test} {dp[L]}")

T = int(input())
def dfs(cnt, d, prob):
    global  max_prob
    if cnt == N:
        max_prob = max(max_prob, prob)
        # print(prob)
        return

    if prob <= max_prob:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, d+1, prob*(lst[d][i]/100))
            visited[i] = False

for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_prob = 0
    visited = [False] *N


    dfs(0,0,1)
    print(F"#{test} {100*max_prob:.6f}")



###########################################
T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
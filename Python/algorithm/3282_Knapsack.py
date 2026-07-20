# T = int(input())
# for test in range(1, T+1):
#     N, K = map(int, input().split())
#     dp = [0]*(K+1)
#     for i in range(N):
#         v, c = map(int, input().split())
#         for j in range(K, v-1, -1):
#             dp[j] = max(dp[j], dp[j-v] + c)

#     print(F"#{test} {dp[K]}")



def dfs(max_V, value, idx):
    global answer

    if max_V > K:
        return 
    if (max_V, value, idx) in zz:
        return
    answer = max(answer, value)
    # print(answer)
    for i in range(idx+1, N):
        v, c = info[i]
        zz.add((max_V, value, idx))
        dfs(max_V + v, value + c, i)

T = int(input())
for test in range(1, T+1):
    zz = set()
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    V = 0

    dfs(0, 0, -1)

    print(F"#{test} {answer}")
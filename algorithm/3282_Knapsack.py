T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    dp = [0]*(K+1)
    for i in range(N):
        v, c = map(int, input().split())
        for j in range(K, v-1, -1):
            dp[j] = max(dp[j], dp[j-v] + c)

    print(F"#{test} {dp[K]}")

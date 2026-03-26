T = int(input())
for test in range(1, T+1):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))

    dp = [0]*(16)

    for i in range(12, 0, -1):
        dp[i] = min(dp[i+3]+ three,
                    dp[i+1]+day*plan[i-1],
                    dp[i+1]+month)

    ans = min(dp[1], year)

    print(F"#{test} {ans}")
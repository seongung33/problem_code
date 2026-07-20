"""
오른쪽 무게의 합 < 왼쪽 무게의 합

오른쪽에 올릴 추만 선택
전체 무게 합 - 오른쪽 추의 합 = 왼쪽 무게 합
왼쪽이 더 무거워야 하므로 오른쪽 추의 합이 전체 합의 절반을 넘어가면 안된다.
오른쪽 추의 합 < 전체 합 / 2
추의 올리는 순서: N번
왼쪽부터 올려야 한다.

오른쪽 추만 고르므로 무조건 왼쪽 추는 있어야 한다.
최대 선택 가능 개수의 추는 N-1개
"""
T = int(input())


def dfs(cnt, left_sum, right_sum):
    global ans

    if left_sum < right_sum:
        return
    remain = total_sum - left_sum - right_sum
    if left_sum >= right_sum + remain:
        ans += factorial[N - cnt] * (2 ** (N - cnt))
        return

    if cnt == N:
        ans += 1
        # print(w)
        return


    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, left_sum+weight[i], right_sum)
            if left_sum >= right_sum + weight[i]:
                dfs(cnt+1, left_sum, right_sum + weight[i])
            visited[i] = False
for test in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))
    visited = [False]*(N)
    total_sum = sum(weight)
    ans = 0
    factorial = [1] * (N + 1)
    for i in range(1, N + 1):
        factorial[i] = factorial[i - 1] * i
    dfs(0, 0, 0)

    print(F"#{test} {ans}")

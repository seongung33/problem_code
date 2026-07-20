"""
완탐
벌은 연속된 꿀 두개를 선택 
각 꿀은 C를 넘으면 안된다.
이떄 꿀들의 제곱의 합이 최대인 것은?

완탐 
크기 100
100* 4방향 * 10 
4000 * 50
200,000
"""
T = int(input())


def dfs(cnt, lst, y, x):
    global ans
    if cnt == M:
        money = sum(lst)
        print(money)
        ans = max(ans, money)

    # print(cnt, y, x)
    for i in range(y, N):
        for j in range(x+1, N-1):
            num1 = mat[i][j] 
            num2 = mat[i][j+1]
            if num1 + num2 <= C:
                mon = revenue([num1, num2])
                dfs(cnt+1, lst + [mon], i, j+1)
            else:
                if num1 >= num2:
                    dfs(cnt+1, lst + [num1**2], i, j)
                else:
                    dfs(cnt+1, lst + [num2**2], i, j+1)



dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def in_range(y, x):
    return 0<= y < N and 0<= x < N


def revenue(lst):
    money = 0
    for i in lst:
        money += i**2
    return money

for test in range(1, T+1):
    N, M, C = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]


    ans = 0
    dfs(0, [], 0, -1)


    # max_revenue = [0]*M
    # visited = [[0]*N for _ in range(N)]
    # for q in range(M):
    #     ans = dp()
    #     # print(ans)
    #     max_revenue[q] = ans
    # ans = sum(max_revenue)
    # print(max_revenue)
    print(F"#{test} {ans}")
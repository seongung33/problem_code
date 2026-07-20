T = int(input())
def dfs(y, x, a):
    global ans
    if x == N:
        ans += 1
        # print(ans)
        return 
    for i in range(N):
        if visited[i]:
            continue

        valid = diagonal(i, x, a)
        if not valid:
            continue
        visited[i] = True
        # lst.append((i, x))
        dfs(i, x+1, a +[(i, x)])
        # lst.pop()
        visited[i] = False


def diagonal(y, x, lst):
    if not lst:
        return True
    for ay, ax in lst:
        if abs(ay-y) == abs(ax-x):
            return False
    return True


for test in range(1, T+1):
    N = int(input())

    visited = [False]*N
    lst = []
    ans = 0
    dfs(0, 0, [])

    print(F"#{test} {ans}")

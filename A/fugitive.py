T = int(input())
for test in range(1, T + 1):
    N, M, R, C, L = map(int, input())
    underground =[list(map(int, input().split()))for _ in range(N)]
    for i in range(L):
        visited = set()
        visited.add(underground[R][C])
        
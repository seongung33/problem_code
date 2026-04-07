# 플로이드 워샬
INF = float('inf')

T = int(input())
for test in range(1, T+1):
    N, M, X = map(int, input().split())

    visited = [[INF]*(N+1) for _ in range(N+1)]
    adj_mat = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        x, y, c = map(int, input().split())
        
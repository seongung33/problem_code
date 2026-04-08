T = int(input())

def dfs(v, path):
    global max_len

    if max_len < len(path):
        max_len = len(path)

    for i in adj_mat[v]:
        if i in path:
            continue
        dfs(i, path + [i])
    



for test in range(1, T+1):
    # 정점, 간선
    # N은 1부터 시작
    N, M = map(int, input().split())
    # 인접 행렬 생성
    adj_mat = [[] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int ,input().split())
        adj_mat[x].append(y)
        adj_mat[y].append(x)
    max_len = 0
    for i in range(1, N+1):
        dfs(i, [i])
    print(F"#{test} {max_len}")
    
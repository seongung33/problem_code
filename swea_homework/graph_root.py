# dfs 함수 생성
def dfs(s, G):# 시작, 도착
    stack = []
    stack.append(s)
    visited = [0] * (V+1)
    v = s
    ans = 0
    if v == G:
        ans = 1
        return ans
    while True:
        for w in range(V+1):
            if adj_m[v][w] and not visited[w]:
                # w 방문
                visited[w] = 1
                stack.append(w)
                # print(stack)
                v= w
                if v == G:
                    ans = 1
                    return ans
                break # for w
        else:
            if stack:
                v = stack.pop()
            else:
                break # while true
    return ans






T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split()) # 노드개수, 간선 수




    # node = [list(map(int, input().split())) for _ in range(E)]
    # S, G = map(int, input().split()) # 시작지점, 도착 지점
    # adj_m = [[0]*(V+1) for _ in range(V+1)] # 인덱스 번호가 노드, 해당 위치의 값이 이동 가능한 다른 노드
    # # 해당 인덱스에 갈 수 있는 노드 값 추가
    # for i, j in node:
    #     adj_m[i][j] = 1
    # print(adj_m)
    ########################################### 위 아래 택 1
    adj_m = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj_m[s][e] = 1
    # print(adj_m)
    S, G = map(int, input().split())


    result = dfs(S, G)
    print(f"#{test} {result}")

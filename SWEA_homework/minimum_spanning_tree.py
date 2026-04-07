# 프림

import heapq
T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    #인접 리스트 생성
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append((w, n2))
        adj_list[n2].append((w, n1))

    visited = [0] * (V + 1)

    pq = []
    # for w, next_node in adj_list[0]:
    #     heapq.heappush(pq, (w, next_node))
    #
    # visited[0] = 1
    ans = 0
    heapq.heappush(pq, (0, 0))
    while pq:

        w, next_node = heapq.heappop(pq)

        if visited[next_node]: # 이미 간 노드면 스킵
            continue
        ans += w # 누적 가중치
        visited[next_node] = 1 # 방문 표시
        # 현재 노드에서 갈 수 있는 다음 노드 추가
        for w,next_node in adj_list[next_node]:
            heapq.heappush(pq, (w, next_node))

    print(F"#{test} {ans}")



########################################################################

# 크루스칼
T = int(input())

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    # 사이클이 존재한다면
    if root_y == root_x:
        return False

    if rank[root_x] > rank[root_y]:
        p[root_y] = root_x
    else:
        p[root_x] = root_y
    if rank[root_x] == rank[root_y]:
        rank[root_y] += 1

    return True




for test in range(1, T+1):
    V, E = map(int, input().split())

    ans = 0
    lst = []
    p = [i for i in range(V+1)]
    rank = [1]*(V+1)

    for i in range(E):
        n1, n2, w = map(int, input().split())
        lst.append((w, n1, n2))
    # 한 줄에 등록 후 정렬
    lst.sort()
    # 사이클이 발생하지 않으면 더함
    for w, n1, n2 in lst:
        valid = union(n1, n2)
        if valid:
            ans += w

    print(F"#{test} {ans}")


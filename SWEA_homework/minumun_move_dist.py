import heapq
T = int(input())
for test in range(1, T+1):
    N, E = map(int, input().split())
    adj_list = [[]for _ in range(N+1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        # 가중치, 이동가능 노드
        adj_list[s].append((w, e))

    pq = []
    weights = [10*1000]*(N+1)
    weights[0] = 0
    for w, e in adj_list[0]:
        heapq.heappush(pq, (w, e))

    while pq:
        weight, end = heapq.heappop(pq)

        if weights[end] < weight:
            continue
        weights[end] = weight

        for weight, next_node in adj_list[end]:
            new_weight = weight + weights[end]
            if new_weight >= weights[next_node]:
                continue
            weights[next_node] = new_weight
            heapq.heappush(pq, (new_weight, next_node))

    print(F"#{test} {weights[N]}")
import heapq
N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]
for i in range(M):
    u, v, w = map(int, input().split())
    lst[u].append([v,w])   
start, goal = map(int, input().split())

dist = [float('inf')]*(N+1)
def dijkstra(start):
    q = []
    # 출발지에서 각 도시별 이동비용
    # q 에 비용, 도착도시를 넣는다.
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now_city = heapq.heappop(q)

        if d > dist[now_city]:
            continue

        for next_city, move_cost in lst[now_city]:
            cost = d + move_cost
            if dist[next_city] > cost:
                dist[next_city] = cost
                heapq.heappush(q, (cost, next_city))

dijkstra(start)
print(dist[goal])
# V, E = map(int, input().split())
# start = int(input())
# mat = [[0]*(V) for _ in range(V)]
# for i in range(E):
#     u, v, w = map(int, input().split())
#     mat[u-1][v-1] = w

# for i in range(V):
#     for j in range(V):
#         if i == j:
#             continue
#         elif not mat[i][j]:
#             mat[i][j] = float('inf') 

# dist = [float('inf')]*V
# q= [(0, start-1)]
# visited = [False]*V
# def get_smallest():
#     idx = 0
#     min_val = float('inf')
#     for i in range(V):
#         if dist[i] < min_val and not visited[i]:
#             min_val = dist[i]
#             idx = i
#     return idx

# def dijkstra(start):
#     visited[start] = True
#     for i in range(V):
#         dist[i] = mat[start][i]
#     for _ in range(V-1):
#         now = get_smallest()
#         visited[now] = True
        
#         for node in range(V):
#             cost = dist[now] + mat[now][node]
#             if cost < dist[node]:
#                 dist[node] = cost
# dijkstra(start-1)
# for i in range(V):
#     if dist[i] == float('inf'):
#         print("INF")
#     else:
#         print(dist[i])


import heapq
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
dist = [float('inf')]*(V+1)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue
        for next_node, val in graph[now]:
            cost = d + val
            if dist[next_node] > cost:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(start)

for i in range(1,V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])


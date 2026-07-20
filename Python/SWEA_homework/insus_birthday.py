# # 플로이드 워샬
# INF = float('inf')

# T = int(input())
# for test in range(1, T+1):
#     N, M, X = map(int, input().split())

#     # 인접 행렬 생성
#     adj_mat = [[INF]*(N+1) for _ in range(N+1)]

#     for i in range(M):
#         x, y, c = map(int, input().split())
#         adj_mat[x][y] = c
#     for i in range(N+1):
#         adj_mat[i][i] = 0
#     # 플로이드 워샬 코드
#     for k in range(1, N+1):
#         for i in range(1, N+1):
#             for j in range(1, N+1):
#                 # print(k)
#                 if adj_mat[i][j] > adj_mat[i][k] + adj_mat[k][j]:
#                     adj_mat[i][j] = adj_mat[i][k] + adj_mat[k][j]
#     ans = [0]*(N+1)
#     for i in range(N+1):
#         ans[i] += adj_mat[X][i] + adj_mat[i][X]    
#     print(F"#{test} {max(ans[1:])}")
#     # print(ans)
"""
플로이드로 풀릴줄 알았는데 시간 초과 뜸
다익스트라로 해야 할듯
"""

######################################################

import heapq
T = int(input())
INF = float('inf')
for test in range(1, T+1):
    # 집, 간선 수, 인수 집
    N, M, X = map(int, input().split())
    dist = [INF]*(N+1)
    pq = []
    # 정방향
    adj_list = [[] for _ in range(N+1)]
    # 역방향 그래프
    adj_rev = [[] for _ in range(N+1)]

    for i in range(M):
        x, y, c = map(int ,input().split())
        adj_list[x].append((y, c))
        adj_rev[y].append((x, c))

    # 정방향 X -> 각 마을들의 최소 거리
    heapq.heappush(pq, (X, 0))
    while pq:
        home, time = heapq.heappop(pq)
        if time > dist[home]:
            continue
        dist[home] = time

        for next_home, time in adj_list[home]:
            next_time = time + dist[home]
            if next_time > dist[next_home]:
                continue
            dist[next_home] = next_time
            heapq.heappush(pq, (next_home, next_time))

    # 역방향
    heapq.heappush(pq, (X, 0))
    dist_rev = [INF]*(N+1)
    while pq:
        home, time = heapq.heappop(pq)
        if time > dist_rev[home]:
            continue
        dist_rev[home] = time

        for next_home, time in adj_rev[home]:
            next_time = time + dist_rev[home]
            if next_time > dist_rev[next_home]:
                continue
            dist_rev[next_home] = next_time
            heapq.heappush(pq, (next_home, next_time))
    ans = [0]*(N+1)
    for i in range(N+1):
        ans[i] = dist_rev[i] + dist[i]
    print(F"#{test} {max(ans[1:])}")

"""
논리: 집 -> X -> 집 의 값을 구해야 함 
여기서 X를 제외한 모든 집들에 대해 구하고 이때의 최댓값을 구해야함
X -> 집: 다익스트라 한 번이면 정답이 나옴. 문제 X
집 -> X: 각 집들에 대해 모두 다익스트라를 해야함. 시간이 너무 오래 걸림
그럼 어떻게 해야할까? 
단방향인 문제에서 방향을 반대로 하면 된다. 
그럼 X에서 다익스트라를 계산 시 나타나는 값은 집 -> X와 동일하다. 

1 -> 3 -> X -> 7 -> 3 -> 1 일 경우 X -> 7 -> 3 -> 1 는 패스
1 -> 3 -> X: 여기서 비용을 1-> 3: 5, 3-> X: 7 이라 두면
방향을 뒤집고 역방향으로 진행시 1번 집에는 X -> 3 -> 1로 진행할 수 있다. 
비용은 동일하게 X -> 3: 7, 3-> 1: 3으로 같은 비용이 나오게 된다. 

즉 방향을 뒤집음으로서 X에서 다익스트라 진행시 나타나는 비용은 
각 집에서 X로 도착할 때의 비용과 동일하다. 

단방향 그래프에서 방향을 뒤집었기 때문에 정방향에서 집 갈때와는 다른 값이 나올 수 밖에 없다.
"""
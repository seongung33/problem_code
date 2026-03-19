"""
MST: 최소 스패닝 트리란? 
주어진 그래프의 모든 정점들을 연결하는  그래프 중 그 합이 최소인 트리

"""

"""
크루스칼 알고리즘이란?
목표: MST, 최소 스패닝 트리 만들기 
간선의 거리(비용)가 짧은(싼) 간선 부터 연결한다. 
사이클을 만들면 안된다 !! 
모든 간선들을 오름차순으로 정렬한다. 
"""

## 크루스칼 알고리즘

V, E = map(int, input().split())
adj_lst = [[] for _ in range(V+1)]
for i in range(E):
    A, B, C = map(int, input().split())
    adj_lst[A].append(C)
    adj_lst[B].append(C)

node_val = [float('inf')]*(V+1)




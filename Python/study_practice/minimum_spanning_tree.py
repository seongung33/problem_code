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

큰 노드를 인덱스로, 작은 노드를 값으로 사용한다.
"""

## 크루스칼 알고리즘

V, E = map(int, input().split())
adj_lst = []
for i in range(E):
    A, B, C = map(int, input().split())
    adj_lst.append((C, A, B))

# 노드 연결
node_line = [i for i in range(V+1)] 

# 노드 가치
node_val = [0]*(V+1)
adj_lst.sort()
for i in range(E):
    if adj_lst[i][1] > adj_lst[i][2]:
        idx = adj_lst[i][1]
        end = adj_lst[i][2]
    else:
        idx = adj_lst[i][2]
        end = adj_lst[i][1]
    if node_line[idx] == i:
        node_line[idx] = end
        node_val[idx] = adj_lst[i]
ans = 0
for i in node_val:
    if i == 1:
        ans = -1
        break
    ans += i
print(ans)

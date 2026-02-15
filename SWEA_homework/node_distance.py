T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    way = [[] for _ in range(V+1)]
    for i in range(E):
        node1, node2 = map(int, input().split())
        way[node1].append(node2)
        way[node2].append(node1)
    # 출발, 도착
    S, G = map(int, input().split())
    #방문 표시
    visited = [0]*(V+1)
    # 큐
    que = [0]*10
    # 시작 끝
    front = rear = 0
    # 정답 설정
    ans = 0
    # 첫 노드 진입
    rear = (rear + 1) % 10
    que[rear] = S
    visited[S] = 1
    while front != rear:
        front = (front + 1) % 10
        val = que[front]
        for i in way[val]:
            if not visited[i]:
                rear = (rear + 1) % 10
                que[rear] = i
                visited[i] = visited[val] + 1
        if val == G:
            ans = visited[G]
    print(f"#{test} {ans}")
                

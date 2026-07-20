from collections import deque

T = int(input())
for test in range(1, T +1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    adj_list = []
    for i in range(N):
        if mat[i]:
            for j in range(len(mat[i])):

                mat[i][j] -= 1
        adj_list.append(mat[i][1:])


    # print(adj_list)
    visited = [0]*(N)
    q = deque()
    for i in range(N):
        if not adj_list[i]:
            q.append(i)
            visited[i] = 1
    # print(visited)
    while q:
        fr = q.popleft()
        for j in range(N):
            # 방문하지 않은 j
            if not visited[j]:
                # j를 가리키는 것에 fr이 있는가.
                if fr in adj_list[j]:
                    # 있다면 j를 가리키는 곳들을 방문 하였는가?
                    for k in adj_list[j]:
                        if visited[k] == 0:
                            break # for k
                    else:
                        # print('wow')
                        max_visit = 0
                        q.append(j)
                        for i in adj_list[j]:
                            max_visit = max(max_visit, visited[i])
                        # 나 j를 가리키는 곳들의 최댓값
                        visited[j] = max_visit + 1
    # print(visited)
    min_cnt = 0
    valid = True
    for i in range(0, N):
        min_cnt = max(min_cnt, visited[i])
        if visited[i] == 0:
            print(F"#{test} -1")
            valid = False
            break
    if not valid:
        continue
    print(f"#{test} {min_cnt}")


'''
1
4
1 3
2 1 3
1 4
0
'''
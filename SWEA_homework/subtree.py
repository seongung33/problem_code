from collections import deque

T = int(input())
for test in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    # 부모를 인덱스로 한 자식 노드 표기
    c1= [0]*(E+1+1)
    c2 = [0]*(E+1+1)
    # 주어진 값으로 자식 노드에 일치하는 노드 입력
    for i in range(E):
        if c1[tree[i*2]] == 0:
            c1[tree[i*2]] = tree[i*2+1]
        else:
            c2[tree[i * 2]] = tree[i * 2 + 1]

    # print(c1)
    # print(c2)

    cnt = 1
    q = deque()
    # 시작값 즉 서브트리의 root 값 입력
    q.append(N)
    # bfs 덱 사용
    # 아래로만 내려가니 방문 필요 없음
    while q:
        i = q.popleft()
        if c1[i] != 0:
            q.append(c1[i])
            cnt += 1
        if c2[i] != 0:
            q.append(c2[i])
            cnt += 1
    print(F"#{test} {cnt}")

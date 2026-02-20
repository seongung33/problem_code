T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 삽입 함수
    def enq(t):
        global last
        # t 삽입
        last += 1
        tree[last] = t
        c= last
        p = c //2
        # 조상 노드랑 비교하며 조상 노드가 더 크면 값 변경
        # 0번째를 0으로 하여 루트 노드 도착시 while문 정지
        # 1번 인덱스 부터 트리 사용
        # while p 로 작성하여도 됨, p 값이 0이 된다면 0번 인덱스 즉 트리의 밖이기 때문
        while tree[p] != 0 and tree[c] < tree[p]:
            tree[c], tree[p] = tree[p], tree[c]
            # 변경된 자리에서 다시 조상노드랑 비교
            c = p
            p = c // 2
    last = 0
    tree = [0]*(N+1)
    for i in lst:
        enq(i)
    # 마지막 노드의 조상 노드의 합 출력
    ans = 0
    while N//2:
        N //= 2
        ans += tree[N]
    print(F"#{test} {ans}")

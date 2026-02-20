T = int(input())
for test in range(1, T+1):
    N, M, L = map(int, input().split())# 노드의 개수,  리프노드 수, 노드 번호
    leaf = [map(int, input().split()) for _ in range(M)] #노드번호 노드 값
    tree = [0]*(N+1) # 트리 생성
    # 리프 노드 트리에 저장
    for num, value in leaf:
        tree[num] = value
    # print(tree)
    # 후위 순회
    def preorder(T):
        # 트리에 값이 있다면, 해당 값 반환
        # 해당 값을 넘어가면 인덱스 에러가 뜨므로 반환한다.
        # 아래 노드가 없는 상태.
        # 자식 노드가 하나일 경우에만 해당.
        # 또한 값을 반환 해줘야 하므로 0을 반환해준다.
        if T > N:
            return 0
        if tree[T]:
            return tree[T]
        # 값이 없다면 값이 있는 리프 노드 까지 진입 후 값 들고 오기
        elif tree[T] == 0:
            l = preorder(T * 2)
            r = preorder(T * 2 + 1)
            # 값을 현재 노드에 저장한다.
            tree[T] = l + r
            # print(tree)
            # 다음 노드에 반환값을 줘야한다.
            return tree[T]
## return을 쓰지 않으면 None 반환되어 l, r에 None 나오게 되어 값이 없는 상태가 된다.
    preorder(1)
    # print(tree)
    print(f"#{test} {tree[L]}")

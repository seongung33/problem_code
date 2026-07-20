# 후위 순회 해야 계산 가능

for test in range(1, 11):
    N = int(input())  # 정점의 개수
    # 정점의 정보
    lst = [list(input().split()) for _ in range(N)]
    # print(lst)
    # 부모 노드를 인덱스로 자식 노드 번호 저장
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)
    # 동일 위치에 값 저장
    tree = [0] * (N + 1)
    # 아래 for 문에서 위 세개에 값 추가 시행
    for i in range(N):
        node_num = int(lst[i][0])
        node_value = lst[i][1]
        # 연산자는 자식 노드가 있다.
        if lst[i][1] in "-+/*":
            cleft[node_num] = int(lst[i][2])
            cright[node_num] = int(lst[i][3])
        # 트리에 값 추가
        tree[node_num] = lst[i][1]

    # print(cleft)
    # print(cright)
    # print(tree)
    # 후위 순회
    def postorder(i):
        if i:
            l = postorder(cleft[i])
            r = postorder(cright[i])
            # 연산자 만나면 자식 노드로 값 계산
            if tree[i] in "-+*/":
                l = int(l)
                r = int(r)
                if tree[i] == "-":
                    res = l - r
                elif tree[i] == "+":
                    res = l + r
                elif tree[i] == "*":
                    res = l * r
                elif tree[i] == "/":
                    res = l / r
                # 연산자에서의 계산 결과를 현재 위치의 트리에 저장한다.
                tree[i] = res
                # return tree[i]
            return tree[i]
        return 0

    ans = postorder(1)
    # print(cleft)
    # print(cright)
    # print(tree)
    print(f"#{test} {ans:.0f}")

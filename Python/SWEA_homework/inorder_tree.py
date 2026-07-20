# 중위 순회 재귀
def inorder(t):
    #종료 조건
    if t > N:
        return
    # 왼쪽  우선 순회
    inorder(t*2)
    # 중앙 출력(할 일)
    print(tree[t], end = '')
    # 오른쪽 순회
    inorder(t*2+1)


for test in range(1, 11):
    N = int(input())
    node = [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)
    # 트리 구조를 리스트에 저장하기.
    for i in node:
        tree[int(i[0])] = i[1]
        # print(tree)
    print(F"#{test}", end=' ')
    inorder(1)
    print()
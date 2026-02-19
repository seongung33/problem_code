# 재귀
def tree(n):
    global c
    # 종료조건
    if n > N:
        return
    # 왼쪽
    tree(n*2)
    #중앙 and 문제 조건 수행
    tree_arr[n] = c
    c += 1
    # 오른쪽
    tree(n*2+1)



T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(range(1, N+1))
    tree_arr = [0]*(N+1)
    c = 1
    tree(1)
    # print(tree_arr)
    # 문제 요구 값 저장
    # 루트노드
    root = tree_arr[1]
    # 절반값
    ans = tree_arr[N//2]

    print(F"#{test} {root} {ans}")
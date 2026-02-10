# dfs 함수 구현
def dfs(A, B):
    #불가능할 경우
    ans = 0
    #스택
    stack = []
    # 현재 좌표
    v = A
    # 방문
    visited = [0]*100
    # 현재 좌표 방문
    stack.append(v)
    visited[v] = 1

    # 목적지 B까지 진행하는 반복문
    while True:

        #목적지 도달 시
        if v ==B:
            ans = 1
            return ans
        # 다음 경로 탐색

        for w in range(100):

            # v 에서 w로 갈 수 있고 방문하지 않은 곳이면
            if adj_m[v][w] and not visited[w]:
                # 방문한다.
                visited[w] = 1
                #이동한다.
                v = w
                #스택에 추가한다.
                stack.append(v)
                # print(v)
                # 다음 길을 탐색하여 다시 while을 돈다.
                break # for w
            # 모든 곳에 가지 못한다면
        else:
            # 되돌아갈 곳이 없다면
            if not stack:
                # 갈 수 있는 모든 곳을 방문한 것이다.
                # 반복문 종료
                return ans # while true
            # 되돌아갈 곳이 있다면
            else:
                # 기존에 왔던 곳으로 돌아간다.
                v = stack.pop()
                


for test in range(10):
    # A: 0, B: 99
    # 
    test, n = map(int, input().split())
    adj_m = [[0]*100 for _ in range(100)]
    ij =list(map(int, input().split()))
    # 방문 가능한 노드 입력
    for i in range(0, n*2, 2):
        adj_m[ij[i]][ij[i+1]] = 1
        # print(ij)
    # print(adj_m)

    ans = dfs(0, 99)
    print(f"#{test} {ans}")

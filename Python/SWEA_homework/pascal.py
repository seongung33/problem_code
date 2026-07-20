# 재귀함수로 만든다.
def pascal(N):
    # 0 부터 N이 되면 멈추기 때문에 재귀마다 i의 값을 +1 해준다.
    global i
    i += 1
    # print(i)
    # 재귀함수의 정지 조건이다.
    if i == N:
        return
    # i>=2 부터 위 인덱스의 합을 계산하기 때문에 아래오 ㅏ같은 조건이 필요하다.
    elif i >= 2:
        for j in range(1, i):
            # j 번째 인덱스는 바로 위의 j-1, j번째 인덱스의 합이다.
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        # 해당 합들을 계속 계산해야 하기 때문에 재귀로 구성한다.
        return pascal(N)
    return pascal(N)
T = int(input())
for test in range(1, T+1):
    N= int(input())
    # 파스칼의 삼각형을 만든다.
    lst = [[1]*i for i in range(1,N+1)]
    i = 0
    # print(lst)
    # 함수를 실행하여 lst에 값을 넣는다.
    pascal(N)
    print(f"#{test}")
    # 출력 결과대로 나오게 하기 위해 반복문과 *를 이용하여 리스트를 해체하여 출력한다.
    for i in range(N):
        print(*lst[i])

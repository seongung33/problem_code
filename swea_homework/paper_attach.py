#재귀
def attach(N):
    # print(N)
    # if N >3 and memo[N] == 0:
    #     # 사각형 배치시 마지막에 두는걸 생각해보자
    #     # 세로 하나 2x1 로 하나 둔다고 생각하면 나머지는 (N-1)을 계산하는것과 일치한다.
    #     # 2x2를 채운다고 생각해보자 2x2와 1x2 를 두개 포개어 둘 수도 있다. 다만 2x1을 두개 두는 것은 위에서 나오는 경우의 수이다.
    #     # 그러므로  2x2와 1x2 이므로 나머지 칸수는(N-2) 가 되어 여기에 2를 곱하면 된다.
    #     return attach(N-1) + attach(N-2)*2
    # else:
    #     return memo[N]

    if N >3 and memo[N] == 0:
        # 사각형 배치시 마지막에 두는걸 생각해보자
        # 세로 하나 2x1 로 하나 둔다고 생각하면 나머지는 (N-1)을 계산하는것과 일치한다.
        # 2x2를 채운다고 생각해보자 2x2와 1x2 를 두개 포개어 둘 수도 있다. 다만 2x1을 두개 두는 것은 위에서 나오는 경우의 수이다.
        # 그러므로  2x2와 1x2 이므로 나머지 칸수는(N-2) 가 되어 여기에 2를 곱하면 된다.
        memo[N] = attach(N-1) + attach(N-2)*2
    return memo[N]



T = int(input())
for test in range(1, T+1):
    N = int(input())
    N //= 10
    memo = [0] * (N+1)
    memo[1] = 1
    memo[2] = 3
    memo[3] = 5
    ans = attach(N)
    print(f"#{test} {ans}")
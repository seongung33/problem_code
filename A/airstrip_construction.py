def in_range(y, x):
    return 0<= y < N and 0<= x < N


T = int(input())
for test in range(1, T+1):
    N, X = map(int, input().split())
    airstrip = [list(map(int, input())) for _ in range(N)]

    cnt = 0
    # 가로 검사
    for i in range(1, N):
        if airstrip[i] == airstrip[i-1]:
            
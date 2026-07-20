T = int(input())
for test in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    max_cnt = 1
    cnt = 1
    for i in range(1, N):
        if C[i] > C[i-1]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")

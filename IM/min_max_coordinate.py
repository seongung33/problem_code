T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    min_num = float('inf')
    max_num = float('-inf')
    for i in range(N):
        if max_num <= lst[i]:
            max_num = lst[i]
            max_idx = i
        if min_num > lst[i]:
            min_num = lst[i]
            min_idx = i
    print(F"#{test} {abs(max_idx- min_idx)}")
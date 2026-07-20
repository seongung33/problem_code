T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]


    # 왜 5천 해야 통과지..?
    bus_num = [0]*5000
    
    for a, b in lst:
        for i in range(a-1, b):
            bus_num[i] += 1

    # print(bus_num)
    # for i in range(N):
    #     num = B[i]
    #     for j in range(A[i]-1, B[i]):
    #         bus_num[j] += 1
    # print(bus_num)
        
    print(F"#{test}", end=' ')
    for i in C:
        print(bus_num[i-1], end= ' ')
    print()
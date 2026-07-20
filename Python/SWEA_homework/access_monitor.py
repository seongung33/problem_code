

T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    xor = lst[0]
    for i in range(1,N):
        xor^= lst[i]

    print(F"#{test} {xor}")




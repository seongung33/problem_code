T = int(input())
for test in range(1, T+1):
    N = int(input())
    binary = bin(N)[2:]
    cnt = 0
    for i in binary:
        if i == "1":
            cnt += 1
    print(F"#{test} {cnt}")
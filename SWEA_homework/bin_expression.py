T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    # ans = "OFF"
    # if M & (1 <<N)-1 == (1<<N)-1:
    #     ans = "ON"
    # print(bin(M & (1 <<N)-1))
    # print(F"#{test} {ans}")


    print(F"#{test} {'ON' if M & (1 <<N)-1 == (1<<N)-1 else 'OFF'}")
    # "ON" if M & (1 << N-1)
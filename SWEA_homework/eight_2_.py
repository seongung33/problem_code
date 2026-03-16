T = int(input())
for test in range(1, T+1):
    new_lst = []
    N, lst =  input().split()
    print(lst)
    for i in range(int(N)):
        new_lst.append(int(lst[i], 16))

    ans = ""
    for i in new_lst:
        ans += str(bin(i))[2:].zfill(4)
    print(F"#{test} {ans}")
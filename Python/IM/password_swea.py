T = int(input())
for test in range(1, T + 1):
    N = int(input())
    lst_N = input()
    M = int(input())
    lst_M = input()
    j = 0
    ans = 0
    for i in range(N):
        if lst_N[i] == lst_M[j]:
            j += 1
        if j == M:
            ans = 1
            break
    print(f"#{test} {ans}")

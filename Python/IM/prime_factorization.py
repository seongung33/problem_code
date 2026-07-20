T = int(input())
for test in range(1, T+ 1):
    N = int(input())
    cnt = 0
    lst = [2, 3, 5, 7, 11]
    print(F"#{test}", end = ' ')
    for i in lst:
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
        print(cnt, end = ' ')
    print()

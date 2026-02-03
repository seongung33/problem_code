#2720 세탁소 사장 동혁 BAEKJOON
T = int(input())
q = 25
d = 10
n = 5
p = 1
lst = [q,d,n,p]

for test in range(T):
    change = [0] * 4
    C = int(input())
    count = 0
    for i in lst:

        if C//i > 0:
            change[count] = C//i
            C = C - (C//i)*i
        count += 1
        
    print(*change)
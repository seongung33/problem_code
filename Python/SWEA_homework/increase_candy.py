'''
증가하는 사탕 수열

1. 순 증가
2. 1개 이상 
3. 조건을 만족시키기 위해 숫자를 감소

높이 차이의 +1 만큼 먹는다.

최악의 경우 (3000, 3000, 3)
3000*3000 이다

'''

# import sys
# sys.stdin = open("input.txt", "r"



T = int(input())
for test in range(1, T+1):
    A, B, C = map(int, input().split())
    if B < 2 or C < 3:
        print(F"#{test} -1")
        continue
    cnt = 0
    if B >= C:
        cnt += B - (C-1)
        B = C - 1

    if A >= B:
        cnt += A - (B-1)
        A = B - 1
    print(F"#{test} {cnt}")
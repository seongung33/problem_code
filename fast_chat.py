T = int(input())
for test in range(1, T + 1):
    A, B = input().split()
    # A의 길이 - B와 일치하는 개수*B의 길이
    ans = 0
    for i in A:
        cnt = 0
        for j in B:
            if i == j:
                cnt += 1
        if cnt == len(B):
            ans += 1

    print(f"#{test} {len(A) - len(B)*ans}")
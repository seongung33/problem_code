T = int(input())
for test in range(1, T +1):
    N = int(input())
    mat = [input() for _ in range(N)]


    mid = N//2

    produce = 0
    for i in range(N):
        for j in range(N):
            if abs(mid - i) + abs(mid - j) <= mid:
                produce += int(mat[i][j])
    print(F"#{test} {produce}")

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    matrix =[list(map(int, input().split())) for _ in range(N)]
    s = 0
    for i in range(N):
        for j in range(N):
            s += matrix[i][j]
    print(f"#{test} {s}")
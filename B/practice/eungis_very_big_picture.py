T = int(input())
for  test in range(1, T+1):
    H, W, N, M = map(int, input().split())
    dream = [input() for _ in range(H)]
    teacher = [input() for _ in range(N)]



    def valid(i, j):
        for y in range(H):
            for x in range(W):
                if dream[y][x] == teacher[i+y][j+x]:
                    continue
                else:
                    return False
            
        return True
    cnt = 0
    for i in range(N-H+1):
        for j in range(M-W+1):
            if valid(i, j):
                cnt += 1
    
    print(F"#{test} {cnt}")
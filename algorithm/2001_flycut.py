T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            now_fly = 0
            for y in range(M):
                for x in range(M):
                    now_fly +=mat[y+i][x+j]
            
            max_fly = max(max_fly, now_fly)
    
    print(F"#{test} {max_fly}")
T= int(input())

def cost(k):
    return k*k +(k-1)*(k-1)

def in_range(y, x):
    return 0<= y < N and 0<= x < N

def area(y, x, k):
    cnt = 0
    for i in range(N+2*k):
        for j in range(N+2*k):
            if abs(i-y) + abs(j-x) < k:
                if in_range(i, j):
                    if home_map[i][j] == 1:
                        cnt += 1
    return cnt
    





for test in range(1, T+1):
    N, M = map(int, input().split())
    home_map = [list(map(int, input().split())) for _ in range(N)]

    # house_y_x = []
    # for i in range(N):
    #     for j in range(N):
    #         if home_map[i][j] == 1:
    #             house_y_x.append((i, j))
    
    max_cnt = 0
    # 시작지점 모든 위치
    for i in range(N):
        for j in range(N):
            for q in range(1, N+5):
                cnt = area(i, j, q)
                charge = cost(q)
                if cnt*M >= charge:
                    max_cnt = max(max_cnt, cnt)

    print(F"#{test} {max_cnt}")
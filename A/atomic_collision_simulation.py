from collections import defaultdict
# 상 하 좌 우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    # x, y, d, k
    atomic_list = [[0]*4 for _ in range(N)]

    dic_xy= {}
    for i in range(N):
        x, y, d, k = map(int, input().split())
        atomic_list[i] = [x*2, y*2, d, k]
        dic_xy[(x*2, y*2)] = [(d, k)]
    
    ans = 0
    t = 0
    while t <4000:
        dic_new_xy = {}
        for key, value in dic_xy.items():
            x, y = key
            for i in dic_xy[key]:
                d, k = i
                ny = y + dy[d]
                nx = x + dx[d]
                if (nx, ny) not in dic_new_xy:
                    dic_new_xy[(nx, ny)] = [(d, k)]
                else:
                    dic_new_xy[(nx, ny)].append((d, k))
        for key, value in dic_new_xy.items():
            if len(value) > 1:
                # print(dic_new_xy[key])
                for i in dic_new_xy[key]:
                    d, k = i
                    ans += k
                dic_new_xy[key] = []
        dic_xy = dic_new_xy
        t += 1

    print(F"#{test} {ans}")
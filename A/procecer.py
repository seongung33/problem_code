'''
가장자리에는 전원이 흐른다.
core와 전원을 연결하는 전선은 직선으로만
절대 교차는 안된다.
가장자리 코어는 선이 없어도 연결 된 것이다.
'''
def core():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                # 가장자리 제외하기
                if  0< i < N-1 and 0 < j < N-1:
                    starts.append([i, j])


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(y, x):
    return 0<=y < N and 0<= x < N

def dfs(starts, k, connected):
    global cnt, max_cnt, max_cnt_2, wow, max_core
    
    if k == core_num:
        if connected >max_core:
            max_core = connected
            max_cnt = cnt
        elif connected == max_core:
            max_cnt = min(max_cnt, cnt)
        return



    y, x = starts[k]
    
    # 연결 X


    for i in range(4):
        valid = True
        point = []
        visited[k] = 1
        for j in range(1, N):
            ny = y +dy[i]*j
            nx = x +dx[i]*j
            # 끝까지 도달
            if not in_range(ny, nx):
                break
            if mat[ny][nx] != 0:
                    valid = False
                    break
            point.append([ny, nx])
        if valid:
            for py, px in point:
                mat[py][px] = 2
            cnt += len(point)
        
            dfs(starts, k +1, connected+1)
            cnt -= len(point)
            for py, px in point:
                mat[py][px] = 0

    dfs(starts, k+1, connected)

        




T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    starts = []
    core()
    # print(starts[0])
    cnt = 0
    max_cnt = 99999999999
    max_cnt_2 = 0
    core_num = len(starts)
    max_core = 0
    visited = [0]*core_num
    # print(core_num)
    wow = False
    dfs(starts, 0, 0)
    
    if wow:
        print(F"#{test} {max_cnt}")
    else:
        print(F"#{test} {max_cnt_2}")
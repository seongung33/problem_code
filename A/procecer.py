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

def elec(i, j, d):
    for k in range(1, N):
        ny = i+ dy[d]*k
        nx = j+ dx[d]*k
        if not in_range(ny, nx):
            return True, k
        if visited[ny][nx] != 0:
            return False, k


def dfs(visited, core_num, cnt, idx):
    global max_cnt, max_num
    if max_num < core_num:
        max_cnt = cnt 
        max_num = core_num
        # print(max_cnt, max_num)

    elif max_num == core_num:
        max_cnt = min(max_cnt, cnt)
        # print(max_cnt, max_num)
    
    if  idx >= len(starts):
        return
    y, x = starts[idx]

    for d in range(4):
        line, k = elec(y, x, d)
        if line:
            new_cnt = 0
            for i in range(1, k):
                ny = y + dy[d]*i
                nx = x +dx[d]*i
                visited[ny][nx] = 2
                new_cnt += 1
            dfs(visited, core_num+1, cnt + new_cnt,idx+1)
            for q in range(1, k):
                ny = y + dy[d]*q
                nx = x +dx[d]*q
                visited[ny][nx] = 0

        
    dfs(visited, core_num, cnt,idx+1)


T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    starts = []
    core()
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                visited[i][j] = mat[i][j]
    max_num = 0
    max_cnt = float('inf')

    dfs(visited, 0, 0, 0)

    print(F"#{test} {max_cnt}")
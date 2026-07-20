"""
제자리 오거나 블랙홀에 빠지면 끝  
벽이나 블록에 부딪힌 횟수가 점수 - 웜홀 통과 X  
최댓값 구하기  
"""
T = int(input())
# 동 남 서 북 방향으로 가는 거임
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

dic = {
    1:(2, 0, 3, 1),
    2:(2, 3, 1, 0),
    3:(1, 3, 0, 2),
    4:(3, 2, 0, 1),
    5:(2, 3, 0, 1),
}

def in_range(y, x):
    return 0<= y < N and 0 <= x < N 



def dfs(cnt, y, x, d):
    global max_cnt, sy, sx

    ny = y + dy[d]
    nx = x + dx[d]

    # 1. 벽 처리 (이게 최우선)
    if not in_range(ny, nx):
        # 벽 밖 좌표(ny, nx)는 어차피 시작점(sy, sx)일 리가 없음.
        # 따라서 여기서 즉시 방향만 바꿔서 다음 재귀로 넘김.
        # 다음 재귀에서 y+dy[d]를 하면 다시 맵 안으로 들어오게 됨.
        dfs(cnt + 1, ny, nx, (d + 2) % 4)
        return

    # 2. 종료 조건 (이제 ny, nx는 무조건 맵 안쪽임)
    # 맵 안쪽일 때만 시작점인지, 블랙홀인지 안전하게 검사
    if (ny, nx) == (sy, sx) or mat[ny][nx] == -1:
        if cnt > max_cnt:
            max_cnt = cnt
        return
    
    # 3. 그 외 오브젝트 처리 (0, 블록, 웜홀)
    target = mat[ny][nx]
    if target == 0:
        dfs(cnt, ny, nx, d)
    elif 1 <= target <= 5:
        dfs(cnt + 1, ny, nx, dic[target][d])
    else: # 웜홀
        h1, h2 = warmhole_dic[target]
        wy, wx = h2 if h1 == (ny, nx) else h1
        dfs(cnt, wy, wx, d)


for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    warmhole_dic = {
        6:[],
        7:[],
        8:[],
        9:[],
        10:[],
    }
    for i in range(N):
        for j in range(N):

            if mat[i][j] in (6, 7, 8, 9, 10):
                num = mat[i][j]
                warmhole_dic[num].append((i, j))

    # print(warmhole_dic)
    # print(dic[1][1])
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                for d in range(4):
                    sy = i
                    sx = j
                    dfs(0, i, j, d)
    print(F"#{test} {max_cnt}")

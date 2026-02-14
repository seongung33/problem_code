#델타
#북 남 서 동
dy = [-1, 1, 0, -0]
dx = [0, 0, -1, 1]

# 매트릭스 바깥 못 나가게 하기
def in_range(y, x):
    return 0<= y < N and 0<= x < N

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    # 공 굴리기 시작지점 완전 탐색
    for i in range(N):
        for j in range(N):
            si = i
            sj = j
            cnt = 0
            while True:
                print(si, sj)
                cnt += 1
                lst = []
                for d in range(4):
                    ny = si + dy[d]
                    nx = sj + dx[d]
                    if in_range(ny, nx) and matrix[si][sj] > matrix[ny][nx]:
                        # if matrix[si][sj] > matrix[ny][nx]:
                        y = ny
                        x = nx
                        lst.append([y, x])
                mi = i
                mj = j
                for y, x in lst:
                    if matrix[mi][mj] > matrix[y][x]:
                        mi = y
                        mj = x
                
                if matrix[mi][mj] >= matrix[si][sj]:
                    break # while True
                si = mi
                sj = mj
            max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")
                
            
                

            
            
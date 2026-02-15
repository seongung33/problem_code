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
                # print(si, sj)
                cnt += 1
                lst = []
                # 4방향 탐색
                for d in range(4):
                    ny = si + dy[d]
                    nx = sj + dx[d]
                    # 인덱스 범위 밖 제거 and 중앙 값 보다 작은 방향만 통과
                    if in_range(ny, nx) and matrix[si][sj] > matrix[ny][nx]:
                        # if matrix[si][sj] > matrix[ny][nx]:
                        # 값 저장 후 리스트에 저장
                        y = ny
                        x = nx
                        lst.append([y, x])
                # 4방향 중 제일 작은 값을 찾아내야 한다.
                mi = si
                mj = sj
                # 중앙보다 작은 방향 중 제일 작은 방향을 탐색한다.
                for y, x in lst:
                    if matrix[mi][mj] > matrix[y][x]:
                        mi = y
                        mj = x
                # 만약 mi, mj값이 갱신되지 않았다면 중앙값 보다 작은 방향이 없었다는 것
                if matrix[mi][mj] == matrix[si][sj]:
                    # 따라서 while문을 종료하고 다음 완전 탐색으로 넘어간다.
                    break # while True
                # 반복문이 돈다면 해당 방향으로 이동 한다.
                si = mi
                sj = mj
            #반복문 종료시 현재 이동한 칸수와 현재까지 최대 이동 칸수를 비교한다.
            max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")
                
            
                

            
            
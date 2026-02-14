# 괴물 찾기
def monster():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                return i, j

# 델타
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# 인덱스 범우 밖 체크
def in_range(y, x):
    return 0 <= y <N and 0 <= x < N
T = int(input())
for test in range(1, T + 1):
    N= int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 0 빈칸
    # 1 벽
    # 2 괴물
    # 괴물위치 설정
    si, sj = monster()
    # 전체 크기 - 괴물의 레이저 수를 통해 계산한다.
    cnt = N*N 
    print(cnt)
    #벽은 안전한 칸에서 제외기 때문에 빼준다.
    for i in range(N):
        for j in range(N):
            #벽일경우
            if matrix[i][j] == 1:
                cnt -= 1
    print(cnt)
    #레이저가 닿이는 곳도 빼준다.
    for d in range(4):
        # 괴물의 자리는 못 쏘기 때문에 1 부터 시작한다.
        for i in range(1, N):
            ny = si + dy[d]*i
            nx = sj + dx[d]*i
            # 괴물의 광선이 벽에 닿이면 막히기 때문에 해당 방향으로 더이상 진행하지 않는다.
            # 방향 for문과 거리의 for문 순서를 잘 설정 해야 한다.
            if in_range(ny, nx) and matrix[ny][nx] == 1:
                break
            if in_range(ny, nx) and matrix[ny][nx] == 0:
                cnt -= 1
                # print(cnt)
    print(F"#{test} {cnt+1}")

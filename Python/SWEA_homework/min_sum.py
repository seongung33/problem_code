
# 델타
dy = [0, 1]
dx = [1, 0]
# 인덱스 탈출 방지
def in_range(y, x):
    return 0<= y < N and 0<= x < N

def recur(i, j, s, min_s):
    
    # 가지치기 
    if s > min_s:
        return min_s

    # 마지막 위치 도달시 종료
    if i == N-1 and j == N-1:
        # 최솟값 반환
        return min(min_s, s)
    # 오른쪽으로 가기, 아래로 가기 이므로 range(2)
    for d in range(2):
        ny = i + dy[d]
        nx = j + dx[d]
        # 인덱스 범위 탈출시 돌아가기
        if not in_range(ny, nx):
            continue
        # 위치별 누적합 + 최솟값도 갖고 다니기
        min_s = recur(ny, nx, s+mat[ny][nx], min_s)
    return min_s
T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]


    min_s = recur(0, 0, mat[0][0], float('inf'))
    print(F"#{test} {min_s}")
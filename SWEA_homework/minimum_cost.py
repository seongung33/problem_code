T = int(input())
import heapq
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 인덱스 에러 방지
def is_range(y, x):
    return 0 <= y < N and 0 <= x < N


for test in range(1, T+1):
    N = int(input())
    # 지도
    mat = [list(map(int, input().split())) for _ in range(N)]
    # 방문지도 (값을 저장하여 해당 위치의 최소비용 갱신)
    visited = [[float('inf')]*N for _ in range(N)]
    # 최소 힙 사용
    pq = []
    # 시작 점 힙에 넣기
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        # 팝
        w, y, x = heapq.heappop(pq)
        # print(w, y, x)
        # 이미 최솟값이면 다음 팝 하기
        if visited[y][x] < w:
            continue
        # 현재가 최솟값이므로 갱신
        visited[y][x] = w
        # 4방향 델타
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            # 인덱스 에러 방지
            if is_range(ny, nx):
                # 기본 이동 비용 1
                cost = 1
                # 이동 하는 곳이 더 높으면 높이 만큼 연료 추가
                if mat[y][x] < mat[ny][nx]:
                    cost += (mat[ny][nx] - mat[y][x])

                # 0, 0에서의 소비량이 기준이므로 현재 위치의 소비량 저장
                cost += visited[y][x]

                # 다음으로 갈 때 이미 연료를 더 많이 쓰면 패스한다.
                if cost > visited[ny][nx]:
                    continue
                # 최솟값 갱신이 된다면 푸쉬
                visited[ny][nx] = cost
                heapq.heappush(pq,(cost, ny, nx))

    print(F"#{test} {visited[N-1][N-1]}")
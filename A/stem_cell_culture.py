'''
생명력: x
x시간 동안 비활성 후 x 시간이 지나면 활성상태가 된다.  
x시간 동안 살 수 있으며 이후에 죽는다.
활성화된 세포는 상,하, 좌, 우 네 방향 동시에 번식한다.
두개 이상이 동시에 번식하려고 하면 생명력 수치가 높은 줄기 세포가 차지한다. 
k시간 후 살아있는 줄기세포(비활성 + 활성)의 수를 구하라 

무한대의 크기: N//2, M//2 가 리스트의 중심이라면 
끝에 1의 세포가 존재하고 k만큼 퍼진다면 k//2 만큼 진행  
상하좌우 모두 가능하니 N+k, M+k 크기의 리스트 생성? 

세포를 델타로 이동시키고 
세포의 활성화 상태, 비활성화 상태, 죽음을 표기해야 한다.
2차원의 방문 배열에 
0은 세포 존재 x, 1: 비활성, 2: 활성, 3: 죽음으로 표기?  
비활성화되고 활성화 되는걸 세야하니 3차원으로 변경 후 
3차원 자리의 첫번째에 세포 상태
두번째에 비활성화, 활성화 상태시의 시간 기록 
if visit in (1, 2):
    시간 흐르기
    0이 라면 세포 상태 변경

'''
from collections import deque
T = int(input())
for test in range(1, T+1):
    N, M, k = map(int, input().split())
    first_grid = [list(map(int, input().split())) for _ in range(N)]

    grid = [[0]*(M+k) for _ in range(N+k)]

    #방문    
    visited = [[[0]*2 for _ in range(M+k)] for _ in range(N+k)]


    # 중앙에 세포 삽입
    for i in range(N):
        for j in range(M):
            if first_grid[i][j]:
                grid[(k)//2+i][(k)//2+j] = first_grid[i][j]
                # 비활성 상태
                visited[(k)//2+i][(k)//2+j][0] = 1
                visited[(k)//2+i][(k)//2+j][1] = first_grid[i][j]
            
    #델타
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # k번 퍼지기
    for _ in range(k):
        # 세포 위치 저장 + 값
        q = deque()
        for i in range(N+k):
            for j in range(M+k):


                # 비활성 상태라면
                if visited[i][j][0] == 1:
                    visited[i][j][1] -= 1
                    # 비활성화 > 활성화
                    if visited[i][j][1] == 0:
                        visited[i][j][0] = 2
                        visited[i][j][1] = grid[i][j]


                # 활성화 상태라면
                elif visited[i][j][0] == 2:

                    # 활성화 종료 됐다면 사망
                    if visited[i][j][1] == 0:
                        visited[i][j][0] = 3
                        visited[i][j][1] = 0

                    # 종료되지 않았다면
                    elif visited[i][j][1] == grid[i][j]:
                        for d in range(4):
                            ny = i +dy[d]
                            nx = j + dx[d]
                            if visited[ny][nx][0] == 0:
                                q.append([grid[i][j], ny, nx])
                    visited[i][j][1] -= 1
        
        # 세포 번식
        q = sorted(q, reverse=True)
        q = deque(q)
        while q:
            vital, ny, nx = q.popleft()
            # 빈칸이면 번식 가능
            if not grid[ny][nx] and visited[ny][nx][0] == 0:
                # 그리드 표시
                grid[ny][nx] = vital
                # 비활성상태
                visited[ny][nx][0] = 1
                # 비활성 카운트
                visited[ny][nx][1] = vital
    cnt = 0
    for i in range(N+k):
        for j in range(M+k):
            if visited[i][j][0] in (1, 2) and visited[i][j][1]:
                cnt += 1
    print(F"#{test} {cnt}")

"""
bfs로 풀어보기
좌표, 세포 상태, 활성 비활성 시 생명력 카운트, 
같은 좌표엔 생명력 큰 값이 차지
방문에 활성 비활성, 카운트 넣어주면 될듯..?

priority Queue 라는걸 써라고 지피티가 알려줌 
큐에서 값에 우선순위를 매겨 작은 값부터 빠져나간다.
이진트리에서 배운 max heap min heap 같은거인듯
"""
import heapq
T = int(input())
for test in range(1, T+1):
    N, M, k = map(int, input().split())
    first_grid = [list(map(int, input().split())) for _ in range(N)]

    grid = [[0]*(M+k) for _ in range(N+k)]

    pq = []
    visited = [[[0]*2 for _ in range(M+k)] for _ in range(N+k)]


    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for i in range(N):
        for j in range(M):
            if first_grid[i][j]:
                grid[k//2+i][k//2+j] = first_grid[i][j] 
                visited[k//2+i][k//2+j][1] = grid[k//2+i][k//2+j]
                visited[k//2+i][k//2+j][0] = 1
                heapq.heappush(pq, (0, -first_grid[i][j], k//2+i, k//2+j))
    
    while pq:
        t, cnt, i, j = heapq.heappop(pq)
        cnt = -cnt
        if t >k-1:
            continue
        

        # 비활성 상태
        if visited[i][j][0] == 1:
            visited[i][j][1] -= 1
            # 활성화로 변경
            if  visited[i][j][1] == 0:
                visited[i][j][0] = 2
                visited[i][j][1] = grid[i][j]
                heapq.heappush(pq, (t+1, -grid[i][j], i, j))
            else:
                heapq.heappush(pq, (t+1, -grid[i][j], i, j))


        elif visited[i][j][0] == 2:
            if visited[i][j][1] == grid[i][j]:
                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if visited[ny][nx][0] == 0:
                        visited[ny][nx][0] = 1
                        grid[ny][nx] = grid[i][j]
                        visited[ny][nx][1] = grid[ny][nx]
                        heapq.heappush(pq, (t+1, -grid[ny][nx], ny, nx))
            visited[i][j][1] -= 1
            if visited[i][j][1] == 0:
                visited[i][j][0] = 3
                visited[i][j][1] = 0

            else:
                heapq.heappush(pq, (t+1, -grid[i][j], i, j))

            
    
    ans= 0

    for i in range(N+k):
        for j in range(M+k):
            if visited[i][j][0] in (1, 2) and visited[i][j][1]:
                ans += 1
    print(F"#{test} {ans}")


    """
    최적화
    """

import heapq

T = int(input())
for test in range(1, T + 1):
    N, M, K = map(int, input().split())
    first_grid = [list(map(int, input().split())) for _ in range(N)]

    # K 시간 동안 최대 사방으로 K/2만큼 퍼질 수 있으므로 여유 있게 설정
    offset = K // 2 + 1
    grid_size_y = N + K + 2
    grid_size_x = M + K + 2
    
    # grid[i][j]: 세포의 생명력(X)
    # birth[i][j]: 세포가 탄생한 시각(S)
    grid = [[0] * grid_size_x for _ in range(grid_size_y)]
    birth = [[-1] * grid_size_x for _ in range(grid_size_y)]

    pq = [] # (활성화=번식 시점, -생명력, r, c)
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for i in range(N):
        for j in range(M):
            if first_grid[i][j]:
                r, c = i + offset, j + offset
                grid[r][c] = first_grid[i][j]
                birth[r][c] = 0
                # 0초에 태어난 세포는 X초 후에 번식(활성화)함
                heapq.heappush(pq, (grid[r][c], -grid[r][c], r, c))

    while pq:
        t, neg_p, r, c = heapq.heappop(pq)
        p = -neg_p
        
        # K시간까지만 번식 가능 (t초에 번식하면 t+1초부터 새 세포 탄생)
        if t >= K:
            continue

        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            # 아직 세포가 없는 곳만 번식 가능
            if birth[nr][nc] == -1:
                birth[nr][nc] = t + 1 # t초에 활성화되어 t+1초에 번식 완료
                grid[nr][nc] = p
                # 새 세포는 (탄생시점 + 생명력) 시점에 번식함
                heapq.heappush(pq, (birth[nr][nc] + p, -p, nr, nc))

    # 최종 생존 계산
    ans = 0
    for i in range(grid_size_y):
        for j in range(grid_size_x):
            if birth[i][j] != -1:
                # 생존 조건: 탄생시각 + 생명력 * 2 > K
                if birth[i][j] + 2 * grid[i][j] > K:
                    ans += 1
                    
    print(f"#{test} {ans}")
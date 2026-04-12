"""
군집의 위치, 군집 내 미생물 수, 이동방향이 주어진다.  
이동방향은 상하좌우  

1. 1시간마다 이동방향에 있는 셀로 이동
2. 약품이 칠해진 곳으로 가면 절반이 죽고 이동방향이 반대로
3. 홀수면 소수점을 버린다. 
4. 만나면 합쳐진다. 방향은 군집이 큰 방향으로 이동  
5. M시간 동안 격리. M시간 후 남아있는 미생물의 총 합은?
이동 중 만나는 것은 겹치지 않는다.
"""

"""
50개 15초
N 100 * 100
군집 천개  
시간 1000
1,000,000 
50,000,000 
1초 대
N 크기 두개 사용시
1억: 3초
시간 충분
"""
from collections import deque
T = int(input())
# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def red_cell(y, x):
    # 약품에 닿이면
    if y <= 0 or x <= 0 or y >= N-1 or x >= N-1:
        return True
    # 안 닿이면
    else:
        return False


for test in range(1, T+1):
    # 셀 개수, 격리 시간, 미생물 군집 수
    N, M, K = map(int, input().split())
    # y, x, 미생물 수, 방향
    micro_list = [[0]*4 for _ in range(K)]
    dic = {}
    for i in range(M):
        dic[i] = set()
    for i in range(K):
        # 군집의 y, x, 미생물 수, 이동방향
        y, x, num, d = map(int, input().split())
        
        micro_list[i] = [y, x, num, d-1]

    # print(micro_list)
    for i in range(M):
        visited = [[[] for _ in range(N)] for _ in range(N)]

        for j in range(K):
            y, x, num, d = micro_list[j]

            if num == 0:
                continue

            ny = y + dy[d]
            nx = x + dx[d]
        #빨간색에 닿이면
            if red_cell(ny, nx):
                num = num // 2
                if num == 0:
                    micro_list[j][2] = 0
                    continue
                if d == 1:
                    d -= 1
                elif d == 0:
                    d += 1
                elif d == 2:
                    d += 1
                elif d == 3:
                    d -= 1
                micro_list[j][3] = d
                micro_list[j][2] = num

            visited[ny][nx].append(j)
            if len(visited[ny][nx]) == 2:
                dic[i].add((ny, nx))
            micro_list[j][0], micro_list[j][1] = ny, nx

        if not dic[i]:
            continue

        for ny, nx in dic[i]:

            first_idx = visited[ny][nx][0]
            sum_num = micro_list[first_idx][2]
            max_idx = first_idx
            max_num = micro_list[first_idx][2]

            for q in range(1, len(visited[ny][nx])):
                idx = visited[ny][nx][q]
                sum_num += micro_list[idx][2]
                if micro_list[idx][2] > max_num:
                   max_num = micro_list[idx][2]
                   micro_list[max_idx][2] = 0
                   max_idx = idx
                else:
                   micro_list[idx][2] = 0
            micro_list[max_idx][2] = sum_num
        



            
            

        # 1 time 끝
    ans = 0
    # print(visited)
    for y, x, num, d in micro_list:
        ans += num

    print(F"#{test} {ans}")
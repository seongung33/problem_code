""""
시간이 흐르면 비활성 힙에서 꺼내기 
꺼내면 퍼지고 활성화 세포 상태 그럼 활성화 힙을 만든다?  
메모리 낭비가 심할듯.. 그럼 어디서 관리? 
완탐은 시간 오래 걸리니까 
힙을 만들어서 시간대로 채워둔다. 사실 이게 제일 베스트 일듯?

그럼 힙이 두개

하나는 비활성 세포 관리 힙

하나는 활성화 세포 관리 힙
"""

import heapq
T = int(input())
for test in range(1, T+1):
    # 최대 힙 사용
    # 비활성 세포 관리
    none_active = []


    N, M, K = map(int, input().split())
    mat = [[0]*(350) for _ in range(350)]

    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(M):
            mat[151+i][151+j] = a[j]
            if a[j]:
                heapq.heappush(none_active, (a[j], -a[j], 151+i, 151+j))
    

    # 델타
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    #활성화 세포
    active = []
    active2 = []
    # print(none_active)
    t = 0
    while t <= K:

        # 활성화 첫 시간에 어떻게  퍼뜨릴 것인가???
        while active and active[0][0] == t:
            time, power, timepower, y, x = heapq.heappop(active)
            power = -power
            heapq.heappush(active2, timepower)
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if mat[ny][nx] == 0:
                    mat[ny][nx] = power
                    # print(mat[ny][nx])
                    heapq.heappush(none_active, (t+power, -power, ny, nx))

        # 이후 활성화 세포 카운트용 저장
        while active2 and active2[0] == t:
            heapq.heappop(active2)


        # 비활성 세포 보관 and 활성화 세포로 넘기기
        while none_active and none_active[0][0] == t:
            time, power, y, x = heapq.heappop(none_active)
            power = -power
            # print(power)
            heapq.heappush(active, (t+1, -power, t+power, y, x))



            # for d in range(4):
            #     ny = y + dy[d]
            #     nx = x + dx[d]
            #     if mat[ny][nx] == 0:
            #         mat[ny][nx] = power
            #         # print(mat[ny][nx])
            #         heapq.heappush(none_active, (t+power+1, -power, ny, nx))
        
        # print(t)
        # print(none_active, len(none_active))
        # print(active, len(active))
        # print(active2, len(active2))
        t += 1

        
    ans = len(none_active) + len(active) + len(active2)
    print(F"#{test} {ans}")

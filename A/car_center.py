"""
N개의 접수창구
M개의 정비 창구

접수창구: 고장 접수
정비창구: 차량 정비
접수창구 i 에서 고장 접수 처리 시간 ai
정비창구 j에서 차량정비 처리 시간 bj 
방문고객 k명  
k의 고객 도착시간: tk 

고객의 이동경로: 도착 -> 대기 후 접수창구 -> 접수 후 -> 차량 정비 
빈 공간이 없다면 생길때까지 기다린다. 

접수 창구 규칙
1. 여러 고객 대기시 고객번호가 낮은 순
2. 빈 창구가 여러개면 접수 창구가 낮은 곳으로 간다.  

정비 창구 규칙
1. 먼저 기다리는 고객 우선
2. 동시에 정비창구 도착시 창구번호가 낮은사람 우선
3. 빈 창구가 여러 개면 번호가 낮은 곳으로 이동

정답: 지갑을 분실한 고객과 같은 창구, 같은 정비 창구 이용한 고객 번호들의 합 출력
없을시 -1 

접수창구 리스트, 정비 창구 리스트. 
저장해야될 것: 고객번호, 접수창구 번호, 정비창구 번호 

시간단위 계산시: 1000*1000 백만
"""

import heapq

T = int(input())
for test in range(1, T+1):
    # 지갑 둔 사람 창구번호 A, B
    N, M, K, A, B = map(int, input().split())
    ai = list(map(int, input().split())) # 접수 창구 N개
    bj = list(map(int, input().split())) # 정비 창구 M개
    tk = list(map(int, input().split())) # 고객 방문 시간 K개

    # 접수 대기 힙
    q_ai = []
    for i in range(K):
        heapq.heappush(q_ai, (tk[i], i))
    # 접수 상태 확인, 소비자 시간
    ai_v = [[0]*2 for _ in range(N)]
    # 정비 대기 힙
    q_bj = []

    bj_v = [[0, 0] for _ in range(M)] 
    # 인덱스가 고객방문 시간
    ans = [[0, 0, 0] for _ in range(K)]
    time = 0
    finished_k = 0
    while finished_k < K:
        # 접수 창구 처리
        for i in range(N):
            if ai_v[i][0] >0:
                ai_v[i][0] -= 1
                if ai_v[i][0] == 0:

                    customer_num = ai_v[i][1]
                    heapq.heappush(q_bj, (time, i,  customer_num))

        # 정비 창구 처리
        for i in range(M):
            if  bj_v[i][0] > 0:
                bj_v[i][0] -= 1
                if bj_v[i][0] == 0:
                    finished_k += 1

        # 새 고객 접수 창구 배정
        for i in range(N):
            if ai_v[i][0] == 0 and q_ai and q_ai[0][0] <= time:
                t, customer_num = heapq.heappop(q_ai)
                ai_v[i][0] = ai[i]
                ai_v[i][1] = customer_num
                ans[customer_num][0] = i
                ans[customer_num][2] = t

        # 정비 창구 배정customer_num
        for i in range(M):
            if bj_v[i][0] == 0 and q_bj and q_bj[0][0] <= time:
                t, idx, customer_num = heapq.heappop(q_bj)
                bj_v[i][0] = bj[i]
                bj_v[i][1] = customer_num
                ans[customer_num][1] = i

        time += 1


    a = 0
    for i in range(K):
        if A -1 == ans[i][0] and B -1 == ans[i][1]:
            a += i + 1
    if a == 0:
        a -= 1
    print(F"#{test} {a}")



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

    ai_v = [0]*(N) # 접수 방문
    ai_v_tk = [0]*(N) # 고객 번호
    bj_v = [0]*M # 정비 방문
    ai_v_tk = [0]*(M)

    v_tk = [[0, 0]for _ in range(1001)] # 고객 번호

    a_wait = []
    b_wait = []
    tk_idx = 0
    time = 0

    a_q = tk
    b_q = []

    while True:
        time = a_q.heappop()
        for i in range(N):
            if not ai_v[i]:
                ai_v[i] = ai[i]
                v_tk[time][0] = i
                break
        
        # 접수창구 시간 흐름
        for i in range(N):
            ai_v[i] -= 1
        # 정비창구 시간 흐름
        for i in range(M):
            bj_v[i] -= 1
            


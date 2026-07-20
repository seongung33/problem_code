#5644 무선충전
'''
장판 위에 있으면 자동 충전됨  
사용자들이 지나갈 때 최대로 충전된 합을 구하는 문제 
사용자가 겹쳐 있다면 반반 나누어 가지므로 
다른 곳에 접속이 가능하다면 해당 위치에 접속한다.
'''

# 인덱스 범위 밖 제외
def in_range(y, x):
    return 0<= y < 10 and 0<= x < 10
T = int(input())
for test in range(1, T+1):
    #M 이동 시간, BC_Num : 충전기 개수
    M, BC_num = map(int, input().split())
    A = list(map(int, input().split())) # 사용자 A
    B = list(map(int, input().split())) # 사용자 B
    #BC = 좌표(x, y), C: 거리, P: 충전량
    BC = [list(map(int, input().split())) for _ in range(BC_num)] # 충전기 정보
  
    #델타 중앙 위 오른쪽 아래 왼쪽
    dy = [0, -1, 0, 1, 0]
    dx = [0, 0, 1, 0, -1]

    # A의 이동좌표를 만들자. 
    # x, y
    A_move = [[0, 0]]
    for i in range(M):  
        ny = A_move[i][0] +dy[A[i]]
        nx = A_move[i][1] + dx[A[i]]
        A_move.append([ny, nx])

    # B의 이동좌표를 만들자. 
    #x, y -> y, x  인덱스이므로 -1
    B_move = [[9, 9]]
    for i in range(M):  
        ny = B_move[i][0] +dy[B[i]]
        nx = B_move[i][1] + dx[B[i]]
        B_move.append([ny, nx])
    
    # 매트릭스 생성
    # 10 x 10으로 주어졌다.
    matrix = [[0]*10 for _ in range(10)]
    # 충전기 표시하기
    # 마름모를 어떻게 구현할 것인가..?
    # AI
    def power_area(ya, xa):
        power = []
        # enumerate 사용시 두개의 리스트로 묶여서 반환됨
        for idx, info in enumerate(BC):
            # 그래서 따로 다시 쪼갠다.
            x, y, c, p = info
            center_r = y - 1   # 행
            center_c = x - 1   # 열
            # for i in range(10):
            #     for j in range(10):
            if abs(center_r - ya) + abs(center_c - xa) <= c:
                # if in_range(i, j):
                    # if ya == i and xb == j:
                power.append([idx, p])
        return power 
    # print(power_area(4, 3))
    # print(matrix)
    # 걷기 시작
    # 무선 충전
    a_sum = 0
    b_sum = 0
    total_score = 0
    
    # print(B_move)
    # 한칸씩 이동
    for i in range(M+1):
        same = []
        # 이동 값 저장
        ya, xa = A_move[i]
        yb, xb = B_move[i]
        # 영향 받는 모든 위치의 충전소 저장
        power_a = power_area(ya, xa)
        power_b = power_area(yb, xb)
        # print(power_a, power_b)
        if power_a and power_b:
            for idx_a, a in power_a:
                for idx_b, b in power_b:
                    # 만약 같은 충전소를 쓴다면
                    if idx_a == idx_b:
                        #same에 저장
                        same.append(b)
            # 겹치는 충전소가 없다면 각각 최댓값에 해당하는 power를 받으면 된다.
            if not same:
                a_sum += max([p for i, p in power_a])
                b_sum += max([p for i, p in power_b])
            # 만약 겹친다면
            else:
                max_power_score = 0
                # 모든 경우의 수와 조합을 비교하여 최댓값을 뽑는다.
                for id1, aa in power_a + [[None, 0]]:
                    for id2, bb in power_b +[[None, 0]]:
                        if id1 == id2 and aa!= 0:
                            score = aa
                        else:
                            score = aa + bb
                        max_power_score = max(score, max_power_score)
                # 최댓값 저장
                total_score += max_power_score
        # 어느 한쪽 혹은 둘다 닿는 충전소 없을경우
        else:
            # a가 충전소가 있다면
            if power_a:
                a_sum += max([p for i, p in power_a])
            # b가 충전소가 있다면
            if power_b:
                b_sum += max([p for i, p in power_b])
    print(F"#{test} {a_sum+b_sum+total_score}")

'''
마름모와 충전소가 겹칠경우를 해결하는 것이 매우 번거로운 문제.  
마름모의 공식은 외워두는 것이 좋을 듯 하다.
'''

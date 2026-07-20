T = int(input())

# 판단 함수
# 무선충전 좌표 X, Y 사람좌표 X, Y, 범위
def is_inpower(pX, pY, hX, xY, C):
    if abs(pX - hX) + abs(pY - xY) <= C:
        return True
    return False



dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]
for test in range(1, T+1):
    # 이동시간, 충전기 개수
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))


    BC = [[0]*4 for _ in range(A)]
    for i in range(A):
        #좌표X, Y, 충전범위, 파워
        x, y, c, p = list(map(int, input().split()))
        BC[i][0], BC[i][1], BC[i][2], BC[i][3] = x-1, y-1, c, p
    
    #X, Y
    A_point = [0, 0]
    B_point = [9, 9]
    maxpower = 0
    for i in range(-1, M):
        if i == -1:
            A_point = [0, 0]
            B_point = [9, 9]
        else:
            A_point[0] += dx[move_A[i]]
            A_point[1] += dy[move_A[i]]

            B_point[0] += dx[move_B[i]]
            B_point[1] += dy[move_B[i]]
        # print(A_point, B_point)
        # A가 포함된 파워 뽑기
        lst_A = []
        lst_B = []
        for j in range(A):
            if is_inpower(BC[j][0], BC[j][1], A_point[0], A_point[1], BC[j][2]):
                lst_A.append((BC[j][3], j))
            if is_inpower(BC[j][0], BC[j][1], B_point[0], B_point[1], BC[j][2]):
                lst_B.append((BC[j][3], j))

        lst_A.sort(reverse=True)
        lst_B.sort(reverse=True)
        if lst_A and lst_B:
            if lst_A[0][1] == lst_B[0][1]:
                # 둘의 최대 파워가 같으면 이케저케 계산 해야됨 이거 개히듦 나중에 하기
                if len(lst_B) == 1 and len(lst_A) == 1:
                    maxpower += lst_A[0][0]
                elif len(lst_B) == 1 and len(lst_A) > 1: 
                    maxpower += lst_B[0][0]
                    maxpower += lst_A[1][0]
                elif len(lst_B) > 1 and len(lst_A) == 1: 
                    maxpower += lst_B[1][0]
                    maxpower += lst_A[0][0]
                elif len(lst_B) > 1 and len(lst_A) > 1:
                    if lst_B[1][0] > lst_A[1][0]:
                        maxpower += lst_B[1][0]
                        maxpower += lst_A[0][0]
                    else:
                        maxpower += lst_A[1][0]
                        maxpower += lst_B[0][0]
            else:
                maxpower += lst_A[0][0]
                maxpower += lst_B[0][0]

        if lst_A and not lst_B:
            maxpower += lst_A[0][0]
        if lst_B and not lst_A:
            maxpower += lst_B[0][0]
        # print(maxpower)
    print(F"#{test} {maxpower}")
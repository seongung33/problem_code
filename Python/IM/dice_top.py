# 주사위르 쌓을때 아랫주사위의 윗면 숫자와 윗 주사위의 아랫면 숫자가 같다.
# 4개의 옆면 중에서 한면의 숫자의 합이 최대가 되어야 한다.
# 주사위 돌리기
<<<<<<< HEAD
def dice_change(dice):
    print(dice)
    for i in range(6):
        if dice[i] == 6:
            six = i
            break # for i
    if six == 3:
        temp = dice[1]
        dice[2:5] = dice[1:4]
        dice[1] = temp
        print(dice)
    elif six == 1:
        temp = dice[4]
        dice[2:5] = dice[1:4]
        dice[1] = temp
        print(dice)
    elif six == 4:
        temp = [0, 0]
        temp[0:2] = dice[1:3]
        dice[1:3] = dice[3:5]
        dice[3:5] = temp[0:2]
        print(dice)
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
new_dices = []
i = 0
# for j in range(N):
dice_change(dices[i])

while i < 6:

    dice_change(i)
    for j in range(i+1, 5):
        if dices[i][0] == dices[j+1][5]:
            new_dices.append(dices[j+1])
            new_dices.append(dices[i])
            i += 1
            break # for j
    i += 1
print(new_dices)
=======
# N = int(input())
# dices = [list(map(int, input().split())) for _ in range(N)]
# dict = {
#     0:5,
#     1:3,
#     2:4,
#     3:1,
#     4:2,
#     5:0
# }
# s = 0
# max_s = float('-inf')
# for i in range(6):
#     s = 0
#     for j in range(N-1, -1, -1):
#         if j == N-1:
#             bot = dices[j][i]
#             top = dices[j][dict[i]]
#             max_i = 0
#             for z in range(6):
#                 if z != i and z != dict[i]:
#                     max_i = max(max_i, dices[j][z])
#             s += max_i
#         else:
#             s= 0
#             for k in range(6):
#                 if top == dices[j][k]:
#                     top = dices[j][dict[k]]
#                     max_i = 0
#                     for z in range(6):
#                         if z != i and z != dict[i]:
#                             max_i = max(max_i, dices[j][z])
#                     s += max_i
#     if max_s < s:
#         max_s = s
# print(max_s)


# ============================================
# 백준 2116번: 주사위 쌓기
# ============================================


# ===============================
# 1️⃣ 입력 받기
# ===============================

# ▶ N 입력받는 코드 작성
# ▶ N개의 주사위를 저장할 리스트 생성
# ▶ 반복문을 통해 각 주사위의 6개 숫자 입력받아 저장

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
# ===============================
# 2️⃣ 마주보는 면 정보 정의
# ===============================

# ▶ 주사위는 마주보는 면이 고정되어 있음
# ▶ 인덱스 기준:
#    0 ↔ 5
#    1 ↔ 3
#    2 ↔ 4
# ▶ 이를 딕셔너리 또는 리스트로 정의하는 코드 작성
dict = {
    0:5,
    1:3,
    2:4,
    3:1,
    4:2,
    5:0
}

# ===============================
# 3️⃣ 최종 정답 변수 선언
# ===============================

# ▶ 전체 최대값을 저장할 변수 선언 (0으로 초기화)
max_ans = 0

# ===============================
# 4️⃣ 첫 번째 주사위 바닥 6가지 경우 탐색
# ===============================
for i in range(6):
# ▶ for문 사용
# ▶ 첫 번째 주사위의 바닥 인덱스를 0~5까지 반복


    # ---------------------------
    # 현재 경우의 총합 변수 생성
    # ---------------------------
    
    # ▶ total 변수 생성 (0으로 초기화)
    total = 0

    # ---------------------------
    # 첫 번째 주사위 처리
    # ---------------------------

    # ▶ 현재 바닥 인덱스를 이용해
    #    바닥 값(bottom_value) 저장하는 코드 작성
    bottom_value = dices[N-1][i]
    # ▶ opposite 정보를 이용해
    #    윗면 인덱스 구하는 코드 작성
    opposite_idx = dict[i]
    # ▶ 윗면 값(top_value) 저장하는 코드 작성
    top_value = dices[N-1][opposite_idx]
    # ▶ 현재 주사위의 6개 면 중에서
    #    바닥 인덱스와 윗면 인덱스를 제외한
    #    4개 면 중 최대값 구하는 코드 작성
    #    (반복문 또는 max 활용)
    max_s = 0
    for j in range(6):
        if j != top_value and j !=bottom_value:
            max_s = max(dices[N-1][j])
    # ▶ 구한 최대값을 total에 더하는 코드 작성
    total += max_s

    # ---------------------------
    # 5️⃣ 두 번째 주사위부터 반복
    # ---------------------------
    for j in range(N-2, -1, -1):
    # ▶ 두 번째 주사위(index 1)부터
    #    마지막 주사위까지 반복하는 for문 작성


        # -----------------------------------
        # 이전 주사위의 top_value와 같은
        # 숫자를 현재 주사위에서 찾기
        # -----------------------------------

        # ▶ 현재 주사위의 6개 면을 탐색
        # ▶ 값이 이전 top_value와 같은 인덱스를 찾는 코드 작성
        # ▶ 그 인덱스를 bottom_idx로 저장
        for k in range(6):
            if top_value == dices[j][k]:

        # -----------------------------------
        # 현재 주사위의 윗면 구하기
        # -----------------------------------

        # ▶ opposite 정보를 이용해
        #    bottom_idx의 반대 인덱스를 구하는 코드 작성
        # ▶ 해당 값을 새로운 top_value로 저장
                new_opposite_idx = dict[k]
                new_top_value = dices[j][new_opposite_idx]

        # -----------------------------------
        # 현재 주사위의 옆면 최대값 구하기
        # -----------------------------------
                max_s = 0
                for z in range(6):
                    if z != top_value and z !=bottom_value:
                        max_s = max(dices[N-1][z])
        # ▶ 현재 주사위 6개 면 중
        #    bottom_idx와 top_idx를 제외한
        #    4개 면 중 최대값 구하는 코드 작성

        # ▶ 구한 최대값을 total에 더하는 코드 작성
                total += max_s

    # ---------------------------
    # 6️⃣ 최대값 갱신
    # ---------------------------

    # ▶ answer와 total 중 더 큰 값으로 갱신하는 코드 작성
    if max_ans < total:
        max_ans = total

# ===============================
# 7️⃣ 결과 출력
# ===============================

# ▶ 최종 answer 출력하는 코드 작성
print(max_ans)
>>>>>>> ec395c10134aa1a19a19c855dea3b23571678fe2

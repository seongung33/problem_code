"""
A 음식의 재료만 계산하면 B음식의 재료는 선택되지 않은 음식들이다
즉 절반인 N//2 개의 음식만 선택하면 된다.

"""

T = int(input())

def make_food(cnt, prev):
    global  min_score
    # print(food)
    # 음식 절반 선택
    if cnt == N//2:
        a_food = 0
        # a음식의 시너지 계산
        for i in food:
            for j in food:
                if i == j:
                    continue
                a_food += mat[i][j]
        # b음식은 차집합으로 뽑아낸다.
        b_food = set(range(N)) - set(food)
        b_food = list(b_food)
        b_food_sum = 0
        # b음식 시너지 계산
        for i in b_food:
            for j in b_food:
                if i == j:
                    continue
                b_food_sum += mat[i][j]
        # 두 값의 차 계산
        score = abs(a_food - b_food_sum)
        # print(a_food, b_food)
        # print(score, min_score)
        min_score = min(min_score, score)
        return
    # 가지치기
    # 가지치기 있을거 같은데 안된다. ㅠ

    # 조합이므로 조합 재귀 구현
    for i in range(prev+1, N):

        food.append(i)
        make_food(cnt+1, i)
        food.pop()


for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_score = float('inf')
    food = []


    make_food(0, -1)
    print(F"#{test} {min_score}")
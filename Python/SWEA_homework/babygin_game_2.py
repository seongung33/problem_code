"""
그리디
각 카드를 받고 플레이어가 런 이나 triplet이 있는지 검사한다.
한명만 있다면 그 사람이 이긴다.
둘 다 있다면 비긴다. 
없으면 카드를 받는다

런 이나 triplet 없이 이길 수 없으므로 성립한다.
이렇게 확인하는게 맞나..?
"""

def who_win(a, b):

    # print(a)
    # print(b)
    # print(len(a))
    win_a = False
    win_b = False
    for i in range(0, len(a)-2):
        a1 = a[i]
        b1 = b[i]
        # 트리플
        #a
        if a1 == a[i+1] and a1 == a[i+2]:
            win_a = True
        #b
        if b1 == b[i+1] and b1 == b[i+2]:
            win_b = True
    # 런
    # 왜 이 과정을 거치나요?
    # 만약 1 1 2 2 3 3 같은경우
    # 1 2 3 으로 런이지만 인덱스로 비교시
    # 해당되지 않아서 중복값을 제거합니다.
    a = list(set(a))
    a.sort()
    b = list(set(b))
    b.sort()

    #a
    for i in range(len(a)-2):
        a1 = a[i]
        if a1 + 1 == a[i+1] and a1 +2 == a[i+2]:
            win_a = True
    for i in range(len(b)-2):
        b1 = b[i]
        #b
        if b1 + 1 == b[i+1] and b1+2 == b[i+2]:
            win_b = True

    return win_a, win_b

T = int(input())

for test in range(1, T+1):
    lst = list(map(int, input().split()))


    player1 = []
    player2 = []

    # 카드 한장씩 주기
    for i in range(6):
        player1.append(lst[i*2])
        player2.append(lst[i*2+1])

        # 카드가 세장은 돼야한다.
        if len(player2) < 3:
            continue

        # 정렬
        player2.sort()
        player1.sort()

        win_1, win_2 = who_win(player1, player2)
        # 승자가 나오면 멈춘다.
        # print(win_a, win_b)

        if win_1 or win_2:
            break # for i
    # 둘다 맞추면 카드를 교대로 가져가므로 선 턴이 이긴다.
    if win_1 and win_2:
        ans = 1
    # a만 이김
    elif win_1:
        ans = 1
    # b만 이김
    elif win_2:
        ans = 2
    # 둘다 못 맞춤
    elif not win_1 and not win_2:
        ans = 0
    # 나머진 자동으로 무승부
    print(F"#{test} {ans}")

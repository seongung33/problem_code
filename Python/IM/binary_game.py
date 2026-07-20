T = int(input())
for test in range(1, T + 1):
    p, a, b = map(int, input().split())

    # 승자
    winner = ''

    #a의 이진 탐색 범위
    a_start, a_end = 1, p
    #b의 이진 탐색 범위
    b_start, b_end = 1, p


    #a와 b의 승부
    while True:

        # a가 찾았는가
        a_find = False
        # b 가 찾았는가
        b_find = False

        # a 의 탐색
        a_middle = (a_start + a_end) // 2
        if a_middle == a:
            a_find = True
        elif a_middle > a:
            a_end = a_middle
        elif a_middle < a:
            a_start = a_middle

        # b의 탐색
        b_middle = (b_start + b_end) // 2
        if b_middle == b:
            b_find = True
        elif b_middle > b:
            b_end = b_middle
        elif b_middle < b:
            b_start = b_middle
        # 탐색이 끝났다면 반복문 종료
        if  a_find or b_find is True:
            break
    # 둘 다 찾았을 경우
    if a_find and b_find:
        winner = 0

    # A만 찾았을 경우
    elif a_find is True:
        winner = 'A'

    # B 만 찾았을 경우
    elif b_find is True:
        winner = 'B'
    print(f"#{test} {winner}")

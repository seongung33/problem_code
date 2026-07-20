T = int(input())
for test in range(1, T +1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # True면 정답 False면 스도쿠가 틀림
    ans = True
    # 정답 비교군
    answer = [list(range(1, 10))]
    # 가로 정답 검사
    for i in range(9):
        lst = [0]*9
        for j in range(9):
            lst[j] =sudoku[i][j]
        lst.sort()
        # 두 리스트가 다르면 False 다르다는 것은 겹치는 숫자가 있다는 것
        if lst not in answer:
            ans = False

    # 세로 정답 검사
    for j in range(9):
        lst = []
        for i in range(9):
            lst.append(sudoku[i][j])
        lst.sort()
        # 두 리스트가 다르면 False 다르다는 것은 겹치는 숫자가 있다는 것
        if lst not in answer:
            ans = False

    # 3*3 검사
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            lst = []
            for y in range(3):
                for x in range(3):
                    lst.append(sudoku[i+y][j+x])
            lst.sort()
            if lst not in answer:
                ans = False

    if ans:
        print(F"#{test} 1")
    else:
        print(F"#{test} 0")
    
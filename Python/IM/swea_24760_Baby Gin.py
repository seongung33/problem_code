T = int(input())
for test_case in range(1, T + 1):
    c = [0]*12 # pedding
    numbers = int(input())
    for i in range(6):
        c[numbers % 10] += 1
        numbers = numbers // 10
    # print(c)
    i = 0
    tri = run1 = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -=3
            tri += 1
            continue
        if c[i] >=1 and c[i+1] >=1 and c[i+2] >=1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run1 += 1
            continue
        i += 1
    if run1 + tri == 2:
        print(f"#{test_case} Baby Gin")
    else:
        print(f"#{test_case } Lose")
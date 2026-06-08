T = int(input())
for test in range(1, T+1):
    N = int(input())
    dist = 0
    v = 0
    for i in range(N):
        command = input()
        if len(command) > 1:
            num, num2 = map(int, command.split())
            if num == 1:
                # 가속
                v += num2
                dist += v
            else:
                # 감속
                v -= num2
                if v < 0:
                    v = 0
                dist += v
        else:
            dist += v
        # 현재속도 유지
    print(F"#{test} {dist}")
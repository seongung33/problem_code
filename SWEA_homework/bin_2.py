T = int(input())
for test in range(1, T + 1):
    N = float(input()) # 실수니까 int 가 아닌 float
    i = 1
    ans = 0 # ans == N이면 이진법 입력 종료
    result = "" # 이진법 입력
    while i < 13: # 13이 넘어가면 오버플로우
        if ans + 2**(-i) <= N: # N보다 작거나 같으면 값을 넣을 수 있다.
            # 해당 값을 넣었으니 이진수는 1
            result += '1'
            # 다음 계산을 위해 해당 값을 넣어준다.
            ans += 2**(-i)
            print(ans, result, i)
        else:
            # 안 넣으면 이진수 0을 넣는다.
            result += '0'
        # 이진수가 완성되면 while문을 종료한다.
        if ans == N:
            break  # while i < 13
        # i 값을 증가시켜 준다.
        i += 1

    # i가 13 이상이면 overflow 출력
    if i > 12:
        print(F"#{test}", "overflow")
    # 아니면 정답 출력
    else:
        print(F"#{test} {result}")

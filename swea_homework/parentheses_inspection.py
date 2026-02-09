T = int(input())
for test in range(1, T+1):
    txt = input()

    #짝 검사
    pair = {
        '(':')',
        '{':'}',
        '[':']',
    }

    # 포인터 설정
    top = -1
    ans = 1
    #스택
    stack = [0]* 999999
    for i in txt:
        # print(top)
        if i in '({':
            top += 1
            stack[top] = i
            continue
        elif i in ')}':
            # top이 -1 이면 닫힌 괄호가 먼저 온 것이므로 잘못 된 상태이다.
            if top == -1:
                ans = 0
                break
            else:
                top -= 1
                # 아래의 경우이면 패스한다.
                if pair[stack[top+1]] == i:
                    continue
                elif pair[stack[top+1]] == i:
                    continue
                else:
                    ans = 0
                    break
    if top > -1:
        ans = 0
    print(f"#{test} {ans}")

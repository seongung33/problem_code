for test in range(1, 11):
    n = int(input())
    infix = input()
    # 스택
    stack = [0]*n
    # top
    top = -1
    #완성 단어 (추가예정)
    postfix =''
    # 우선순위
    icp = {'(':3, '-':1, '+':1, '/':2, '*':2 } # 밖
    isp = {'(':0, '-':1, '+':1, '/':2, '*':2 } # 안
    # str로 바로 순회
    for i in infix:
        # 숫자면
        if i not in '(*/+-)':
            postfix += i
        elif i ==')':
            # 열린괄호를 찾을때까지 반복
            while stack[top] !='(':
                top -= 1
                # 꺼내면 무조건 postfix에 저장
                postfix += stack[top+1]
            # 반복문은 (를 만나면 종료하므로 따로 스택에서 제거한다.
            top -= 1
            # 괄호는 postfix에 넣지 않는다.
        # infix에 들어갈 수 있는 모든 경우의 수가 다 나왔다.
        elif i in '(/+*-':
            # 우선순위 비교 후 i의 우선순위가 더 높아야만 들어간다.
            # 단, top에 존재하는게 없다면 무조건 스택에 넣는다.
            #스택이 있다면 top의 비교를 하지 않아도 되지만 현재 이용하는 stack은 실제로 값이 지워지지 않으니
            # 반드시 top의 값이 -1보다 크다는게 있어야 하나...?
            # 적다보니 그럼 왜 or인지 의문이 듦....
            # or 하니 키 에러가 떴다.
            # top이 -1인데 검색하려 해서 뜬 것 and가 맞았다.
            # 가르쳐 준 코드 보니 아래 elif문과 if의 조건 위치가 반대라 그렇다.
            # 아래 코드가 위에 적힌 줄 알고 or라 기억한 것. and가 맞았다!
            if top > -1 and icp[i] <= isp[stack[top]]:
                # 아래 조건을 모두 만족해야 반복할 수 있다.
                while top > -1 and icp[i] <= isp[stack[top]]:
                    #반복하면서 pop 해야한다.
                    top -= 1
                    #꺼내면 무조건 postfix에 넣는다.
                    postfix += stack[top+1]
                # 다 꺼냈으니 연산자를 다시 넣어야 한다.
                top += 1
                stack[top] = i
            # 스택에 아무것도 없거나 i의 우선순위가 스택 최상단의 우선순위보다 높다면
            elif top < 0 or icp[i] > isp[stack[top]]:
                # 스택에 넣는다.push
                top += 1
                stack[top] = i
    #남아있는 스택을 다 뺀다.
    while top > -1:
        top -= 1
        #스택에서 빼면 postfix에 넣는다.
        postfix += stack[top+1]
    # print(postfix)
    #### 연산식 시작
    stack [0]* n
    top = -1
    for i in postfix:
        if i not in '-+*/':
            top += 1
            stack[top] = int(i)
        else:
            if i == '-':
                top -= 1
                right = stack[top+1]
                top -= 1
                left = stack[top+1]
                result = left - right
            elif i == '+':
                top -= 1
                right = stack[top+1]
                top -= 1
                left = stack[top+1]
                result = left + right
            elif i == '/':
                top -= 1
                right = stack[top+1]
                top -= 1
                left = stack[top+1]
                result = left / right
            if i == '*':
                top -= 1
                right = stack[top+1]
                top -= 1
                left = stack[top+1]
                result = left * right
            top += 1
            stack[top] = result

    top -= 1
    ans = stack[top+1]
    print(f"#{test} {ans}")
        
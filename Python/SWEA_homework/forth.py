# 5일차 - Forth
T =int(input())
for test in range(1, T+1):
    lst = list(input().split())
    #스택
    stack = [0]*len(lst)
    #top
    top = -1
    #정답
    ans = ''
    #lst로 반복문
    for i in lst:
        #숫자면
        if i not in '+*/-.':
            # 스택에 넣는다
            top += 1
            # 계산 가능하게 int로 넣는다.
            stack[top] = int(i)
        #숫자가 아니면
        else:
            # 연산기호와 . 두종류가 있다.
            if i in '+*/-':
                #연산기호일 경우
                top -= 1
                right = stack[top+1]
                top -= 1
                left = stack[top+1]
                if i == '+':
                    result = left + right
                elif i == '-':
                    result = left - right
                elif i == '*':
                    result = left * right
                elif i == '/':
                    result = left // right #항상 나누어 떨어진다는 조건이 있다.
                # 결과를 다시 스택에 넣어야 한다.
                top += 1
                stack[top] = result
            # .일 경우
            elif i == '.':
                # 스택에서 남아 있는 값을 꺼낸다.
                top -= 1
                ans = stack[top + 1]
    # 반복 종료 후 스택에 값이 더 남아있다면 이는 오류이다.
    if top != -1:
        ans = 'error'
    print(F"#{test} {ans}")
'''
연산 기호가 더 많다면 이 또한 오류가 떴을 것이다.  
이유는 stack에 더 이상 꺼낼게 없기 때문. 
top을 사용하여 stack 내부에는 값이 있기 때문에 아마도 내 코드는 top 값만 다르지 오류는 뜨지 않았을 것이다.
즉 if top != -1: 로 처리가 된다는 것. 
하지만 append와 pop을 사용했다면 pop이 불가능해 오류가 떴을 것이다. 
이때는 아마 try:-except: 를 이용하여 오류가 뜰 경우 for 문을 멈추고 ans = 'error'로 지정하였을 것 같다.
'''

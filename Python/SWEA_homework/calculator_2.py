# 우선순위
icp = {'*':2, '+':1}
isp = {'*':2, '+':1}

# tc 10개
for test in range(1, 11):
    N = int(input())# 길이
    infix = input()  # 문자열
    def change(infix):
        global icp
        global isp
        stack = [0]*N
        top = -1
        postfix = ''
        for i in infix:
            if i not in '+*':
                postfix += i
            elif i in '+*':
                # 스택이 없거나 icp i의 우선순위가 더 크면 추가
                if top < 0 or isp[stack[top]] < icp[i]:
                    top += 1
                    stack[top] = i
                else:
                    # 스택이 있고 icp값이 더 크지 못하면
                    while top > -1 and isp[stack[top]] >= icp[i]:
                        top -= 1
                        postfix += stack[top + 1]
                    top += 1
                    stack[top] = i
        while top > -1:
            top -= 1
            postfix += stack[top + 1]
        return postfix
    # post = change(infix)
    # print(post)
    def cal(post):
        top = -1
        stack = [0]*N
        for i in post:
            if i not in '+*':
                top += 1
                stack[top] = int(i)
            else:
                if i == '+':
                    top -= 1
                    right = stack[top + 1]
                    top -= 1
                    left = stack[top + 1]
                    res = left + right
                elif i == '*':
                    top -= 1
                    right = stack[top + 1]
                    top -= 1
                    left = stack[top + 1]
                    res = left * right
                top += 1
                stack[top] = res
        top -= 1
        ans = stack[top +1]
        return ans


    post = change(infix)
    print(F"#{test} {cal(post)}")


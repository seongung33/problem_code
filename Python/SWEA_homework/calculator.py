for test in range(1, 11):
    N = int(input())
    infix = input()
    # 중위를 후위로 바꾸는 함수
    def in_post(infix, N):
        postfix = ''
        top = -1
        stack = [0]*N
        for i in infix:
            if i != '+':
                postfix += i
            elif i =='+':
                if not stack:
                    top += 1
                    stack[top] = i
                else:
                    while top > -1:
                        top -= 1
                        postfix += stack[top + 1]
                    top += 1
                stack[top] = i
        while top > -1:
            top -= 1
            postfix += stack[top + 1]
        return postfix

    # 후위 계산 식
    def post_cal(postfix):
        top = -1
        stack = [0]*N
        for i in postfix:

            if i != '+':
                top += 1
                stack[top] = int(i)
            else:
                top -= 1
                right = stack[top + 1]
                top -= 1
                left = stack[top + 1]
                result = left + right
                top += 1
                stack[top] = result
        # 결과값 빼기
        top -= 1
        ans = stack[top + 1]
        return ans


    post = in_post(infix, N)
    print(f"#{test} {post_cal(post)}")


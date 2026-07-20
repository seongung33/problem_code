T = int(input())
for test in range(1, T+1):
    N = int(input())
    st = list(input().strip())
    
    stack = []
    for ch in st:
        stack.append(ch)

        if len(stack) >= 3:
            if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
                stack.pop(-1)
                stack.pop(-1)
                stack.pop(-1)
    
    print(len(stack))
                
        
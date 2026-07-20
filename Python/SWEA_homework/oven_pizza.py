from collections import deque
T= int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split())) # 치즈 양

    q = deque()
    oven = [0]*(M)
    # 덱에 피자 넣기
    for i in range(N):
        q.append(i)
        oven[i] = 1
    
    # BFS 
    while q:
        # print(q)
        # 피자 꺼내기
        pizza_idx = q.popleft()
        pizza = C[pizza_idx]
        # 다 녹았나 확인
        pizza = pizza//2
        C[pizza_idx] = pizza
        if pizza == 0 and  N < M:
        # 다 녹았으면 빼고 다음 피자 넣기
            q.append(N)
            oven[N] = 1
            oven[pizza_idx] = 0
            N += 1
        # 다 녹지 않았다면 다시 넣기
        elif pizza > 0:
            q.append(pizza_idx)

    # 자동적으로 마지막에 피자를 꺼내고 while문이 종료 즉 마지막 꺼낸 피자의 번호가 나온다.
    # 인덱스 이므로 + 1 해야한다.
    print(F"#{test} {pizza_idx+1}")

'''
인덱스 번호를 큐에 넣고 값 계산은 따로 인덱스 번호를 활용하여 풀어야 한다.
그래야 마지막에 어떤 피자를 꺼냈는지 구분하기 쉽다.
'''
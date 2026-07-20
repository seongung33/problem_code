T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))


    # 선형 큐
    # q = [0] * (N+M+100)

    # rear = front = -1
    # # 스택에 기존 값 먼저 넣기
    # for i in range(N):
    #     rear += 1
    #     q[rear] = arr[i]
    # #빼고 넣기 반복
    # for i in range(M):
    #     front += 1
    #     front_value = q[front]
    #     rear += 1
    #     q[rear] = front_value
    # # 첫번째 값을 뽑으므로 front +=1 하고 뽑아야 한다.
    # # enqueue 한 값을 출력하면 되는 것
    # front += 1
    # print(F"#{test} {q[front]}")


    # 원형 큐
    # front = rear = 0
    # q = [0]*(N+1)
    # # 원형 큐에 주어진 값 넣기
    # for i in range(N):
    #     rear = (rear + 1) % N
    #     q[rear] = arr[i]
    # # 원형으로 빼고 넣기
    # for i in range(M):
    #     front = (front+1) % N
    #     front_value = q[front]
    #     rear = (rear + 1) % N
    #     q[rear] = front_value
    # # 마지막에 enqueue 해서 첫번쨰 값 출력
    # front = (front+1) % N
    # print(f"#{test} {q[front]}")

    ## 덱 써보기
    from collections import deque
    # 덱 선언
    q = deque()
    # 기존 값 먼저 넣기
    for i in range(N):
        q.apppend(arr[i])
    
    # 빼고 넣기
    for i in range(M):
        # 빼기
        first_value = q.popleft()
        # 넣기
        q.append(first_value)
    ans = q.popleft()
    print(F"#{test} {ans}")
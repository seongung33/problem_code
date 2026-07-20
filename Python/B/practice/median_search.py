import heapq
T = int(input())
for test in range(1, T+1):
    N, A = map(int, input().split())

    max_h = [-A]
    min_h = []
    ans = 0
    for _ in range(N):
        X, Y = map(int, input().split())
        
        for val in [X, Y]:
            if val < -max_h[0]:
                heapq.heappush(max_h, -val)
            else:
                heapq.heappush(min_h, val)

        while len(max_h) > len(min_h) + 1:
                temp = heapq.heappop(max_h)
                temp = -temp
                heapq.heappush(min_h, temp)
        while len(max_h) < len(min_h) + 1:
                temp = heapq.heappop(min_h)
                heapq.heappush(max_h, -temp)
            
        
        # 3. 현재 중앙값은 항상 max_h의 루트에 있음
        ans += -max_h[0]
    
    answer = ans % 20171109


    print(F"#{test} {answer}")
import heapq

N, M = map(int, input().split())
A_B = [[] for _ in range(N+1)] # A과목 들으면 B로 갈 수 있음
B_A = [[]A_B for _ in range(N+1)] # 날 들으려면 들어야 하는 과목들
for i in range(M):
    A, B = map(int, input().split())
    [A].append(B)
    B_A[B].append(A)

answer = [0]*(N+1)

pq = []
for i in range(1, N+1):
    if not B_A[i]:
        heapq.heappush(pq, (0, i))

while pq:
    now, num = heapq.heappop(pq)
    if answer[num]:
        continue
    answer[num] = now + 1
    for i in A_B[num]:
        valid = True
        for j in B_A[i]:
            if  answer[j] == 0:
                valid = False
                break
        if valid:
            heapq.heappush(pq, (now+1, i))
print(*answer[1:])



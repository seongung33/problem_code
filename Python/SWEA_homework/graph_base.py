# T = int(input())

# def dfs(N, cnt):
#     global ans

#     if cnt >= ans:
#         return
    
#     # if N > M + 10:
#     #     return
    
#     if N > 1000000:
#         return

#     if N <= 0:
#         return
#     if N in sett:
#         return
#     sett.add(N)


#     if N == M:
#         ans = min(ans, cnt)
#         return


#     dfs(N+1, cnt+1)
#     dfs(N*2, cnt+1)
#     dfs(N-10, cnt+1)
#     dfs(N-1, cnt+1)


# for test in range(1, T+1):
#     N, M = map(int, input().split()) 
#     ans = float('inf')
#     sett = set()
#     dfs(N, 0)
#     print(F"#{test} {ans}")


#########################

from collections import deque



T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split()) 
    q = deque()
    q.append((N, 0))
    ans = abs(N-M) + 1
    visited = [0]*1000001

    a = N
    c = 0
    if a < M:
        while a < M:
            a = a * 2
            c += 1
        a = a// 2
        c -= 1
        while a != M:
            a += 1
            c += 1
    else:
        while a > M:
            a -= 10
            c += 1
        a += 10
        c -= 1
        while a !=M:
            a -= 1
            c += 1
    ans = c
    # print(ans)
    while q:
        N, cnt = q.popleft()
        if visited[N]:
            continue
        visited[N] = 1
        if N <= 0:
            continue
        
        if cnt >= ans:
            continue

        if N == M:
            ans = min(ans, cnt)
            continue
        if 0< N*2 and N*2 <= 1000000:
            q.append((N*2, cnt+1))
        if 0 < N-10 and N-10 <= 1000000:
            q.append((N-10, cnt+1))
        if 0 < N+1 and N+1 <= 1000000:
            q.append((N+1, cnt+1))
        if 0 < N-1 and N-1 <= 1000000:
            q.append((N-1, cnt+1))
    print(F"#{test} {ans}")
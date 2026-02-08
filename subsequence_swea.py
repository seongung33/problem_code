T= int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    q = 0
    c = 0
    lst = []
    for i in range(M): # B
        b = B[i]
        for j in range(q, N): # A
            if b == A[j]:
                c = j
                lst.append(A[j])
                # print(lst)
                break
        q = c + 1
    if lst == B:
        print(f"#{test} YES")
    else:
        print(f"#{test} NO")



T= int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    b_idx = 0
    for i in range(N):
        if A[i] == B[b_idx]:
            b_idx += 1
        if b_idx == M:
            break
    if b_idx == M:
        print(f"#{test} YES")
    else:
        print(f"#{test} NO")
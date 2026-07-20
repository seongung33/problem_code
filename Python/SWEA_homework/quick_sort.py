def quick_sort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)
def partition(A, l, r):
    p = A[l]
    i = l
    j = r

    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j

T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, N-1)
    print(F"#{test} {lst[N//2]}")
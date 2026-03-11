A = list(map(int, input().split()))

def merge_sort(l, r):

    if l == r - 1:
        return l, r
    mid = (l+r)//2
    left_s, left_e = merge_sort(l, mid)
    right_s, right_e = merge_sort(mid, r)

    merge(left_s, left_e, right_s, right_e)
    return l, r

def merge(left_s, left_e, right_s, right_e):
    N = right_e - left_s
    result = [0]*N
    l = left_s
    r = right_s
    idx = 0

    while l < left_e and r < right_e:
        if A[l] <A[r]:
            result[idx] = A[l]
            idx += 1
            l += 1
        else:
            result[idx] = A[r]
            idx += 1
            r += 1
    while l < left_e:
        result[idx] = A[l]
        l += 1
        idx += 1
    while r < right_e:
        result[idx] = A[r]
        r += 1 
        idx += 1

    for i in range(N):
        A[i+left_s] = result[i]
merge_sort(0, len(A)-1)
print(A[500000])
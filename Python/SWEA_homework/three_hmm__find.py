T = int(input())

def binary_search(N):
    start = 0
    end = N

    while start <= end:
        mid = (start + end) // 2
        val = mid** 3

        # x^3 = N 일때의 x를 찾아야 함
        # x = mid 이고 val = x^3
        # 즉 val = N인 경우를 찾는다.
        # 값의 이동은 x의 값이어야 하므로
        # mid로 이동한다.
        if val == N:
            return mid
        elif val < N:
            start = mid+1
        else:
            end = mid - 1
    return -1
for test in range(1, T+1):
    N = int(input())
    ans = binary_search(N)
    print(F"#{test} {ans}")
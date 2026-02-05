# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if lst[j] >= lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     print(f"#{test_case}", *lst)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    def counting_sort(arr, n, k):
        count = [0]* (k+1)
        sort_arr = [0]*(n)
        for i in range(n):
            count[arr[i]] += 1
        for i in range(1, k+1):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            count[arr[i]] -= 1
            sort_arr[count[arr[i]]] = arr[i]
        return sort_arr
    print(f"#{test_case}", *counting_sort(lst, N, max(lst)))


# 선택 정렬
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
    print(f"#{test_case}", *lst)
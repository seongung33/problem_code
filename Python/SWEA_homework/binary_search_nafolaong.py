"""
이진 탐색
각 구간을 쪼개는 것은 문제에서 주어준다.
왼-오-왼-오 순으로 탐색해야 한다.
오-왼-오-왼 순으로 탐색해야 한다.
위 두 조건을 만족하는 값의 개수를 구하면 된다.
1. 함수로 이진탐색을 구현한다.
내부에서 왼쪽과 오른쪽을 번갈아 탐색하는지 확인하는 장치를 설정한다.

어떤 장치인가??
while문 안에서 갱신하는 내용
mid 그리고 값의 크기에 따라 mid = end or mid = start
이전에 end로 바꾸었다면 start로 바꿔야 한다.
moniter = 0 설정 후
moniter = (moniter + 1) % 2
0 1 0 1 무한 스위칭 된다.
첫 지점을 기록하고 그걸로 0 1 설정 후 무조건 변경되고 해당 방향으로 가게 설정
0: 왼쪽
1: 오른쪽

구현 못 하겠다. True False로 출입문 여닫기 변경


퀵 정렬 써봤는데 N이 너무 커서 재귀호출 깊이 에러가 뜬다.
sort를 써야 한다네요
"""



T = int(input())

# 정렬한 상태로 준다는 줄 알았는데
# 정렬을 해야 한다고 한다...
# def quick_sort(A, l, r):
#     if l < r:
#         p = partition(A, l, r)
#         quick_sort(A, l, p-1)
#         quick_sort(A, p+1, r)
#
# def partition(A, l, r):
#     p = A[l]
#     i = l
#     j = r
#
#     while i <= j:
#         while i <= j and A[i] <= p:
#             i += 1
#         while i <= j and A[j] >= p:
#             j -= 1
#         if i < j:
#             A[i], A[j] = A[j], A[i]
#     A[l], A[j] = A[j], A[l]
#     return j
#이진탐색 구현
def binary_search(target):
    global cnt
    start = 0
    end = N-1
    left = right = False # False면 지나간다.
    # 왼쪽 통과시 오른쪽을 가야하므로 왼 True 오른쪽 False
    # 처음엔 둘다 지나갈 수 있으므로 둘 다 False
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            cnt += 1
            # print(A[mid], target)
            return
        elif A[mid] > target: # 왼쪽 탐색
            # 직전에 오른쪽을 통과했다면 left == False로 통과된다.
            if not left:
                left = True
                right = False
                end = mid - 1
            else:
                # print(right, left, target, '타겟이 작음')
                return
        elif A[mid] < target:
            # 직전에 왼쪽을 통과 했다면 right == False로 통과된다.
            if not right:
                right = True
                left = False
                start = mid + 1
            else:
                # print(right, left, target, '타겟이 큼')
                return


for test in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    # quick_sort(A, 0, N-1)
    # print(A)
    A.sort()
    for i in range(M):
        binary_search(B[i])
    print(f"#{test} {cnt}")

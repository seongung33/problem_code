"""
국어가 너무 어렵다. 문제 이해 하는데 30분은 넘게 쓴 듯 하다.
N//2 번째 원소
오른쪽 원소가 먼저 복사되는 경우의 수
위 두개를 각각 출력하라는 것이었다 ㅠㅠ
멍청하게 아랫 조건의 반대 경우의 수 쓰라는줄..
"""


# 병합정렬
def merge_sort(arr, N):
    # 길이가 1이면 종료
    if len(arr) == 1:
        return arr
    # 왼쪽 오른쪽 절반
    # 문제에서 요구하는대로 잘라야 함
    left_arr = merge_sort(arr[0:N//2], len(arr[0:N//2]))
    right_arr = merge_sort(arr[N//2:N], len(arr[N//2:N]))

    # 병합하기
    # 자연스럽게 병합하는 과정에서 두 집합이 합쳐진다.
    ans = merge(left_arr, right_arr)
    return ans

# 병합
def merge(left, right):
    # 정답 도출
    global cnt
    # 인덱스 시작 위치 설정
    l = 0
    r = 0
    # 정렬 저장
    result = [0]*(len(left)+ len(right))
    # 문제에서 요구하는 정답
    if left[-1] > right[-1]:
        cnt += 1

    # result에 넣기
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    # 위 반복문에서 다 못 넣으면 따로 넣어줘야 한다.
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 위 반복문과 아래 중 하나만 실행되지 않을까?
    while r < len(right):
        result[l + r] = right[r]
        r += 1
    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(mat, N)
    print(F"#{test} {ans[N//2]} {cnt}")
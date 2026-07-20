T = int(input())

def dfs(cnt, now):
    global min_cnt

    # 마지막 정류장 도착시, 인덱스니까 계산
    if now == N-1:
        # 마지막 도착시에는 배터리 교체 X
        # 하지만 재귀 구조상 배터리수 무조건 + 1 하므로 - 1
        min_cnt = min(cnt-1, min_cnt)
        return

    # 백트레킹
    if cnt-1 >= min_cnt:
        return
    # 인덱스 에러 방지 및 마지막 정류장을 넘어서니 취소
    if now >= N:
        return

    # 현재 정류장의 배터리 값
    k = lst[now]
    # 현재 정류장 +1, 현재 정류장 + 배터리 까지 갈 수 있다.
    for i in range(now+k, now, -1):
        dfs(cnt + 1, i)

for test in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    min_cnt = float("inf")
    dfs(0, 0)
    print(F"#{test} {min_cnt}")
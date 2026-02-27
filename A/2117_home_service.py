# 비용 계산 함수
def charge(k):
    return ((k*k) + (k-1)*(k-1))


# 해당 지점에서의 최대방문 수 계산
def house_cnt(y, x):
    max_cnt = 0
    # k의 범위 모두 계산
    for k in range(N+1):

        # 가지치기 느낌으로 써봤는데 속도 비슷하네요
        if (2*(k+1)**2)*M < charge(k+1):
            return max_cnt
        

        cnt = 0
        # 완전탐색
        # k만큼 사각형 그려서 계산하니까 mat에서의 인덱스 위치 잡기가 안되서
        # 완전탐색으로 돌려서 비교했습니다.
        for i in range(N):
            for j in range(N):
                if abs(i-y) + abs(j-x) <= k:
                    if mat[i][j]:
                        cnt += 1
        # 손해를 보지 않으면 집 개수로 비교하기
        if cnt*M - charge(k+1) >= 0:
            max_cnt = max(max_cnt, cnt)
    return max_cnt



T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    #완전 탐색
    for y in range(N):
        for x in range(N):
            # 각 좌표별 값중 최댓값 선정
            max_cnt = house_cnt(y, x)
            ans = max(max_cnt, ans)
    print(F"#{test} {ans}")
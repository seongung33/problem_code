# 인덱스 범위 밖 제외
def in_range(y, x):
    return 0<= y < N and 0<= x < M

T = int(input())
for test in range(1, T+1):
    N, M =map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # 개수 출력
    max_cnt = 0

    # 완전탐색 시작
    for i in range(0, N):
        for j in range(0, M):
            # 중앙값 비교용
            center = A[i][j]
            cnt = 0
            # 중앙을 기준으로 3X3 탐색
            for y in range(i-1, i+2):
                for x in range(j-1, j+2):
                    # 인덱스를 벗어나지 않으며 중앙값보다 작은 지역의 개수 세기
                    if in_range(y, x) and center > A[y][x]:
                        cnt += 1
            # 그 개수가 4개가 넘으면 
            if cnt >= 4:
                #후보지 + 1
                max_cnt += 1
    print(F"#{test} {max_cnt}")
    
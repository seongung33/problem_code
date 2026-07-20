# 파리퇴치
T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]


    # 최댓값 저장
    max_s = 0
    # 완전 탐색
    # 범위 끝 값이 N-M +1 인 이유는 해당 위치부터 M,M 인덱스 만큼 이동하여 검사해야 하기 때문
    # 이렇게 계산하면 인덱스 범위를 벗어나지 않는다.
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리 퇴치
            s = 0
            # 인덱스 시작 지점 i, j를 왼쪽 위로 지정하여 계산한다.
            for x in range(M):
                for y in range(M):
                    ny =i + x
                    nx = j + y
                    s += matrix[ny][nx]
                    
            #최댓값 비교
            if max_s < s:
                max_s = s
    print(f"#{test} {max_s}")
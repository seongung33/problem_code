"""
컨테이너 N
트럭 M
컨테이너가 트럭의 무게를 넘으면 싣지 못한다.
트럭당 한개의 컨테이너
각 트럭이 가장 무거운 화물을 실으면 된다.

각 트럭이 가장 무겁지 않은 화물을 실었다면 이는 최대 무게가 아니다.

가장 적은 무게를 드는 트럭부터
자신이 들 수 있는 최대 무게의 화물을 싣는다.
"""

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    max_car = list(map(int, input().split()))

    max_car.sort()
    container.sort(reverse=True)

    # 화물의 합
    s = 0
    # 트럭 인덱스
    i = 0
    # 화물 인덱스
    j_c = 0
    # 트럭은 작은 값부터
    # 화물은 큰 값 부터 정렬
    # while 조건: 모든 트럭에 대해 검사하면 종료
    while  i != M:
        # 위처럼 정렬하여서 가장 작은 트럭이
        # 들 수 있는 최대 무게의 화물을 찾으면
        if max_car[i] >= container[j_c]:
            # 누적합
            s += container[j_c]
            # 해당 화물은 모든 트럭이 못 드는 무게인 100으로 변경
            # 제외하기
            # pop은 길이가 달라져 이렇게 처리함
            container[j_c] = 100
            # 다시 처음부터 탐색
            j_c = 0
        else:
            # 화물의 인덱스가 벗어나지 않으면
            # N-1에서 인덱스 찾고 여기 else문으로 들어오고 아래로 가야해서
            # N-1
            if j_c < N-1:
                # 인덱스 증가
                j_c += 1
                continue
        # 여길오면 화물을 실었거나
        # 실을수 있는 화물이 없다는 것이다.
        # 따라서 트럭 인덱스 +1
        i += 1
        # 화물 인덱스 초기화
        j_c = 0

    print(f"#{test} {s}")
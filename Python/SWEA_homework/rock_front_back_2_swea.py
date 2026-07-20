T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    ij = [map(int, input().split()) for _ in range(M)]
    cnt = 0
    # print(*lst)
    # ij 로 for 문을 돌아 바로 i, j값을 사용할 수 있도록 한다.
    for i, j in ij:
        # i값은 인덱스로 쓰이므로 -1 해준다.
        i -= 1
        # 아래 for 문은 큰 값 > 작은 값 으로 이동한다. 하지만 작은 값 > 큰 값 이동도 필요하므로 cnt를 지정한다.
        cnt = 0
        # 자기 자신을 제외한 양 옆 값들끼리 비교하므로 i-1로 시작한다.
        for k in range(i - 1, i - j-1, -1):
            cnt += 1
            # 범위를 벗어나면 중단한다.
            if 0 >k or i+cnt >= N:
                break
            # 같은 색이면 뒤집는다.
            #cnt를 통해 서로 중심 i로 부터 멀어지도록 설정했다.
            if lst[k] == lst[i+cnt]:
                # 1이면 0이되고 0이면 1이된다.
                lst[k] = 1 - lst[k]
                lst[i+cnt] = 1 - lst[i+cnt]
        # print(*lst)
            # 다른 색이면 그대로 둔다.

    print(f"#{test}", *lst)

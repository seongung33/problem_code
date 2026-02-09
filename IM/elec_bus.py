def elec_bus(K, N, M, num):
    num_idx = 0
    i = 0
    k = 0
    charge = 0

    while i < N:
        # 이동 불가시 
        if k == K + 1:
            return print(f"#{test}", 0)
        # 다음 충전소 갈 수 있는지 판단
        if num_idx + 1 < M:
            if num[num_idx] == i and num[num_idx + 1] - num[num_idx] <= K - k and k < K:
                i += 1
                k += 1
                num_idx += 1
                continue
            # 충전소에서 충전
        if num_idx < M and num[num_idx] == i:
            if N - i <= K- k:
                i += 1
                continue
            # print('good')
            num_idx += 1
            charge += 1
            k = 0
        i += 1
        k += 1
    return print(f'#{test} {charge}')
T = int(input()) # 노선 수
for test in range(1, T +1):
    # K : 이동가능 정류장
    # N : 정류장 수
    # M : 충전기 정류장 수
    K, N, M = map(int, input().split()) 
    num = list(map(int, input().split()))
    elec_bus(K, N, M, num)
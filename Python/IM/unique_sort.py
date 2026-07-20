T = int(input())
for test in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    # 인덱스가 짝수 > 큰 애들
    # 인덱스가 홀수 > 작은 애들
    for i in range(N-1):
        idx = i
        for j in range(i+1, N):
            if i % 2 == 0: #짝수인경우, 큰 값을 찾아야 한다.
                if num[idx] < num[j]:
                    idx = j

            if i % 2 == 1 and num[idx] > num[j]: # 홀수인 경우, 작은 값을 찾아야 한다.
                idx = j
        # 위치 변경
        num[idx], num[i] = num[i], num[idx]

    print(f"#{test}", *num[:10])


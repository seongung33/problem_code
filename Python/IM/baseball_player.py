T = int(input())
for test in range(1, T +1):
    N, K = map(int,input().split())
    player = list(map(int, input().split()))
    #야구선수 추가
    player.sort()
    max_cnt = 0
    # 모든 플레이어를 기준으로 순회한다.
    for i in range(N):
        cnt = 0
        lst = []
        # 한 플레이어를 모든 플레이어와 비교한다.
        for j in range(N):
            # 앞 뒤 간격을 2K 로 설정하였다.
            # 반드시 정렬이 필요한 구조
            if player[j] - K <= player[i] <= player[j] + K:
                cnt += 1
                lst.append(player[j])
                # print(i, j)
                # 만약 들어온 선수들의 차가 K 이상이면 브레이크
                if max(lst) - min(lst) > K:
                    break # for j
            # 브레이크가 안 되었을때만 비교 됨
            max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")
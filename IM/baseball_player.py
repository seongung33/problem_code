T = int(input())
for test in range(1, T +1):
    N, K = map(int,input().split())
    player = list(map(int, input().split()))
    #야구선수 추가
    player.sort()
    max_cnt = 0
    for i in range(N):
        cnt = 0
        lst = []
        for j in range(N):
            if player[j] - K <= player[i] <= player[j] + K:
                cnt += 1
                lst.append(player[j])
                # print(i, j)
                if max(lst) - min(lst) < K:
                    break # for j
            max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")
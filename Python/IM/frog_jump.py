<<<<<<< HEAD
T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    water_hole = list(map(int, input().split()))

    # 이동거리
    i = 0
    while True:
        i += K
        if i >= N:
            i = N-1
            break
        elif water_hole[i] == 1:
            continue

        elif sum(water_hole[i-K+1: i]) > 0:
            for j in range(i, i-K, -1):
                if water_hole[j] == 1:
                    i = j
                    # print(i)
                    break
        else:
            break
=======
T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    water_hole = list(map(int, input().split()))

    # 이동거리
    i = 0
    while True:
        i += K
        if i >= N:
            i = N-1
            break
        elif water_hole[i] == 1:
            continue

        elif sum(water_hole[i-K+1: i]) > 0:
            for j in range(i, i-K, -1):
                if water_hole[j] == 1:
                    i = j
                    # print(i)
                    break
        else:
            break
>>>>>>> e4a9be2b9954f3f739eb37006796a30bcc10ebca
    print(f"#{test} {i+1}")
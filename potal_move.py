T = int(input())
for test in range(1, T + 1):
    N = int(input())
    room_num = list(map(int, input().split()))
    i = 0
    idx = [0]*N
    cnt = 0
    while True:
        # 각 반복마다 이동하므로 cnt를 + 1 해준다
        # print(i)
        #도착시 정지
        if i == N - 1:
            break
        # 처음이면 무조건 한칸 전진
        elif i == 0:
            i += 1
            cnt += 1
            continue
        # 처음 간 방이면 해당 방 번호로 이동
        elif idx[i] == 0:
            idx[i] += 1
            cnt+= 1
            i = room_num[i] - 1
        # 위 상황이 모두 아니면 이미 간 방이므로 한칸 전진
        else:
            i += 1
            cnt += 1
    print(f"#{test} {cnt}")


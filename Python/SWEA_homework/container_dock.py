"""
종료시간이 가장 짧은 것들을 고른다.
해당 종료시간부터 시작이 가능하고 그 중에서 가장 가까운 종료시간인 것을 택한다.
"""
T = int(input())
for test in range(1, T+1):
    N = int(input())
    starts = [0]*N
    ends = [0]*N
    for i in range(N):
        start, end = map(int, input().split())
        starts[i] = start
        ends[i] = end

    cnt = 0
    time = 0
    while ends:
        # 종료시간이 가장 빠른 인덱스 찾기
        end_idx = ends.index(min(ends))

        # 작업종료 시간: time 다음 작업 시작 시간: starts
        # 다음 작업이 시작 가능하면 해당작업 실시
        if time <= starts[end_idx]:
            cnt += 1
            time = ends[end_idx]
            ends.pop(end_idx)
            starts.pop(end_idx)
        # 작업이 안되면 해당 작업 제외
        else:
            ends.pop(end_idx)
            starts.pop(end_idx)
        if time == 24:
            break

    print(F"#{test} {cnt}")
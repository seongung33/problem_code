"""
사람: 1
계단: 2
계단은 반드시 2개이다.

이 문제 무조건 시뮬일줄 알았는데
재귀로 어떻게 푼단 말인가...  

필요한 정보: 각 사람들이 두 계단에 도착하는 시간
두 리스트를 만들어서 인덱스 순으로 사람 번호를 매기고 도착하는 시간을 저장해둠
방문배열을 통해 계단에 내려간 사람을 표기함
계단에 사람이 들어갈 수 있으면 도착한 사람중 무작위로 내리고
방문표시를 통해 다른 계단으로 갈 수 없게 함
"""

T = int(input())

def stairs():
    for i in range(N):
        for j in range(N):
            if mat[i][j] not in (0, 1):
                stair.append((i, j, mat[i][j]))

def humans():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                human.append((i, j))

def move(y, x, i, j):
    time = abs(y-i) + abs(x-j)
    return time

def recur(stair_1_time, stair_2_time):
    global min_time
    # 모든 사람이 계단을 내려가면 종료
    if sum(visited) == len(human):
        max_t = max(stair_1_time, stair_2_time)
        print(stair_1_time, stair_2_time)
        min_time = min(min_time, max_t)
    # 사람이 계단을 내려가면 끝

    # 첫 번째 계단
    for i in range(len(human)):
        if not visited[i]:
            if stair_1_time < stair1[i]:
                stair_1_time = stair1[i]+1
            visited[i] = True
            recur(stair_1_time+ stair[0][2], stair_2_time)
            visited[i] = False

    # 두번째 계단
    for i in range(len(human)):
        if not visited[i]:
            if stair_2_time < stair2[i]:
                stair_2_time = stair2[i] + 1
            visited[i] = True
            recur(stair_1_time, stair_2_time + stair[1][2])
            visited[i] = False



for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    # 계단 위치
    stair = []
    stairs()
    print(stair)
    # 사람 위치
    human = []
    humans()
    # 계단 1
    stair1 = []
    for y, x in human:
        time = move(y, x, stair[0][0], stair[0][1])
        stair1.append(time)
    # 계단 2
    stair2 = []
    for y, x in human:
        time = move(y, x, stair[1][0], stair[1][1])
        stair2.append(time)

    visited = [False]*len(human)


    stair_1_time = 0
    stair_2_time = 0

    min_time = float('inf')

    recur(0, 0)
    print(min_time)


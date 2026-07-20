from collections import deque

T = int(input())
for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stair = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                person.append((i, j))
            elif mat[i][j] >= 2:
                stair.append((i, j, mat[i][j]))

    person_num = len(person)
    time = 0
    eating_lunch_cnt = 0
    person_to_stair = [[0,0] for _ in range(person_num)]
    for i in range(person_num):
        person_to_stair[i][0] =abs(person[i][0]-stair[0][0]) + abs(person[i][1] - stair[0][1])
        person_to_stair[i][1] =abs(person[i][0]-stair[1][0]) + abs(person[i][1] - stair[1][1])

    # print(person_to_stair)
    person_gone = [False] * person_num
    # 계단 사용 여부
    stair1 = [0]*3
    stair2 = [0]*3
    min_time = float('inf')

    visited = [False] *person_num
    ans = 0
    def dfs(cnt):
        global visited, min_time, ans, used, stair
        if cnt == person_num:
            # ans += 1
            eating_lunch_cnt = 0
            time = 0
            stair1 = [0]*3  #2, 2, 0
            stair2 = [0]*3  
            q_1 = deque()
            q_2 = deque()
            used = [False]*person_num

            while eating_lunch_cnt < person_num:
                # 계단 내려가기
                for i in range(3):
                    if stair1[i] > 0:
                        stair1[i] -= 1
                        if stair1[i] == 0:
                            eating_lunch_cnt += 1
                    if stair2[i] > 0:
                        stair2[i] -= 1
                        if stair2[i] == 0:
                            eating_lunch_cnt += 1
            # 1번 계단
                for j in range(person_num):
                    if person_to_stair[j][0] <= time and visited[j] and not used[j]:
                        q_1.append(person_to_stair[j][0]+1)
                        used[j] = True
                    if person_to_stair[j][1] <= time and not visited[j] and not used[j]:
                        q_2.append(person_to_stair[j][1]+1)
                        used[j] = True
                        
                for i in range(3):
                    if q_1 and q_1[0] <= time:
                        if not stair1[i] and q_1:
                            go_stair = q_1.popleft()
                            stair1[i] = stair[0][2]

                for i in range(3):
                    if q_2 and q_2[0] <= time:
                    # 2번 계단
                        if not stair2[i] and q_2:
                            go_stair = q_2.popleft()
                            stair2[i] = stair[1][2]

                time += 1

            min_time = min(min_time, time)
            return
        
        visited[cnt] = True
        dfs(cnt+1)
        visited[cnt] = False
        dfs(cnt+1)


    dfs(0)
    # print(subset)
    print(F"#{test} {min_time-1}")
    # print(ans)
    # print(person_num)
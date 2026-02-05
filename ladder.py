for test in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 2:
                goal_y = i
                goal_x = j
    goal_x = goal_x
    goal_y = goal_y

    # 동 북 서
    dx = [1, 0, -1]
    dy = [0, -1, 0]
    # 진행 방향
    d = 1

    def in_range(y, x):
        return 0 <= y < 100 and 0 <= x < 100
    while True:
        # 1. 앞으로 간다.
        # 2. 오른쪽 혹은 왼쪽으로 갈 수 있는지 확인한다.
        # 3. 갈 수 있다면 방향 전환을 한다.
        # 4. 왼쪽으로 갔다면 진행 후 오른쪽으로 갈 수 있는지 확인한다.
        # 5. 오른쪽으로 갔다면 진행 후 왼쪽으로 갈 수 있는지 확인한다.
        # 6. 세 방향 모두 진행 불가능 하다면 이는 사다리의 시작지점이다.

        # 전진
        ny = goal_y + dy[d]
        nx = goal_x + dx[d]

        #오른쪽, 혹은 왼쪽으로 갈 수 있다면
        if d == 1:
            for D in range(0,3,2):
                ny = goal_y + dy[D]
                nx = goal_x + dx[D]
                if in_range(ny, nx):
                    if matrix[ny][nx] == 1:
                        d = D
                        goal_y = ny
                        goal_x = nx
                        continue
        if d in (0, 2):
            ny = goal_y + dy[d]
            nx = goal_x + dx[d]
            if in_range(ny, nx):
                if matrix[ny][nx] == 1:
                    d = 1
                    goal_y = ny
                    goal_x = nx
                    continue
        if d == 1:
            ny = goal_y + dy[d]
            nx = goal_x + dx[d]
            if not in_range(ny, nx):
                goal_y = ny
                goal_x = nx
                break
        # goal_y = ny
        # goal_x = nx
    print(f"#{test} {goal_x}")




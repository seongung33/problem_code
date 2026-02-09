import sys
sys.stdin = open('input.txt', 'r')

for test in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if matrix[99][j] == 2:
            goal_x = j
    goal_x = goal_x
    goal_y = 99
    # 동 북 서
    dx = [1, 0, -1]
    dy = [0, -1, 0]
    # 진행 방향
    d = 1

    def in_range(y, x):
        return 0 <= y < 100 and 0 <= x < 100
    while goal_y != 0:
        # 1. 북쪽으로 향하면서
        # 2. 오른쪽 혹은 왼쪽으로 갈 수 있는지 확인한다.
        # 3. 갈 수 있다면 해당 방향으로 간다.
        # 4. 불가능 하다면 북쪽으로 간다.

        # 5. 오른쪽 혹은 왼쪽으로 이동 시
        # 6. 북쪽으로 갈 수 있는 지 확인한다.
        # 7. 가능하다면 북쪽으로 진행하고 불가능 하다면 오른쪽 혹은 왼쪽으로 진행한다.
        # 8. y값이 0이 되면 출발지점 도달이다.


        # 전진
        # ny = goal_y + dy[d]
        # nx = goal_x + dx[d]
        # goal_y = ny
        # goal_x = nx

        #전진중
        if d == 1:
            # 오른쪽, 혹은 왼쪽으로 갈 수 있다면
            # 오른쪽 혹은 왼쪽으로 이동한다.
            s = 0
            for D in 0, 2:
                ny = goal_y + dy[D]
                nx = goal_x + dx[D]
                if in_range(ny, nx):
                    if matrix[ny][nx] == 1:
                        d = D
                        goal_y = ny
                        goal_x = nx
                        s += 1
                        break
            # 좌우로 이동을 못했을 경우 전진한다.
            if s == 0:
                ny = goal_y + dy[d]
                nx = goal_x + dx[d]
                if in_range(ny, nx):
                    if matrix[ny][nx] == 1:
                        goal_y = ny
                        goal_x = nx
                        continue
        # 오른쪽 or 왼쪽으로 진행중 북 쪽으로 갈 수 있을 경우
        # 갈 수 있다면 북 쪽으로 간다.
        if d in (0, 2):
            ny = goal_y + dy[1]
            nx = goal_x + dx[1]
            if in_range(ny, nx):
                if matrix[ny][nx] == 1:
                    d = 1
                    goal_y = ny
                    goal_x = nx
                    continue
        #가지 못했을 경우
        # 오른쪽 혹은 왼쪽으로 진행한다.
                else:
                    ny = goal_y + dy[d]
                    nx = goal_x + dx[d]
                    if in_range(ny, nx):
                        if matrix[ny][nx] == 1:
                            goal_x = nx
                            goal_y = ny
                            continue
        # if d == 1:
        #     ny = goal_y + dy[d]
        #     nx = goal_x + dx[d]
        #     if not in_range(ny, nx):
        #         break
        # print(goal_y, goal_x)
        # goal_y = ny
        # goal_x = nx
    print(f"#{test} {goal_x}")
    # print(goal_y)




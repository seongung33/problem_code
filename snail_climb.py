for test in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 2:
                goal_y, goal_x = i, j
    # 동 북 서
    dx = [1, 0, -1]
    dy = [0, -1, 0]
    # 진행 방향
    d = 1
    dir = {
        'E':0,
        'U':1,
        'W':2,
    }
    while True:
        # 1. 앞으로 간다.
        # 2. 오른쪽 혹은 왼쪽으로 갈 수 있는지 확인한다.
        # 3. 갈 수 있다면 방향 전환을 한다.
        # 4. 왼쪽으로 갔다면 진행 후 오른쪽으로 갈 수 있는지 확인한다.
        # 5. 오른쪽으로 갔다면 진행 후 왼쪽으로 갈 수 있는지 확인한다.
        # 6. 세 방향 모두 진행 불가능 하다면 이는 사다리의 시작지점이다.
        ny = i + dy[d]
        nx = j + dx[d]



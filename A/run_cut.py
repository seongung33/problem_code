T = int(input())
for test in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]

    # 동 남 서 북
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    way = {
        # 동 남 서 북
        1:[4, dy, dx],
        # 남 북
        2:[2, dy[1:4:2], dx[1:4:2]],
        # 동 서
        3:[2, dy[0:4:2], dx[0:4:2]],
        # 동 북
        4:[2, dy[0:4:3], dx[0:4:3]],
        # 동 남
        5:[2, dy[0:2], dx[0:2]],
        # 남 서
        6:[2, dy[1:3], dx[1:3]],
        # 서 북
        7:[2, dx[2:4], dy[2:4]],
    }
    print(way)

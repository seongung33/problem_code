my_b = [list(map(int,input().split())) for _ in range(5)]
ans = [list(map(int,input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
cnt = 0
turn = 0
# 빙고 세줄 검사
def check_bing():
    bingo = 0
    #가로
    for i in range(5):
        if sum(visited[i]) == 5:
            bingo += 1
    #세로
    s = 0
    for i in range(5):
        s = 0
        for j in range(5):
            s += visited[j][i] 
            if s == 5:
                bingo += 1
    #대각
    s = 0
    for i in range(5):
        s += visited[i][i]
        if s == 5:
            bingo += 1
    # 반대 대각
    s = 0
    for i in range(5):
            s +=visited[i][5-i-1]
            if s == 5:
                bingo += 1
    return bingo
# 빙고시 체크하기
def bing():
    cnt = 0
    for i in range(5):
        for j in range(5):
            answer = ans[i][j]
            cnt += 1
            for y in range(5):
                for x in range(5):
                    if answer == my_b[y][x]:
                        visited[y][x] = 1
                    if check_bing() >= 3:
                        return cnt
wow = bing()
print(wow)

                    
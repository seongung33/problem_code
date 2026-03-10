"""
사람: 1
계단: 2
계단은 반드시 2개이다.

이 문제 무조건 시뮬일줄 알았는데
재귀로 어떻게 푼단 말인가...
"""

T = int(input())

def stairs():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                stair.append((i, j))

def humans():
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                human.append((i, j))

def move(y, x, i, j):
    time = abs(y-i) + abs(x-j)
    return time

def recur():



for test in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    # 계단 위치
    stair = []
    stairs

    # 사람 위치
    human = []
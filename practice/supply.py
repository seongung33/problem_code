# swea 1249 보급로

# 델타
dy = [1, 0]
dx = [0, 1]


# 인덱스 제한
def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


# dfs를 써보자
def dfs(i, j):
    for d in range(2):
        ny = i + dy[d]
        nx = j + dy[d]


T = int(input())
for test in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

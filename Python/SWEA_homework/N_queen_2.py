"""
깊이 : N
가짓수: N
"""

# 대각선 체크
def is_safe(row, col, queens):
    for r, c in queens:
        # 같은 열이거나, 대각선에 있으면 False
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def dfs(cnt, i, j):
    global ans
    # print(visited)
    if cnt == N:
        ans += 1
        return
    
    for k in range(N):
        v = is_safe(k, j, queens)
        if v and not visited[k]:
            # visited[k] = True
            queens.append((k, j))
            dfs(cnt +1,i, j+1)
            queens.pop()
            # visited[k] = False

T = int(input())
for test in range(1, T+1):
    N = int(input())
    # 세로 체크
    visited = [False]*N 
    ans = 0
    queens = []
    dfs(0, 0, 0)
    # print(visited)
    print(F"#{test} {ans}")

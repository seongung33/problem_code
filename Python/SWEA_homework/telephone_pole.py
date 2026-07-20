"""
시간복잡도 모두 비교하면
O(N^2)
제한시간: 2초, 6천만번
테케 15개
백만 X 15 = 1500만개 -> 가능

"""


T = int(input())

def dfs( prev):
    global cnt
    if prev == N:
        return

    for i in range(prev+1, N-1):
        if lst[i][0] > lst[i+1][0] and lst[i][1] < lst[i][1]:
            cnt += 1
            dfs(i)
            cnt -= 1
    return

for test in range(1, T+1):
    N = int(input())

    wires = []
    ans = 0

    for _ in range(N):
        start, end = map(int, input().split())

        for prev_start, prev_end in wires:
            if start > prev_start and end < prev_end:
                ans += 1
            elif start < prev_start and end > prev_end:
                ans += 1
        wires.append((start, end))

    print(F"#{test} {ans}")
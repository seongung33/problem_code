# 백준 2309번
lst = [int(input()) for _ in range(9)]

def subset(lst):
    for i in range(1 << 9):
        cnt = -1
        s = 0
        ans = [0]* 7
        for j in range(i):
            if i &( 1<<j ):
                cnt += 1
                # print(cnt)
                ans[cnt] = lst[j]
                s += lst[j]
                if cnt == 6 and s == 100:
                    return ans
                if cnt >= 6:
                    break

ans = subset(lst)
for i in range(7-1, 0, -1):
    for j in range(i):
        if ans[j] > ans[j+1]:
            ans[j], ans[j+1] = ans[j+1], ans[j]
print(*ans, sep = '\n')


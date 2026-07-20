Q = int(input())



N = 0
perfume_list = [-1]
keep_list = [False]


def preparation(num):
    global perfume_list, N, keep_list
    N = num.pop(0)
    N += 1
    perfume_list += num
    keep_list += [True]*(N - 1)
def plus(v):
    global N, keep_list
    perfume_list.append(v)
    keep_list += [True]
    N += 1

def abandon(i):
    global keep_list
    value = perfume_list[i]
    perfume_list[i] = -1
    keep_list[i] = False
    return value

def blending(k):
    min_cnt = float('inf')
    visited = [True]*N
    visited[0] = False
    def dfs(k, sumation, cnt, prev):
        nonlocal min_cnt
        if sumation == k:
            min_cnt = min(cnt, min_cnt)
        for i in range(prev+1, N):
            if visited[i] and keep_list[i]:
                visited[i] = False
                print(perfume_list[i])
                dfs(k, sumation + perfume_list[i], cnt+1, i)
                visited[i] = True
    dfs(k, 0, 0, 0)

    if min_cnt == float('inf'):
        min_cnt = -1
    return min_cnt

def note(k):
    cnt = 0
    for i in range(N):
        if keep_list[i]:
            for j in range(N):
                if keep_list[j]:
                    for k in range(N):
                        if keep_list[k]:
                            if perfume_list[i] + perfume_list[j] + perfume_list[k] >= k:
                                cnt += 1
    return cnt


dic = {
    1:preparation,
    2:plus,
    3:abandon,
    4:blending,
    5:note,
}


for i in range(Q):
    input_values = list(map(int, input().split()))
    num = input_values.pop(0)
    func = dic[num]
    if num == 4:
        func(*input_values)
    else:
        func(input_values)
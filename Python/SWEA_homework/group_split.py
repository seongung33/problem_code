T = int(input())

def find(x):
    if x != lst[x]:
        lst[x] = find(lst[x])
    return lst[x]

def union(x, y):
    king_x = find(x)
    king_y = find(y)

    
    if rank[king_x] > rank[king_y]:
        lst[king_y] = king_x
    else:
        lst[king_x] = king_y

        if rank[king_x] == rank[king_y]:
            rank[king_y] += 1





for test in range(1, T+1):
    N, M = map(int, input().split())

    lst = [i for i in range(N+1)]
    rank = [0]*(N+1)

    inp = list(map(int, input().split()))

    for  i in range(0, M* 2, 2):
        a = inp[i]
        b = inp[i+1]
        union(a, b)

    groups = set()
    for i in range(1, N+1):
        groups.add(find(i))

    print(F"#{test} {len(groups)}")

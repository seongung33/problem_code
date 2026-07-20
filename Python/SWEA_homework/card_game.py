# 재귀
def winner (a, b):
    # 무승부
    if lst[a] == lst[b]:
        return min(a, b)
    elif (lst[a] == 1 and lst[b] == 3) or (lst[a] == 2 and lst[b] == 1 ) or (lst[a] == 3 and lst[b] == 2):
        return a
    elif (lst[b] == 1 and lst[a] == 3) or (lst[b] == 2 and lst[a] == 1 ) or (lst[b] == 3 and lst[a] == 2):
        return b



def card(i, j):
    global winner
    if i == j:
        return i
        # print('why')
    else:     # if N % 2 == 0:
        a = card(i, (i + j)//2)
        b = card((i+j)//2 + 1, j)
        return winner(a, b)








T = int(input())
for test in range(1, T+1):
    N= int(input())
    lst = list(map(int,input().split()))
    
    # a = lst[0:N//2+1]
    # b = lst[N//2+1:N+1]
    ans = card(0, N-1)
    #인덱스 이므로 ans + 1
    print(f"#{test} {ans+1}")
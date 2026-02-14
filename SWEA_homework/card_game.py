# 재귀
def card(i, j):
    global winner
    if i == j:
        if lst[0] == lst[1]:
            winner = lst[0]
            return winner
        elif (lst[0] == 1 and lst[1] == 3) or (lst[0] == 2 and lst[1] == 1 ) or (lst[0] == 3 and lst[1] == 2):
            winner = lst[0]
            return winner
        elif (lst[1] == 1 and lst[0] == 3) or (lst[1] == 2 and lst[0] == 1 ) or (lst[1] == 3 and lst[0] == 2):
            winner = lst[1]
            return winner
    else:
        # print('why')
        # if N % 2 == 0:
        a = lst[i:(i+j)//2]
        b = lst[(i+j)//2 + 1:j]
        winner1 = card(i, (i+j)//2)
        winner2 = card((i+j)//2 + 1, j)
        print(winner1, winner2)
        if (winner1 == 1 and winner2 == 3) or (winner1 == 2 and winner2 == 1 ) or (winner1 == 3 and winner2 == 2):
            winner = winner1

        elif (winner2 == 1 and winner1 == 3) or (winner2 == 2 and winner1 == 1 ) or (winner2 == 3 and winner1 == 2):
            winner =winner2
        return winner








T = int(input())
for test in range(1, T+1):
    N= int(input())
    lst = list(map(int,input().split()))
    
    a = lst[0:N//2+1]
    b = lst[N//2+1:N+1]
    ans = card(0, N-1)
    print(f"#{test} {ans+1}")
# 재귀
def card():
    if 






T = int(input())
for test in range(1, T+1):
    N= int(input())
    lst = list(map(int,input().split()))
    
    a = lst[0:N//2+1]
    b = lst[N//2+1:N+1]
    print(len(a)+len(b))
T = int(input())
for test in range(1, T+1):
    N = int(input())
    names = set()
    for i in range(N):
        name = input()
        names.add(name)
    
    lst = list(names)
    lst.sort()
    lst.sort(key= lambda x:len(x))
    print(F"#{test}")
    for i in range(len(lst)):
        print(lst[i])
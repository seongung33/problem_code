lst = []
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if k == j or k == i:
                continue
            lst.append([str(i), str(j), str(k)])

N = int(input())
for _ in range(N):
    num, st, b = map(int, input().split())
    new_lst = []
    for pro in lst:

        strike = 0
        ball = 0

        for q in range(3):
            if str(num)[q] == pro[q]:
                strike += 1
            elif str(num)[q] in pro:
                ball += 1

        if st == strike and b == ball:
            new_lst.append(pro)

    lst = new_lst
print(len(lst))
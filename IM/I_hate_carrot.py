from collections import defaultdict

T = int(input())
for test in range(1, T+1):
    N= int(input())
    carrot = list(map(int, input().split()))
    dic = defaultdict(int)
    # 딕셔너리로 변환
    for i in range(N):
        dic[carrot[i]] += 1
    # print(dic)
    # 같은 값 별로 리스트로 묶어서 2차원 구조로 변경
    carrot_2 = [[key]*value for key, value in dic.items()]
    print(carrot_2)
    s_n = len(carrot_2)
    s = [0]*s_n
    s[0] = len(carrot_2[0])
    for i in range(1,s_n):
        s[i] = len(carrot_2[i]) + s[i-1]
    print(s)



    target1 = N//3
    target2 = N*2//3
    s = []
    m = []
    r = []

    for i in range(s_n):
        if target1 -1 >= i:
            s.append(len(carrot_2[i]))
        elif target2 >= i:
            m.append(len(carrot_2[i]))
        else:
            r.append(len(carrot_2[i]))


    print(s)
    print(m)
    print(r)
    # max_num = max(len(s), len(m), len(r))
    # min_num = min(len(s), len(m), len(r))
    # if s and m and r:
    #     print(F"#{test} {max_num-min_num}")


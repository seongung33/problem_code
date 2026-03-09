def max_prize(lst, cnt, max_money):
    # change 번 바꾸면 해당 값 비교
    if cnt == change:

        money = "".join(lst)
        if max_money < int(money):
            max_money = int(money)
        return max_money
    
    # 중복 안되는 set을 이용한 가지치기
    if ((cnt, "".join(lst))) in memo:
        return max_money

    memo.add((cnt, "".join(lst)))
    # 가지치기
    # 이따구로 하면 안될거 같긴한데 모르겠다
    # if cnt > 2 and N > 3:
    #     if lst[0] == lst_sort[0]:
    #         pass
    #     else:
    #         return max_money
    # # 가지치기 
    # # 누가봐도 개쓰레기처럼 했는데 ㅋㅋ;
    # if cnt > 3 and N > 3:
    #     if lst[1] == lst_sort[1]:
    #         pass
    #     else:
    #         return max_money


    # 모든 경우의 수를 탐색하는 반복문
    # 값이 좀만 커져도 시행횟수가 너무 많아
    # 가지치기가 필수다.
    # 근데 가지치기를 모르겠다.
    for i in range(N):
        for j in range(i+1, N):
            lst[i], lst[j] = lst[j], lst[i]
            max_money = max_prize(lst, cnt+1, max_money)
            lst[i], lst[j] = lst[j], lst[i]
    return max_money


T = int(input())
for test in range(1, T+1):
    info, change = map(int, input().split())
    info = str(info)
    N = len(info)
    lst = [i for i in info]
    lst_sort = sorted(lst, reverse=True)

    memo = set()

    max_money = max_prize(lst, 0, 0)
    print(F"#{test} {max_money}")
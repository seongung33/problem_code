T = int(input())
for test in range(1, T+1):
    N = int(input())
    # 문자열로 받은 이유는 해당 데이터가 split도 불가능하기 때문
    # 숫자로 바꾼다면 시퀀스를 사용할 수 없어 문자열로 받고 비교하는 것이 편하다.
    list = input()
    # 최대 1의 길이
    max_cnt = 0
    cnt = 0
    for i in list:
        # 문자열로 받아서 문자열과 비교
        if i =='1':
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    print(F"#{test} {max_cnt}")
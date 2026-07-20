T = int(input())
for test in range(1, T+1):
    N, hex = input().split()
    N = int(N)
    result = ""
    for i in range(N):
        # 10진수 변환
        deci = int(hex[i], 16)
        #0b 제거
        ans = bin(deci)[2:]
        # 길이 4로 맞추기 부족한 만큼 0 추가
        while len(ans) < 4:
            ans = '0' + ans
        # result에 입력
        result += ans

    print(F"#{test} {result}")
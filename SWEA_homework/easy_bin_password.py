# 변경
password = {
    "0001101":'0',
    "0110001":'5',
    "0011001":'1',
    "0101111":'6',
    "0010011":'2',
    "0111011":'7',
    "0111101":'3',
    "0110111":'8',
    "0100011":'4',
    "0001011":'9'
}
T = int(input())
for test in range(1,T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    # 7자리 비트 담기
    ans = [0]* 8
    # 비트 8개 담기 세기
    cnt = 7

    # lst 돌기
    for i in range(N):
        m= M - 1
        while m > -1:
            # 뒤에서 부터 순회하며 1 발견하면 시작
            if lst[i][m] == '1':
                code = ""
                # 7개의 비트 code에 저장
                for _ in range(7):
                    code = lst[i][m] + code
                    m -= 1
                # 7개의 비트 ans에 담기
                # 뒤에서 탐색했으니까 ans의 뒤에서부터 담는다
                ans[cnt] = code
                cnt -= 1
                m += 1
            m -= 1
        # 7개 다 담으면 종료
        if cnt == -1:
            break # for i

    # dictinary 이용해서 숫자로 변경
    for i in range(8):
        ans[i] = password[ans[i]]
    # print(ans)
    even = 0
    odd = 0

    # 문제 조건에 맞춰 계산
    for i in range(4):
        even += int(ans[2*i])
        odd += int(ans[2*i+1])
    # 나머지가 존재하면 암호가 틀렸다.

    if (even*3 + odd) % 10:
        print(F"#{test} 0")
    # 나머지가 없으면 10의 배수
    else:
        print(F"#{test} {even+odd}")

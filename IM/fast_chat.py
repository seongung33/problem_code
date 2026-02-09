T = int(input())
for test in range(1, T + 1):
    A, B = input().split()
    # A의 길이 - B와 일치하는 개수*B의 길이 + B와 일치하는 개수
    ans = 0
    # A 길이 - B의 길이 + 1 을 해야 아래 for 문에서 인덱스를 벗어나지 않음
    i = 0
    #abcabcabc abc 같은 경우 기존 for문 사용시 이를 하나로 파악하여 정답이 1이 된다.
    # 이를 방지하기 위해 while 문을 사용하였고 i의 값을 조정해준다.
    while i < len(A) - len(B) + 1:
        # 카운트의 개수를 초기화 해준다.
        cnt = 0
        for j in range(len(B)):
            # A의 인덱스도 함께 증가해야 문자를 비교시 다음 문자도 비교함
            if A[i+j] == B[j]:
                cnt += 1
                n = j
                # print(cnt)
        # 모든 문자열이 일치하면 cnt의 개수와 문자열의 길이가 일치해진다.
        if cnt == len(B):
            ans += 1
            # 일치하는 값이 나왔으므로 i의 값에 n을 더해 A의 인덱스 위치를 조정한다.
            i += n
        # print(i)
        i += 1

    # A와 B가 일치하는 개수도 더해줘야 한다.
    print(f"#{test} {len(A) - len(B)*ans + ans}")

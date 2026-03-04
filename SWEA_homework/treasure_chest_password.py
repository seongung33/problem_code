"""
문제에서 주어지진 않았지만 N//4 가 비밀번호로 입력될 수 있는 것들이다.
따라서 rotate 하면서 4방면의 값들을 중복 없이 저장한다.
중복 없는 자료구조: set 을 이용
한바퀴 회전하면서 4방면의 모든 값들을 저장하면 된다.
이는 사실 주어진 배열에서 모든 묶음을 만들어 내면 된다.
즉  N = 16일 경우 0~3, 1~4, ..., 12~15, 13~0, 14~1, 15~2 까지 구하면 되는 것이다.
회전을 한바퀴 다 돌린다 쳤을 때 한쪽 면 만 보고 해당 면에 있는 모든 값을 저장한다고 생각하면 될 것이다.
하지만 나는 문제에서 str로(수정 불가) 받아 직접 회전하지 않고 위에 적은대로 직접 찾아가는 방식이다.
"""

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    password = input()
    sett = set()
    # 끊을 단위 저장
    M= N // 4
    # 전체 반복
    for i in range(N):
        plus =""
        # 구간 별 M만큼 이동
        for j in range(i,i+M):
            # 마지막 부분일시 앞으로 이동
            if j >=N:
                # 인덱스 범위 초과 시 앞으로 이동
                # 원형 큐에도 사용한 식
                s = (j+N) % N
                plus += password[s]
            else:
                plus += password[j]
        # set의 append 버전
        sett.add(plus)

    # 인덱스를 사용하기 위해 list 변환
    lst = list(sett)
    # 16진수를 10진수로 변경
    # 중복되는 경우가 있을 경우 N의 값보다 작으므로 len(lst)를 사용해야 한다.
    for i in range(len(lst)):
        lst[i] = int(lst[i], 16)
    # 내림차순 정렬
    lst.sort(reverse= True)
    print(F"#{test} {lst[K-1]}")
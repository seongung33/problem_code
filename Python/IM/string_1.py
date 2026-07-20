T = int(input())
for test in range(1, T +1):
    s1 = input()
    s2 = input()

    s1_count = [0]* 26
    for c in s1:
        s1_count[ord(c) - 65] = 1

    s2_count = [0] * 26
    max_count = 0
    # s2로 반복문
    for s in s2:
        # s2의 문자가 s1에 존재할시 s2_count + 1
        if s1_count[(ord(s) - 65)] == 1:
            s2_count[(ord(s) - 65)] += 1
        # 방금 추가한 문자의 개수가 가장 많다면 최댓값 변경
        if max_count <= s2_count[(ord(s) - 65)]:
            max_count = s2_count[(ord(s) - 65)]

    print(f"#{test} {max_count}")
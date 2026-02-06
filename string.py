T = int(input())
for test in range(1, T +1):
    s1 = input()
    s2 = input()

    s1_count = [0]* 26

    for c in s1:
        s1_count[ord(c) - 65] = 1

    s2_count = [0] * 26
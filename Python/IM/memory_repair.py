T = int(input())
for test in range(1, T+1):
    memory = input()
    N = len(memory)
    base = ['0']*N

    cnt = 0
    for i in range(N):
        if memory[i] != base[i]:
            cnt += 1
            for j in range(i, N):
                if base[j] == '1':
                    base[j] = '0'
                else:
                    base[j] = '1'
                print(base)
    print(F"#{test} {cnt}")

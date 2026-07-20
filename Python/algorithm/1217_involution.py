def involution(N, a, answer):
    if M < a:
        return answer
    answer = involution(N, a+1, N*answer)
    return answer
for i in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())

    answer = involution(N, 1, 1)
    print(F"#{T} {answer}")
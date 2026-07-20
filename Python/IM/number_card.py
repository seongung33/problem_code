#16191. 1일차 - 숫자카드
#swea 2일차 문제
T = int(input())
for test_cases in range(1, T+1):
    N = int(input())
    a = int(input())
    num = [0]*(10)
    for i in range(N):
        num[a % 10] += 1
        a //= 10
    # print(num)
    max_num = num[0]
    num_idx = 0
    for i in range(10):
        if num[i] >= max_num:
            max_num = num[i]
            num_idx = i
    print(f"#{test_cases} {num_idx} {max_num}")
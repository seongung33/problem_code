import copy
# T = int(input())
# for test in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = list(range(1, 13))
#     new_arr = []
#     for i in range(1 << 12):
#         for j in range(12):
#             if i & (i << j):
#                 arr[j]
#
#         print()

T = int(input())
for test in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    binary = [0]*12
    count = []
    answer = 0
    while True:
        for i in range(1<<12):
            # print(binary)
            if sum(binary) == N:
                count.append(copy.deepcopy(binary))

            if binary[i] == 1:
                binary[i] = 0
            elif binary[i] == 0:
                binary[i] = 1
                break

        if sum(binary) == 12:
            # print(binary)
            break
    # print(count)
    unique = []
    for i in count:
        if i not in unique:
            unique.append(i)
    # print(len(unique))
    # print(unique)
    for i in range(len(unique)):
        s = 0
        for j in range(12):
            if unique[i][j] == 1:
                s += j + 1
                # print(s)
        if s == K:
            # print(unique[i])
            answer += 1
    print(f"#{test} {answer}")
N, M = map(int, input().split())
num = list(map(int, input().split()))
max_sum = 0
# 비트를 이용한 부분집합 탐색
#시간 초과..
# for  i in range(1 << N):
#     lst = [0] * 3
#     cnt = 0
#     s = 0
#     for j in range(N):
#         if i & (1 << j):
#             cnt += 1
#             # print(num[j], end = ' ')
#             if cnt > 3:
#                 break
#             s += num[j]


#     if max_sum < s and s <= M and cnt == 3:
#         max_sum = s
#         # print(max_sum)
#     # print()
# print(max_sum)

# 그냥 세개 검색
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 만족하는 조건중 가장 큰 값을 최댓값 지정
            if max_sum < num[i]+num[j]+num[k] and num[i]+num[j]+num[k] <= M:
                max_sum = num[i]+num[j]+num[k]
print(max_sum)
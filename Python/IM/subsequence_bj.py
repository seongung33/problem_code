# 백준 6550 이거 테스트 케이스 수 정해진게 아니라 오류코드 뜨면 while문 정지하는 식으로 해야함
# while True:
#     try:
#         s, t = input().split()

#         answer = 'No'
#         j = 0
#         for i in range(len(t)):
#             if t[i] == s[j]:
#                 j += 1

#             if j == len(s):
#                 answer = "Yes"
#                 break
#     except:
#         break
#     print(answer)

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    A = input()
    B = input()
    answer = 'NO'
    j = 0
    for i in range(len(A)):
        if A[i] == B[j]:
            j += 1
        if j == len(B):
            answer = 'YES'
            break
    print(f"#{test} {answer}")
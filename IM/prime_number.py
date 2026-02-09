# 백준 소수찾기 1978
N = int(input())
lst = map(int, input().split())
cnt = 0
for i in lst:
    # list 순회하며 소수이면 cnt + 1
    # 그렇다면 소수를 어떻게 판별할 것인가?
    if i == 1:
        cnt += - 1
    # 1. 모든 수로 나누어 본다.
    # 2 이상으로 나누었을 때 항상 나머지가 있어야 한다.
    for j in range(2, i):
        # i % j 일 때 나머지가 있으면 1 이상이므로 True 이다.
        # not을 사용하여 나머지가 없으면 break 가 된다.
        if not i % j: # 나머지가 없으면
            break
    # for -else 문: for문이 정상 작동하면 else 문이 작동한다.
    #나머지가 없을 경우 break를 하므로 else가 작동하지 않는다.
    else: # for문이 전부 반복되면 cnt + 1
        cnt += 1
print(cnt)

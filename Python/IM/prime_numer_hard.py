#백준 소수 2581


M = int(input())
N = int(input())

def prime_sum(M, N):
    s = 0
    min_num = float('inf') # 무한. 최솟값 비교이므로 가능한 가장 큰 값으로 설정
    # 문제 에서 최댓값은 10,000 이므로 10,000 으로 대체해도 무방
    for i in range(M, N + 1):
        # list 순회하며 소수이면 cnt + 1
        # 그렇다면 소수를 어떻게 판별할 것인가?
        if i == 1: # 1은 소수가 아니므로 continue를 통해 바로 다음수로 이동
            continue
        # 1. 모든 수로 나누어 본다.
        # 2 이상으로 나누었을 때 항상 나머지가 있어야 한다.
        for j in range(2, i):
            # i % j 일 때 나머지가 있으면 1 이상이므로 True 이다.
            # not을 사용하여 나머지가 없으면 break 가 된다.
            if not i % j: # 나머지가 없으면
                break
        # for -else 문: for문이 정상 작동하면 else 문이 작동한다.
        #나머지가 없을 경우 break를 하므로 else가 작동하지 않는다.
        else: # for문이 전부 반복되면 누적합
            s += i
            if min_num > i: # 최솟값 비교
                min_num = i
    if s > 0:
        print(s) # 함수로 만들어서 return을 하니 튜플로 반환되고 이어져서 나옴.
        print(min_num) # return으로 해도 두줄 출력 되는 방법이 있을까?
    else:
        print(-1)
    
prime_sum(M, N) # 함수 자체에서 출력하니 print문 x
# return을 썼다면 print(함수) 해야함
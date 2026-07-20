T = int(input())

def subset_sum(idx, prev, cnt, s):
    # 종료조건
    if idx == N:
        # 부분집합의 합이 K와 같아야 한다.
        if s == K:
            cnt += 1
        return cnt
    
    # 가지치기
    if s >= K:
        return cnt
    
    # 1부터 12까지 중 하나 선택
    # prev를 통하여 이전 값 선택 x
    for i in range(prev+1, 13):
        cnt = subset_sum(idx +1, i, cnt, s+i)
    return cnt

for test in range(1, T+1):
    N, K = map(int, input().split())


    print(F"#{test} {subset_sum(0, 0, 0, 0)}")
# 인덱스 범위 제한
def in_range(y, x):
    return 0<= y < N and 0<= x < N


T= int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    cnt = 0
    # 가로 개수 세기
    for i in range(N):
        valid = True
        for j in range(N-K+1):
            if matrix[i][j] == 1:

                for d in range(K):
                    if matrix[i][j+d] != 1:
                        break
                else:
                    cnt += 1
                    if  in_range(i, j+K) and matrix[i][j+K] == 1:
                        cnt -= 1
                    elif in_range(i, j-1) and matrix[i][j-1] == 1:
                        cnt -= 1


         
    for i in range(N-K+1):
        valid = True
        for j in range(N):
            if matrix[i][j] == 1:

                for d in range(K):
                    if matrix[j+d][i] != 1:
                        break
                else:
                    cnt += 1
                    if  in_range(j+K,i) and matrix[j+K][i] == 1:
                        cnt -= 1
                    elif in_range(j-1, i) and matrix[j-1][i] == 1:
                        cnt -= 1
    print(F"#{test} {cnt}")
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


    # print(cnt)
    #세로 세기
    for i in range(N):
        # 인덱스 범위 제한으로 k칸 검색
        for j in range(N-K+1):
            if matrix[j][i] == 1:

                for d in range(K):
                    if matrix[j+d][i] != 1:
                        break
                else:
                    # K칸 만큼 1이면 1 추가
                    cnt += 1
                    # 하지만 선택한 길이보다 더 길다면 다시 -1을 하여 해당 위치는 
                    # 불가능한 자리로 판단
                    if  in_range(j+K,i) and matrix[j+K][i] == 1:
                        cnt -= 1
                    elif in_range(j-1, i) and matrix[j-1][i] == 1:
                        cnt -= 1
    print(F"#{test} {cnt}")
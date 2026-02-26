def in_range(y, x):
    return 0<= y < N and 0<= x < N


T = int(input())
for test in range(1, T+1):
    N, X = map(int, input().split())
    airstrip = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 가로 탐색
    for i in range(N):
        costruction = [True]*N
        valid = True
        #왼쪽 검사
        for j in range(N-1):
            diff = airstrip[i][j] - airstrip[i][j + 1]
            if diff == 0:
                continue
                # j가 더 높음  j > j + 1
            elif diff == 1:
                for k in range(j+1, j+1+X):
                    if k == j + X and costruction[k] and k+1 == N -1:
                        costruction[k] = False
                    else:
                        valid = False
                        break    
                    if costruction[k] and airstrip[i][k] == airstrip[i][k+1]:
                        costruction[k] = False
                    else:
                        valid= False
                        break

            # j 가 더 낮음 j < j + 1
            elif diff == -1:
                # print(i, j, '오른쪽')
                for k in range(j, j-X, -1):
                    if k == j - X+1 and costruction[k] and k == 0:
                        costruction[k] = False
                        
                    elif costruction[k] and airstrip[i][k] == airstrip[i][k-1]:
                        costruction[k] = False
                    else:
                        valid = False
                        break
            else:
                valid = False
                break
        if valid:
            # print(i, '가로')
            cnt += 1





    # 세로 탐색 해야함
    for i in range(N):
        num = airstrip[0][i]
        costruction = [True]*N
        valid = True
        # 위에 활주로 깔기
        for j in range(1, N):
            if num + 1 ==airstrip[j][i]:
                # print(i, j, '왼쪽')
                num = airstrip[j][i]
                for k in range(j-1, j-X-1, -1):
                    # num과 길이가 같아야 하는 조건 추가
                    if in_range(k, i) and costruction[k] and airstrip[k][i] == airstrip[k+1][i]:
                        costruction[k] = False
                    else:
                        valid = False
                        # print(i, valid)
                        break # for k
            # 아래 다리 깔기
            elif num == airstrip[j][i] + 1:
                num = airstrip[j][i]
                # print(i, j, '오른쪽')
                for k in range(j+1, j+X):
                    # num과 길이가 같아야 하는 조건 추가
                    if in_range(k, i) and costruction[k] and airstrip[k][i] == airstrip[k-1][i]:
                        costruction[k] = False
                    else:
                        valid = False
                        # print(i, valid)
                        break # for k
            elif abs(num - airstrip[j][i]) >= 2:
                num = airstrip[j][i]
                valid = False
                break
            if not valid:
                break # for j
        if valid:
            # print(i)
            cnt += 1
    print(F"#{test} {cnt}")

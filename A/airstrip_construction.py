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
                for k in range(j+1, j+X+1):
                    ans = airstrip[i][j+1]
                    if not in_range(i, k):
                        valid = False
                        break
                    if ans == airstrip[i][k] and costruction[k]:
                        costruction[k] = False
                    else:
                        valid = False
                        break # for k
                    
            # j 가 더 낮음 j < j + 1
            elif diff == -1:
                # print(i, j, '오른쪽')
                for k in range(j, j-X, -1):
                    ans = airstrip[i][j]
                    if not in_range(i, k):
                        valid = False
                        break
                    if ans == airstrip[i][k] and costruction[k]:
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
        costruction = [True]*N
        valid = True
        #왼쪽 검사
        for j in range(N-1):
            diff = airstrip[j][i] - airstrip[j+1][i]
            if diff == 0:
                continue
                # j가 더 높음  j > j + 1
            elif diff == 1:
                for k in range(j+1, j+X+1):
                    ans = airstrip[j+1][i]
                    if not in_range(k, i):
                        valid = False
                        break
                    if ans == airstrip[k][i] and costruction[k]:
                        costruction[k] = False
                    else:
                        valid = False
                        break # for k
                    
            # j 가 더 낮음 j < j + 1
            elif diff == -1:
                # print(i, j, '오른쪽')
                for k in range(j, j-X, -1):
                    ans = airstrip[j][i]
                    if not in_range(k, i):
                        valid = False
                        break
                    if ans == airstrip[k][i] and costruction[k]:
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
    print(F"#{test} {cnt}")



'''
1
6 2
3 3 3 2 1 1
3 3 3 2 2 1
3 3 3 3 3 2
2 2 3 2 2 2
2 2 3 2 2 2
2 2 2 2 2 2
'''
'''
1
6 4
3 2 2 2 1 2
3 2 2 2 1 2
3 3 3 3 2 2
3 3 3 3 2 2
3 2 2 2 2 2
3 2 2 2 2 2
'''
T = int(input())
for test in range(1, T +1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    answer = ''
    for i in range(N):

        for j in range(N-M+1):
            # 가로 검색
            for k in range(M // 2):
                if matrix[i][j+k] != matrix[i][j+M-k-1]:
                        break
            else:
                answer = matrix[i][j:j+M]
            # 세로 검색
            for k in range(M//2):
                if matrix[j+k][i] != matrix[j+M-k-1][i]:
                    break
            else:
                for q in range(j, M+j):
                    answer = answer + matrix[q][i]

    print(f"#{test} {answer}")

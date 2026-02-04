T = int(input())
for test in range(1, T+ 1):
    n = int(input())
    color = [list(map(int,input().split())) for _ in range(n)]
    matrix = [[0]*10 for _ in range(10)]
    count1 = 0
    for col in color:
            for i in range(col[0], col[2]+1):
                for j in range(col[1], col[3]+1):
                     matrix[i][j] += col[4]
    # print(matrix)
    for i in  range(10):
         for j in range(10):
              if matrix[i][j] == 3:
                   count1 += 1
    print(f"#{test} {count1}")
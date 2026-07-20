import sys
sys.stdin = open('SUM_input.txt', 'r')
for test in range(1, 11):
    test_num = int(input())
    matrix = [list(map(int, input().split()))for _ in range(100)]
    # print(matrix[0][0])
    diag = 0
    diag_trans = 0
    row_sum_max = 0
    col_sum_max = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            if i == j:
                diag += matrix[i][i]
            if i == 99 - j:
                diag_trans += matrix[i][j]
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum_max < row_sum:
            row_sum_max = row_sum

        if col_sum_max < col_sum:
            col_sum_max = col_sum
    sum_max = max(col_sum_max, row_sum_max, diag, diag_trans)
    print(f"#{test_num} {sum_max}")
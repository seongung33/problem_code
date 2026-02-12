# 백준 2669
matrix = [[0]*100 for _ in range(100)]

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(a[0], a[2]):
    for j in range(a[1], a[3]):
        matrix[i][j] = 1
        
for i in range(b[0], b[2]):
    for j in range(b[1], b[3]):
        matrix[i][j] = 1

for i in range(c[0], c[2]):
    for j in range(c[1], c[3]):
        matrix[i][j] = 1

for i in range(d[0], d[2]):
    for j in range(d[1], d[3]):
        matrix[i][j] = 1
s = 0
for i in range(100):
    for j in range(100):
        s += matrix[i][j]
print(s)
# print(matrix)
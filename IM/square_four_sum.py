<<<<<<< HEAD
from pprint import  pprint
matrix = [[0]*100 for _ in range(100)]
=======
# 백준 2669
matrix = [[0]*100 for _ in range(100)]

>>>>>>> ec395c10134aa1a19a19c855dea3b23571678fe2
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(a[0], a[2]):
<<<<<<< HEAD
    for j in range(a[2], a[1]):
        matrix[i][j] = 1
for i in range(b[0], b[2]):


    for j in range(b[2], b[1]):
        matrix[i][j] = 1
for i in range(c[0], c[2]):
    for j in range(c[2], c[1]):
        matrix[i][j] = 1
for i in range(d[0], d[2]):
    for j in range(d[2], d[1]):
=======
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
>>>>>>> ec395c10134aa1a19a19c855dea3b23571678fe2
        matrix[i][j] = 1
s = 0
for i in range(100):
    for j in range(100):
        s += matrix[i][j]
print(s)
<<<<<<< HEAD
print(matrix)
=======
# print(matrix)
>>>>>>> ec395c10134aa1a19a19c855dea3b23571678fe2

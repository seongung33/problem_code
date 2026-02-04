N = int(input())

square = 1 # 시작값
for i in range(1, N + 1):
    square *=  4
    # print(square)
side = square ** 0.5 
# print(type(side))  float
answer = (side +1)*(side+ 1)
print(int(answer))
# 1 > 4 > 16 > 64
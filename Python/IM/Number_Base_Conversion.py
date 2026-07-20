# 2745 진법 변환 BAEKJOON 
N, B = input().split()
dic = {}
B = int(B)
count = 10
# ord란? unicode 표준에서 정해놓은 문자에 따른 숫자 번호를 출력
#chr은 반대이다.
for i in range(0, 10):
    dic[str(i)] = i
for i in range(ord('A'), ord('Z') + 1): # 
    dic[chr(i)] = count # 문자가 필요하므로 해당 숫자를 chr을 통해 문자로 다시 변환한다.
    count += 1
decimal = 0 #10진법 값
for i in range(len(N)):
    decimal = dic[N[i]] + decimal*B
print(decimal)
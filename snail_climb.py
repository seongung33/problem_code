A, B, V = map(int, input().split())

start = 0
end = 1000000000 
#t = 0  문제점 찾기용
# 이진 탐색 이용
# 1시간 반 소요...
#지피티랑 대화 몇 번 했는데 할루시 개 당했습니다...
while True:
    # t += 1
    i = (start + end) // 2 #중간 값

    # V보다 큰 i의 최솟값을 찾는다.
    # A*i -B*(i-1) >= V  --> 낮에 도달 시 즉시 종료이므로 B 값에 -1을 해준다.
    if A*i -B*(i-1) >= V: # V보다 큰 i 를 찾는다.
        i -= 1 # i에 1을 빼고
        if A*i -B*(i-1) >= V: # 다시 계산해도 크다면 해당 i는 최솟값이 아니다.
            end = i  # 위에서 -1을 했으므로 해당 i를 end로 바꾼다.
            continue # 즉시 반복
        else: # 만약 첫 i만이 V보다 크다는 것을 만족하면 해당 i는 v보다 크거나 같은 최솟값이 된다.
            answer = i +1 #i에 1을 뺐으므로 더한다.
            break
    elif  A*i -B*(i-1) <= V: # 작은경우 시작 값을 키운다.
        start = i + 1
    # print(start, end, i)
print(answer)

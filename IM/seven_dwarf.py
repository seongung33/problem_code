# 백준 2309번
lst = [int(input()) for _ in range(9)]
# 부분집합 함수 생성
def subset(lst):
    #부분 집합 만들기
    for i in range(1 << 9):
        cnt = -1
        s = 0
        ans = [0]* 7
        for j in range(i):
            if i &( 1<<j ):
                # cnt를 통해 난쟁이가 7명임을 확인
                cnt += 1
                # print(cnt)
                # ans에 난쟁이의 키를 넣어둔다. 추후에 해당 난쟁이들의 키를 출력해야 하기 때문
                ans[cnt] = lst[j]
                # 난쟁이 키의 합 구하기
                s += lst[j]
                # 난쟁이가 7명이고 합이 100이면 합격
                if cnt == 6 and s == 100:
                    return ans
                # 7명 넘어가면 다음
                if cnt >= 6:
                    break

ans = subset(lst)
# 버블정렬 사용
for i in range(7-1, 0, -1):
    for j in range(i):
        if ans[j] > ans[j+1]:
            ans[j], ans[j+1] = ans[j+1], ans[j]
print(*ans, sep = '\n')


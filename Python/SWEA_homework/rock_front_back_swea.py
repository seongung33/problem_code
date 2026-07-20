T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    ij = [map(int, input().split()) for _ in range(M)]

    # i번째 에서 j의 개수만큼 i의 색으로 뒤집는다.
    #여기서 색은 숫자이다.
    # ij의 개수만큼 뒤집기를 시행하고 매번 주어진 i, j값이 변한다.


    # ij 리스트를 순회한다. i, j를 이용해 i 값과 j값을 분리하여 사용할 수 있도록 한다.
    #인덱스는 0부터 이므로 주어진 i 값에 -1을 하여 사용하여야 한다.
    for i, j in ij:
        # 동일한 색으로 뒤집어야 하므로 i번째 색을 저장해둔다.
        color = lst[i-1]
        # i부터 j까지 반복문을 통해 색을 바꾼다.
        for k in range(i - 1, i - 1 + j):

            # 만약 N의 길이보다 넘어가게 된다면 N까지만 색을 바꾸면 된다.
            # 인덱스 범위 에러가 뜨므로 넘어가게 된다면 break로 for문을 정지해주자
            if k >= N:
                break
            # i부터 j의 개수만큼 색을 바꾼다. 
            # i도 포함이므로 이를 계산해서 range 범위를 지정해주자.
            lst[k] = color
    
    print(f"#{test}", *lst)

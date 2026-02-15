T = int(input())
for test in range(1, T+1):
    N= int(input())
    carrot = list(map(int, input().split()))
    #정렬이 필요한 방식
    carrot.sort()

    # 같은 값은 한 상자이므로 구분이 가능한 위치 파악
    cut_point = []
    for i in range(1, N):
        if carrot[i] != carrot[i-1]:
            cut_point.append(i)
    # print(cut_point)
    cut_len = len(cut_point)
    # 만약 컷 구간이 0~1개 라면 
    # 세개에 나누어 담을 수 없다.
    if cut_len <2:
        # -1 출력
        print (F"#{test} -1")
        # 바로 다음 테스트로 넘어간다.
        continue #for test
    
    # 최솟값
    min_diff = float('inf')
    # 세 구간으로 컷 한다.
    # i < j 구조로 0:i, i:j, j:N 으로 세구간을 나눈다.
    for i in range(cut_len-1):
        for j in range(i+1, cut_len):
            s = carrot[0:cut_point[i]]
            m = carrot[cut_point[i]:cut_point[j]]
            r = carrot[cut_point[j]:N]
            # 최대 -최소 비교
            max_carrot = max(len(s), len(m), len(r))
            min_carrot = min(len(s), len(m), len(r))
            curr_min_diff = max_carrot - min_carrot
            # 가장 작은 값 저장
            if min_diff > curr_min_diff:
                min_diff = curr_min_diff

    print(F"#{test} {min_diff}")
        
    
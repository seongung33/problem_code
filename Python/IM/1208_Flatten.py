for test_case in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))

    # for i in range(dump):
    #     max_idx = height.index(max(height))
    #     height[max_idx] -= 1
    #     min_idx = height.index(min(height))
    #     height[min_idx] += 1
    # print(f"#{test_case}", max(height)- min(height))


    for i in range(dump):
        max_height = height[0]
        min_height = height[0]
        max_idx = 0
        min_idx = 0
        for i in range(len(height)):
            if max_height <= height[i]:
                max_height = height[i]
                max_idx = i
            if min_height >= height[i]:
                min_height = height[i]
                min_idx = i
        height[max_idx] -= 1
        height[min_idx] += 1
    print(f"#{test_case}", max(height)- min(height))
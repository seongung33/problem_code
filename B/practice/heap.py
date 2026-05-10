import heapq

# 입출력 속도를 높이기 위해 sys.stdin.readline 사용

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    max_heap = []
    results = []
    for _ in range(N):
        # 연산을 리스트로 받음 (1 x 또는 2)
        lst = list(map(int, input().split()))
        
        if lst[0] == 1:
            # 연산 1: 삽입 (최대 힙을 위해 -를 붙여 저장)
            heapq.heappush(max_heap, -lst[1])
        
        elif lst[0] == 2:
            # 연산 2: 최댓값 출력 후 삭제
            if not max_heap:
                results.append("-1")
            else:
                # 꺼낸 음수 값을 다시 양수로 변환
                val = -heapq.heappop(max_heap)
                results.append(val)
    
    # 결과 출력 예시: #1 5 3 1
    print(f"#{test}", *results)
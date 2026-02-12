# 재귀 함수 구현
# 기존의 최솟값의 합과 새로구한 최솟값의 합을 비교해야 한다.
def min_sum(i, j, N, s): #좌표 y, x, 길이, 현재 합
    # 종료 조건
    global ans
    # j == N일 경우 인덱스 기준 마지막 위치 +1 이므로 정지하고 값 출력
    # 값 비교 s는 이전 기준 합
    # 가지치기
    # 만약 현재까지 누적한 합이 현재 누적 최솟값 보다 크다면 계산을 하지 않고 백트래킹 한다.
    if ans < s:
        return
    if i == N and ans > s:
        ans = s
        return
    else:
    # if True:
        #가로 순회 중 제일 작은 값 선정.
        for k in range(N):
            # print(i, k, sumation)
            # 동일 열 중에 방문한 곳이 없어야 한다.
            if not visited[k]:
                # 방문 등록
                visited[k] = 1
                # 합 계산서에 저장
                sumation[k] = matrix[i][k]
                # 재귀를 통해 다음 행 진입
                # 합 계산
                s = sum(sumation)
                # 해당 합으로 다음 재귀에서 비교 및 아래 행으로 이동
                min_sum(i+1, 0, N, s)
                # 다시 나온다면
                # 방문 취소
                visited[k] = 0
                # 합 계산서 저장 취소
                sumation[k] = 0



T= int(input())
for test in range(1, T+1):
    N= int(input()) # 길이
    matrix = [list(map(int, input().split())) for _ in range(N)] # 매트리스 저장
    # 세로 별 최솟값 저장할 공간
    min_i = [0] * N


    # 최솟값 설정
    previous_sum = float('inf')
    # print(previous_sum)
    cnt = 0
    # 미리 변수 생성 및 비교할 최솟값 저장 위치
    ans = float('inf')
    # 현재 최솟값 저장 위치
    s = float('inf')
    # 방문
    visited = [0]*N
    # 합 저장 위치
    sumation = [0]*N


    min_sum(0, 0, N, s)
    print(f"#{test} {ans}")
"""
GPT를 통한 DP 깨닫기.
그리디로 풀다가 세달 처리 하는 것에서 벽 느끼고 GPT한테서 DP를 배웠습니다.
의사코드 조금 받아서 풀긴 했지만 DP를 깨달은 것 같아 상당히 행복한 문제였습니다.
값을 잘게 쪼개서 해당 값을 가지고 계산하는 방식
"""

T = int(input())
for test in range(1, T+1):
    day, month, three, year = map(int, input().split())
    lst = list(map(int, input().split()))
    # dp의 배열 생성 12월(index: 11) 계산시 세달 뒤 15월 까지 계산해야 해서 +3
    dp = [0] * (12+3)

    # dp 계산식입니다.
    # 진짜 이렇게 간단할수가;;
    # 12월부터 역으로 계산하여 1월로 갑니다.
    # 선정 방식은 간단합니다.
    # 현재 달 금액(month or day*lst[i]) + 이후의 달
    # 세 달 금액 + 세 달 이후 금액
    # 위 두 금액 중 최솟값을 골라 담는 문제
    # 문제에서 최소비용을 구하기 때문
    # 이렇게 값을 12월부터 1월까지 채워 넣으면 된다.
    for i in range(11, -1, -1):
        dp[i] = min(
            lst[i]*day + dp[i+1],
            month + dp[i+1],
            three + dp[i+3]
        )
    # 1월에는 자연스럽게 최소비용을 선택하여 저장된다.
    # year와 비교후 더 적은 비용을 고르면 된다.
    ans = min(dp[0], year)
    print(F"#{test} {ans}")
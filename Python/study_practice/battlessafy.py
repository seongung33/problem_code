"""
일반 포탄: 사거리 3 + 데미지 30
메가 포탄: 사거리 3 + 데미지 7-

1턴 당 행동: 방향 전환 + 이동 or 방향 전환 + 공격
"""

# 맵 크기 세로, 가로, 아군, 적군, 암호문 수
N, M, F, E, P =  input().split()

# 세로 N, 가로 M의 지도 생성
# 맵 정보 G: 풀, W: 물, S: 모래
# R: 바위, T: 나무
mat = [list(map(int, input().split())) for _ in range(N)]


F_info = [[] for _ in range(F)]
for i in range(F):
    # F_info[i][0] == M 이면 탱크 정보
    # M이면 체력, 방향, 일반 포탄 수, 메가 포탄 수
    #M, 100, R, 1, 0
    #M1 M2 등이면 다른 플레이어 체력 - 아군의 수인듯
    # M숫자면, 체력
    # M1, 100
    # H면 아군 포탑 체력
    info = list(input().split())
    F_info[i] = info

E_info = [[] for _ in range(E)]
for i in range(E):
    info = list(input().split())
    # E1 E2 등이면 적 플레이어 체력
    # E숫자면, 체력
    #E1, 10
    # X 면, 적 포탑의 체력
    # X, 10
    E_info[i] = info


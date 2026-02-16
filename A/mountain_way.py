'''
등산로 조성

최대한 긴 등산로 만들기 

숫자는 지형의 높이
1. 위에서 아래로 이동한다.
2. 가로 세로 연결
3. 최대 깊이 K만큼 딱 한 곳 깎을 수 있다.

dfs 를 사용해야 할 거 같다.
'''

# 시작지점 설정

def start():
    high = 0
    start_ij = [0]*5
    for i in range(N):
        for j in range(N):
            if high <= mat[i][j]:
                high = mat[i][j]
    cnt = -1
    for i in range(N):
        for j in range(N):
            if mat[i][j] == high:
                cnt +=1 
                start_ij[cnt] = [i, j]
    return start_ij

# 델타
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
# 바깥 탐색 금지
def in_range(y, x):
    return 0<=y < N and 0<= x < N
#dfs를 만들어보자
valid = True
# 등산로 개수 세기
cnt = 0
# 재귀함수
def dfs(i, j):
    global cnt, max_cnt, valid
    # print(i, j, cnt)
    if max_cnt <= cnt:
        max_cnt = cnt
    # 최댓값을 갱신해도 더 진행할 수 있기 때문에 else와 return을 쓰지 않는다.
    for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        # 내려가기
        if in_range(ny, nx) and mat[i][j] > mat[ny][nx] and not visited[ny][nx]:
            cnt += 1
            visited[ny][nx]= 1
            dfs(ny, nx)
            visited[ny][nx]= 0
            cnt -= 1
        # 땅 파기
        elif in_range(ny, nx) and valid and mat[i][j] <= mat[ny][nx] and not visited[ny][nx]:
            if mat[ny][nx] - K < mat[i][j]:
                for p in range(1, K+1):
                    if mat[ny][nx] - p < mat[i][j] and mat[ny][nx] - p >= 0:
                        # 다음부터 땅 파기 금지
                        # valid 가 False라면 땅을 판 것 True라면 땅을 팔 수 있다.
                        valid = False
                        # 땅 파기
                        mat[ny][nx] -= p
                        cnt += 1
                        visited[ny][nx]= 1
                        dfs(ny, nx)
                        visited[ny][nx]= 0
                        cnt -= 1
                        # 백트레킹 시 되돌리기
                        mat[ny][nx] += p
                        valid = True
                        # 땅은 언제나 최소한으로 파는 것이 이득
                        # 다른 곳을 가기 위해선 높은 지대가 유리
                        # 더 깊이 땅을 팔 필요가 없다.
                        break# for p


T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split()))for _ in range(N)]
    start1 = start()
    # print(start1)

    # AI 사용
    # 리스트에서 0인 값을 제거 하였다.
    # start 함수에서 가장 높은 봉우리가 최대 5개라
    # list를 5개 만들고 이에 맞추어 저장하였는데
    # 아래 for y, x in start1을 돌기 위해선 
    # 모든 리스트 내부 리스트가 원소 두개를 가져야 했다.
    # 하지만 0,0 시 0, 0도 시작지점으로 판단.
    # 즉 리스트 원소가 두개 인 것만 유지해야 했음
    # OR start 함수 제작시 append를 사용하면 해결
    # start 함수를 변경하는 것 보단 0인 원소를 제거 하였다.
    # 아래 list comprehension 식은 AI를 이용했다.
    start1 = [x for x in start1 if x != 0]

    # 시작지점인 봉우리를 포함한 값이다.
    max_cnt = 1
    # 최대 높이인 봉우리의 개수만큼 반복한다.
    for y, x in start1:
        # 방문지도 
        # 봉우리 따라 초기화 해야됨
        visited = [[0]*N for _ in range(N)]
        # 시작점 방문 후 dfs 진입
        visited[y][x] = 1
        cnt = 1 # 시작점도 길이기 때문
        dfs(y, x)
    print(F"#{test} {max_cnt}")

    '''
    방문지도 없이 41개
    방문지도 만드니 46개
    반례가 무엇일까..?
    시작점을 방문하지 않았고
    방문지도를 초기화 하지 않았다.

    AI 사용을 한 군데만 해서 뿌듯하다.
    dfs 와 백트레킹만 잘 다룬다면
    dfs 문제는 쉽게 풀 수 있을 듯 하다.
    문제에서 주어진 특이한 조건 땅 파기 와 같은 조건을
    어떤 식으로 처리해야 하는지가 큰 관건인 듯 하다.

    또한 내려가기만 해서 방문지도가 필요 없을 줄 알았지만
    지나 온 곳을 땅을 깎지 않기 위해 필요하다.
    '''
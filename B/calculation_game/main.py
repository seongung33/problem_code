def init(mJoker, mNumbers):
    pass

def putCards(mDir, mNumbers):
    pass

def findNumber(mNum, mNth, ret):
    pass

def changeJoker(mValue):
    pass

# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
# fs = open("input.txt", "r")
# input = fs.readline

CMD_INIT = 100
CMD_PUT = 200
CMD_FIND = 300
CMD_CHANGE = 400

MAX_CARD_NUM = 5
MAX_RET_NUM = 4

def run():
    query_num = int(input())
    ok = False

    for q in range(query_num):
        line = list(map(int, input().split()))
        query = line[0]

        if query == CMD_INIT:
            joker = line[1]
            numbers = line[2:2 + MAX_CARD_NUM]
            init(joker, numbers)
            ok = True
        elif query == CMD_PUT:
            dir = line[1]
            numbers = line[2:2 + MAX_CARD_NUM]
            putCards(dir, numbers)
        elif query == CMD_FIND:
            num, Nth, ans = line[1], line[2], line[3]
            ret_numbers = [-1 for i in range(MAX_RET_NUM)]
            ret = findNumber(num, Nth, ret_numbers)
            if ans != ret:
                ok = False
            if ans == 1:
                ans_numbers = line[4:]
                for i in range(MAX_RET_NUM):
                    if ans_numbers[i] != ret_numbers[i]:
                        ok = False
        elif query == CMD_CHANGE:
            value = line[1]
            changeJoker(value)

    return ok

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')

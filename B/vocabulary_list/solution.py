"""
200 -> add : 단어, 중요도, 페이지 번호
300 -> move : 왼 오, 번호, 단어
400 -> search # 단어 검색 이동
500 -> go # 사전 번호로 이동

"""


class PAGE:
    def __init__(self, no, word):
        self.no = no
        self.word = word

db = [0]
current_idx = -1

def init() -> None:
    global db, current_idx
    db = [0]
    current_idx = 0


# 주어진 문자열을 단어로 등록, 현재 페이지는 등록된 단어의 페이지로 변겨
# add(단어, 중요도)
# PAGE.no = 페이지 번호
# PAGE.word = 단어
def add(mWord : str, mImportance : int) -> PAGE:
    db.append((mWord, mImportance))
    current_idx = len(mWord) - 1
    # 페이지 번호, 단어
    return PAGE(current_idx, mWord)


# 페이지를 좌 또는 우로 이동
#mDir = 1 : 오른쪽 페이지 n -> n+1
# mDir = -1: 왼쪽 페이지 n -> n -1
def move(mDir : int) -> PAGE:
    global current_idx, db
    if mDir == -1:
        # 왼쪽으로 이동
        current_idx -= 1
        now_word = db[current_idx]
    else:
        current_idx += 1
        now_word = db[current_idx]
    return PAGE(current_idx, now_word)

# 검색기능
# 검색에 실패하면 PAGE.no = -1
# 검색 성공시 찾은 단어의 페이지로 변경
# 검색 실패시 변경  X
def search(mStr : str) -> PAGE:
    global current_idx
    for i in range(len(db)):
        if db[i] == mStr:
            current_idx = i
            return PAGE(i, db[i])
    return PAGE(-1, "")
# mNo 번의 페이지로 이동한다.
def go(mNo : int) -> PAGE:
    global current_idx
    mNo -= 1
    current_idx = mNo
    show = db[mNo]
    return PAGE(mNo, show)
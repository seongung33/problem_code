# """
# 200 -> add : 단어, 중요도, 페이지 번호
# 300 -> move : 왼 오, 번호, 단어
# 400 -> search # 단어 검색 이동
# 500 -> go # 사전 번호로 이동

# """


# class PAGE:
#     def __init__(self, no, word):
#         self.no = no
#         self.word = word

# db = [0]
# current_idx = -1

# def init() -> None:
#     global db, current_idx
#     db = [0]
#     current_idx = 0


# # 주어진 문자열을 단어로 등록, 현재 페이지는 등록된 단어의 페이지로 변겨
# # add(단어, 중요도)
# # PAGE.no = 페이지 번호
# # PAGE.word = 단어
# def add(mWord : str, mImportance : int) -> PAGE:
#     db.append((mWord, mImportance))
#     current_idx = len(mWord) - 1
#     # 페이지 번호, 단어
#     return PAGE(current_idx, mWord)


# # 페이지를 좌 또는 우로 이동
# #mDir = 1 : 오른쪽 페이지 n -> n+1
# # mDir = -1: 왼쪽 페이지 n -> n -1
# def move(mDir : int) -> PAGE:
#     global current_idx, db
#     if mDir == -1:
#         # 왼쪽으로 이동
#         current_idx -= 1
#         now_word = db[current_idx]
#     else:
#         current_idx += 1
#         now_word = db[current_idx]
#     return PAGE(current_idx, now_word)

# # 검색기능
# # 검색에 실패하면 PAGE.no = -1
# # 검색 성공시 찾은 단어의 페이지로 변경
# # 검색 실패시 변경  X
# def search(mStr : str) -> PAGE:
#     global current_idx
#     for i in range(len(db)):
#         if db[i] == mStr:
#             current_idx = i
#             return PAGE(i, db[i])
#     return PAGE(-1, "")
# # mNo 번의 페이지로 이동한다.
# def go(mNo : int) -> PAGE:
#     global current_idx
#     mNo -= 1
#     current_idx = mNo
#     show = db[mNo]
#     return PAGE(mNo, show)



class PAGE:
    def __init__(self, no, word):
        self.no = no
        self.word = word


class Node:
    def __init__(self, word, imp):
        self.word = word
        self.imp = imp
        self.prev = None
        self.next = None


head = None
tail = None
current = None

word_map = {}
size = 0


def init() -> None:
    global head, tail, current, word_map, size
    head = None
    tail = None
    current = None
    word_map = {}
    size = 0


def get_index(node):
    idx = 1
    cur = head
    while cur != node:
        cur = cur.next
        idx += 1
    return idx


def add(mWord: str, mImportance: int) -> PAGE:
    global head, tail, current, size

    new_node = Node(mWord, mImportance)

    if head is None:
        head = tail = new_node
    else:
        cur = head
        # 나보다 중요도가 낮은(작은) 첫 번째 노드를 찾음
        while cur and cur.imp >= mImportance:
            cur = cur.next

        if cur == head:  # 새 노드가 가장 중요함 (맨 앞)
            new_node.next = head
            head.prev = new_node
            head = new_node
        elif cur is None:  # 새 노드가 가장 안 중요함 (맨 뒤)
            new_node.prev = tail
            tail.next = new_node
            tail = new_node
        else:  # 중간 삽입
            prev_node = cur.prev
            # 연결 관계 설정
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = cur
            cur.prev = new_node

    word_map[mWord] = new_node
    current = new_node
    size += 1
    
    return PAGE(get_index(new_node), mWord)


def move(mDir: int) -> PAGE:
    global current

    if mDir == -1 and current.prev:
        current = current.prev
    elif mDir == 1 and current.next:
        current = current.next

    return PAGE(get_index(current), current.word)


def search(mStr: str) -> PAGE:
    global current

    if mStr not in word_map:
        return PAGE(-1, "")

    current = word_map[mStr]
    return PAGE(get_index(current), current.word)


def go(mNo: int) -> PAGE:
    global current
    if mNo < 1 or mNo > size:
        return PAGE(-1, "")

    # 최적화: 뒤에서 찾는 게 더 빠를 경우
    if mNo > size // 2:
        cur = tail
        for _ in range(size - mNo):
            cur = cur.prev
    else:
        cur = head
        for _ in range(mNo - 1):
            cur = cur.next

    current = cur
    return PAGE(mNo, cur.word)
max_node = 600000
class LinkedList:
    def __init__(self):
        self.data = [0]*max_node
        self.prev = [-1]*max_node
        self.next = [-1]*max_node
        self.node_count = 0

        self.head = 0
        self.tail = 1
        
        self.next[self.head] = self.tail
        self.prev[self.tail] = self.head

    def add_after(self, target_idx, val):
        new_node = self.node_count
        self.data[new_node] = val

        nxt = self.next[target_idx]

        self.next[new_node] = nxt
        self.prev[new_node] = target_idx
        self.next[new_node] = new_node
        self.prev[nxt] = new_node

        self.node_count += 1
        return new_node
    
    def remove(self, target_idx):
        prv = self.prev[target_idx]
        nxt = self.next[target_idx]
        
        self.next[prv] = nxt
        self.prev[nxt] = prv
        
node_map = {}

ll = LinkedList()
for i in input():
    idx_



################################################

import sys

# 입력 속도를 위해 한꺼번에 읽기
input = sys.stdin.read().split()

class EditorList:
    def __init__(self, max_nodes):
        # 더미 노드 포함 넉넉하게 할당
        self.data = [''] * (max_nodes + 2)
        self.prev = [-1] * (max_nodes + 2)
        self.next = [-1] * (max_nodes + 2)
        
        self.head = 0
        self.tail = 1
        self.node_count = 2
        
        # 초기 상태: Head <-> Tail
        self.next[self.head] = self.tail
        self.prev[self.tail] = self.head
        
        # 커서의 위치 (어느 노드의 '오른쪽'에 있는지)
        self.cursor = self.head

    def add_after_cursor(self, val):
        new_node = self.node_count
        self.data[new_node] = val
        
        a = self.cursor
        b = self.next[self.cursor]
        
        # 연결 고리 4개 조작
        self.next[new_node] = b
        self.prev[new_node] = a
        self.next[a] = new_node
        self.prev[b] = new_node
        
        # 커서를 새로 추가된 노드로 이동
        self.cursor = new_node
        self.node_count += 1

    def remove_cursor_node(self):
        # 커서가 헤드에 있으면 삭제할 것이 없음
        if self.cursor == self.head:
            return
        
        target = self.cursor
        prv = self.prev[target]
        nxt = self.next[target]
        
        # 연결 고리 끊기
        self.next[prv] = nxt
        self.prev[nxt] = prv
        
        # 커서를 이전 노드로 옮김
        self.cursor = prv

    def move_left(self):
        if self.prev[self.cursor] != -1 and self.cursor != self.head:
            self.cursor = self.prev[self.cursor]

    def move_right(self):
        if self.next[self.cursor] != self.tail:
            self.cursor = self.next[self.cursor]

    def get_result(self):
        res = []
        curr = self.next[self.head]
        while curr != self.tail:
            res.append(self.data[curr])
            curr = self.next[curr]
        return "".join(res)

# 1. 초기 문자열 입력 및 세팅
initial_str = input[0]
M = int(input[1])
# 최대 노드 수 = 초기 문자열 길이 + 명령어 개수(P 명령 최대 M번)
editor = EditorList(len(initial_str) + M)

for char in initial_str:
    editor.add_after_cursor(char)

# 2. 명령어 처리
idx = 2
for _ in range(M):
    cmd = input[idx]
    if cmd == 'L':
        editor.move_left()
    elif cmd == 'D':
        editor.move_right()
    elif cmd == 'B':
        editor.remove_cursor_node()
    elif cmd == 'P':
        idx += 1
        editor.add_after_cursor(input[idx])
    idx += 1

# 3. 출력
print(editor.get_result())
# from collections import defaultdict
# N = int(input())
# inte = map(int, input().split())
# M = int(input())
# M_inte = map(int, input().split())
# dic = defaultdict(int)
# for i in inte:
#     dic[i] += 1

# for i in M_inte:
#     print(dic[i], end = " ")

################################################

max_size = 100003

class Hashtable:
    def __init__(self):
        # 각 버킷에 키, 값을 담을 리스트
        self.table = [[] for _ in range(max_size)]

    def _get_hash(self, key):
        return abs(key) % max_size
    
    # 키 추가
    def add(self, key):
        idx = self._get_hash(key)

        for item in self.table[idx]:
            if item[0] == key:
                item[1] += 1
                return
        self.table[idx].append([key, 1])

    def find(self, key):
        idx = self._get_hash(key)
        for item in self.table[idx]:
            if item[0] == key:
                return item[1]
        return 0

ht = Hashtable()
N = int(input())
for i in map(int, input().split()):
    ht.add(i)

M = int(input())
results = [str(ht.find(x)) for x in map(int, input().split())]
print(" ".join(results))
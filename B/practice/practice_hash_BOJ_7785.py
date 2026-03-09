N = int(input())

log = {}
for i in range(N):
    name, e_l =  input().split()
    if e_l == "enter":
        log[name] = name
    else:
        del log[name]
lst = [0]*N
j = 0
for i in log:
    lst[j] = i
    j += 1
while True:
    if lst[-1] == 0:
        lst.pop()
    else:
        break
lst.sort(reverse=True)

for i in lst:
    print(i)



##################################################

# N = int(input())

# table_size = 100003
# max_nodes = 10000005

# class Hashtable:
#     def __init__(self):
#         self.head = [-1]*table_size
#         self.keys = [""]*max_nodes
#         self.nexts = [-1]*max_nodes

#         self.node_count = 0
#         self.is_removed = [False]*max_nodes

#     def get_hash(self, s):
#         h = 0
#         for char in s:
#             h = h(h*31 + ord(char)) % table_size
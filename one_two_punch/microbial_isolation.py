from collections import defaultdict
import copy
T = int(input())

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def mo(y, x):
    return 0 < y < N-1 and 0 < x < N-1


for test in range(1, T+1):
    N, M, K = map(int, input().split())

    micro_info = [[0]*4 for _ in range(K)]

    for i in range(K):
        # 세로 가로 미생물 수, 이동방향
        y, x, num, dir = map(int, input().split())
        dir -= 1
        micro_info[i] =  [y, x, num, dir]
    # print(micro_info)
    length = K
    for _ in range(M):
        dic = defaultdict(list)
        for idx, (y, x, num, dir) in enumerate(micro_info):

            ny = y + dy[dir]
            nx = x + dx[dir]

            # if not dic[(ny, nx)]:
            #     dic[(ny, nx)] = [(num, dir, idx)]
            # else:
            dic[(ny, nx)].append(( num, dir, idx))

        for key, value in dic.items():
            ny, nx = key 
            if len(value) >= 2:
                length = length - len(value) + 1
                max_num, max_dir, max_idx = dic[key][0]
                power = max_num
                for i in range(1, len(dic[key])):
                    num, dir, idx = dic[key][i]
                    if num > max_num:
                        max_idx = idx
                        max_num = num
                        max_dir = dir
                        power += max_num
                    else:
                        power += num
                for num, dir, idx in dic[key]:
                    if idx != max_idx:
                        micro_info[idx] = [0, 0, 0, 0]
                micro_info[max_idx] = [ny, nx, power, max_dir]
            else:
                # print(value)
                num, dir, idx = value[0]
                if not mo(ny, nx):
                    if dir == 1:
                        dir = 0
                    elif dir == 0:
                        dir = 1
                    elif dir == 2:
                        dir = 3
                    elif dir == 3:
                        dir = 2
                    micro_info[idx] = [ny, nx, num//2, dir]
                    if num//2 == 0:
                        length -= 1
                else:
                    micro_info[idx] = [ny, nx, num, dir]
        idx = 0
        new_lst = [0]*length
        # print(micro_info)
        for i in range(len(micro_info)):
            if micro_info[i][2]:
                y, x, num, dir = micro_info[i]
                new_lst[idx] = [y, x, num, dir]
                idx += 1
        micro_info = copy.deepcopy(new_lst)
        # print(micro_info)
                
    ans = 0

    for i in range(len(micro_info)):
        ans += micro_info[i][2]

    print(F"#{test} {ans}")
            


            

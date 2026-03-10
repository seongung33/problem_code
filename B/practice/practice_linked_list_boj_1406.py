left_list = list(input().strip())
right_list = []

for i in range(int(input())):
    func = input()
    if func == "L":
        if not left_list:
            continue
        cursor = left_list.pop()
        right_list.append(cursor)
    elif func == "D":
        if not right_list:
            continue
        else:
            cursor = right_list.pop()
            left_list.append(cursor)
    elif func == 'B':
        if not left_list:
            continue
        left_list.pop()
    else:
        left_list.append(func[2])
right_list.reverse()
print(''.join(left_list)+''.join(right_list))
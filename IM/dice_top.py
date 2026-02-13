# 주사위르 쌓을때 아랫주사위의 윗면 숫자와 윗 주사위의 아랫면 숫자가 같다.
# 4개의 옆면 중에서 한면의 숫자의 합이 최대가 되어야 한다.
# 주사위 돌리기
def dice_change(dice):
    print(dice)
    for i in range(6):
        if dice[i] == 6:
            six = i
            break # for i
    if six == 3:
        temp = dice[1]
        dice[2:5] = dice[1:4]
        dice[1] = temp
        print(dice)
    elif six == 1:
        temp = dice[4]
        dice[2:5] = dice[1:4]
        dice[1] = temp
        print(dice)
    elif six == 4:
        temp = [0, 0]
        temp[0:2] = dice[1:3]
        dice[1:3] = dice[3:5]
        dice[3:5] = temp[0:2]
        print(dice)
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
new_dices = []
i = 0
# for j in range(N):
dice_change(dices[i])

while i < 6:

    dice_change(i)
    for j in range(i+1, 5):
        if dices[i][0] == dices[j+1][5]:
            new_dices.append(dices[j+1])
            new_dices.append(dices[i])
            i += 1
            break # for j
    i += 1
print(new_dices)

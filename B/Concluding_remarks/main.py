words_list = []
player = []
player_true = []
player_num = 0
use_words_list = [0]*100020
use_words_list_idx = 0
alpha = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,


}

def init(N, M, mWords):
    global words_list, player, player_true, player_num
    words_list = [[0]*(M*2+10) for _ in range(26)]
    player = [i for i in range(N)]
    player_true = [True]*N
    player_num = N
    for i in mWords:
        idx = alpha[i[0]]
        words_list[idx][0] += 1
        inner_idx = words_list[idx][0]
        words_list[idx][inner_idx] = i
    for i in range(26):
        temp_set = set(words_list[i])
        temp_list = list(temp_set)
        temp_list.sort(key=str)
        words_list[i] = temp_list # 2번째부터 사용
def playRound(mID, mCh):
    global use_words_list_idx
    print(words_list)
    start_player = mID - 1
    use_words = []
    start_word =''
    end_word = alpha[mCh]
    for i in range(26):
        words_list[i][0] = 2
    while True:
        if player_true[start_player] == False:
            start_player += 1
            continue
        if start_player >= player_num:
            start_player = 0
        word_idx= words_list[end_word][0]
        words_list[end_word][0] += 1
        try:
            start_word = words_list[end_word][word_idx]
            use_words.append(start_word)
            use_words_list[use_words_list_idx] = start_word
            use_words_list_idx += 1
            start_player += 1
        except:

            # 단어 뒤집어서 넣기 
            for i in use_words:
                reverse_word = i[::-1]
                for j in use_words_list:
                    if j == 1 or reverse_word == j:
                        player_true[start_player] = False
                        break # for j
                        return start_player
                        
                    else:
                        start_word_idx = alpha[reverse_word[0]]
                        words_list[start_word_idx].append(reverse_word)
                        


            return start_player



# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
# fs = open("sample_input.txt", "r")
# input = fs.readline

def run():
    ok = True
    N, M = map(int, input().split())
    mWords = [input().rstrip() for i in range(M)]

    init(N, M, mWords)
    print(words_list)
    print(player)
    cnt = int(input())
    for _ in range(cnt):
        line = input().split()

        mID = int(line[0])
        mCh = line[1]
        ret = playRound(mID, mCh)
        ans = int(line[2])

        if ret != ans:
            ok = False

    return ok

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')

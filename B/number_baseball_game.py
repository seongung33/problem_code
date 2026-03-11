# GPT 버전 메인
import sys

N = 4
MAX_QUERYCOUNT = 1000000
limit_query = 2520

digits = [0]*N
digits_c = [0]*10
querycount = 0


class Result:
    def __init__(self, strike=0, ball=0):
        self.strike = strike
        self.ball = ball


def isValid(guess):
    guess_c = [0]*10

    for i in range(N):
        if guess[i] < 0 or guess[i] >= 10 or guess_c[guess[i]] > 0:
            return False
        guess_c[guess[i]] += 1

    return True


def query(guess):
    global querycount

    if querycount >= MAX_QUERYCOUNT:
        return Result(-1, -1)

    querycount += 1

    if not isValid(guess):
        return Result(-1, -1)

    strike = 0
    ball = 0

    for i in range(N):
        if guess[i] == digits[i]:
            strike += 1
        elif digits_c[guess[i]] > 0:
            ball += 1

    return Result(strike, ball)


def initialize(num_str):
    global querycount

    for i in range(10):
        digits_c[i] = 0

    for i in range(N):
        digits[i] = int(num_str[i])
        digits_c[digits[i]] += 1

    querycount = 0


def check(guess):
    for i in range(N):
        if guess[i] != digits[i]:
            return False
    return True


# -------------------------
# User Solution
# -------------------------

class UserSolution:

    def doUserImplementation(self, guess):
        probably = [True]*10
        for i in range(4):
            guess[i] = i
        result = query(guess)
        st = result.strike
        b = result.ball
        if st + b == 0:
            for i in range(4):
                probably[i] = False
        elif st + b == 4:
            for i in range(4, 10):
                probably[i] = False

        guess[0:4] = range(4, 8)
        result = query(guess)
        st = result.strike
        b = result.ball
        if st + b == 0:
            for i in range(4, 8):
                probably[i] = False
        elif st + b == 4:
            for i in range(4):
                probably[i] = False
            for i in range(8, 10):
                probably[i] = False


        # while True:
        # maybe = [0]*10
        # g = [0]*4



# -------------------------
# Main
# -------------------------

def main():
    input = sys.stdin.readline

    T = int(input())
    total_score = 0
    total_querycount = 0

    user = UserSolution()

    for testcase in range(1, T+1):

        num_str = input().strip()
        initialize(num_str)

        guess = [0]*N
        user.doUserImplementation(guess)

        global querycount

        if not check(guess):
            querycount = MAX_QUERYCOUNT

        if querycount <= limit_query:
            total_score += 1

        print(f"#{testcase} {querycount}")

        total_querycount += querycount

    if total_querycount > MAX_QUERYCOUNT:
        total_querycount = MAX_QUERYCOUNT

    print(f"total score = {total_score*100//T}")
    print(f"total query = {total_querycount}")


if __name__ == "__main__":
    main()


T = int(input())
for test in range(1, T + 1):
    s = input()
    #s 문자열이 회문인가?

    # 해결법
    # 1. 전체를 뒤집어서 원본과 같은지 비교
    # 2. 절반 기준으로 앞과 뒤가 같은지 비교

    #정답
    answer = 0
    # 2의 방법을 채택한다.
    for i in range(len(s) >> 1):
        if s[i] != s[len(s) - 1 - i]:
            break
    #위의 반복문이 중간에 종료(break) 되지 않았다면 실행되는 코드
    else:
        answer = 1
    print(f"#{test} {answer}")


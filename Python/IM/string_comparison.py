# 테스트 케이스
T = int(input())
for test in range(1, T + 1):

    # 첫번째 문자열
    N = input() #찾을 값
    # 두번째 문자열
    M = input() # 찾는 위치

    # 함수를 사용하여 return을 통해 일치한 문자열 찾을 시 반복문 즉시 종료
    # 완전 탐색 순회
    def compare(str1, str2):
        # 아래서 일치할시 str1의 길이만큼 탐색하므로
        # 인덱스 에러가 뜨지 않기 위해 해당 길이만큼 적게 지정
        for i in range(len(str2)-len(str1) + 1):
            # str2의 원소 중 하나가 str1의 첫 번째 원소와 일치하다면 이후 값 비교 시작
            if str2[i] == str1[0]:
                # 첫 원소는 비교하였으므로 인덱스 1부터 시작
                cnt = 0
                for j in range(0, len(str1)):
                    # 방법 1. 모든 원소가 일치하면 통과
                    # 방법 2. 원소가 불일치하면 break. 모두 일치하면 else 사용

                    # 방법 1.
                #     if str2[i+j] ==str1[j]:
                #         cnt += 1
                # # 논리: 모든 원소가 일치하면 str1의 길이와 cnt의 값이 같을 것이다.
                # # 하지만 첫 원소는 비교하여 제외하였으므로 길이 -1 을 진행한다.
                # if cnt == len(str1):
                #     answer = 1
                #     return answer

                    # 방법 2.
                    # 값이 일치하지 않으면 break 그럼 else 문이 작동하지 않는다.
                    if str2[i+j] !=str1[j]:
                        break
                else:
                    #else 문 작동시 문자열이 일치하였으므로 1 반환
                    answer = 1
                    return  answer
        # 찾지 못하였을 시 0 반환
        answer = 0
        return answer

    print(f"#{test} {compare(N, M)}")
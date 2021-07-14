# 뒤집기
def solution(n):
    answer = []

    n = str(n)

    for i in range(len(n)-1, -1, -1):
        answer.append(int(n[i]))

    print(answer)

    return answer

solution(12345)
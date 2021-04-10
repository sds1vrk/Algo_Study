def solution(number, k):
    num_size = len(number) - k
    # 10-4 =6 개
    start = 0
    answer = ""
    for i in range(num_size):
        max_num = number[start]
        max_idx = start

        for j in range(start, k + i + 1):
            if max_num < number[j]:
                max_num = number[j]
                max_idx = j

                # print("max_num",max_num)

                # 10번 케이스 시간초과 발생 방지
                if max_num=="9":
                    break
                   # print("test")

        start = max_idx + 1
        answer += max_num

    # print(answer)

    # answer = ''
    return answer


# solution("1924",2)
# solution("1231234", 3)
solution("4177252841",4)
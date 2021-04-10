def solution(number, k):
    num_size = len(number) - k
    # 10-4 =6 개
    start = 0
    answer = ""
    result=[]
    for i in range(num_size):
        max_num = number[start]
        max_idx = start

        for j in range(start, len(number)-(num_size-len(result))+1):
            if max_num < number[j]:
                max_num = number[j]
                max_idx = j

                # print("max_num",max_num)

                # 10번 케이스 시간초과 발생 방지
                if max_num=="9":
                    print("test")
                    break


        start = max_idx + 1
        # answer += max_num
        result.append(max_num)

    answer="".join(result)
    print(answer)

    # answer = ''
    return answer


solution("1924",2)
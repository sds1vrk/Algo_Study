def solution(number, k):
    last = len(number) - k
    res = []
    # 구할려는 자리수
    ans = len(number) - k

    # 큰수 찾고 해당 앞까지 인덱스 지우기
    def find_su(m):
        max_val = 0
        for i in range(len(m)):
            if max_val <= int(m[i]):
                max_val = int(m[i])

            if int(m[i])==9:
                return str(max_val)


        # return 큰 수
        # print("max_val",max_val)
        return str(max_val)

    while True:
        if len(res) == ans:
            break

        # 만약 숫자가 2개 남고 들어가야 할 자리가 1자리라면 둘중
        # if len(number)==2 and ans-len(res)==1:
        # max_value=find_su(number)
        # res.append(max_value)
        # continue

        # 숫자 자르기

        temp = number[:len(number)-last+1]
        last_temp = number[len(number)-last:]
        max_value = find_su(temp)
        # max_value 추가하기
        res.append(max_value)
        # max_value 앞까지 지우기

        # 인덱스 찾고 해당 인덱스까지 지우기
        idx = temp.find(max_value)
        # print("idx",idx,"max",max_value)
        # temp=temp[idx+1:]

        # number=temp+last_temp
        number = number[idx + 1:]
        # print("numb", number)

        last -= 1
        # print("last",last)

        # 만약 필요한 자리가 m개와 들어가야 자리가 m개로 같다면
        # print("ans-len(res)", ans - len(res), len(number))
        if ans - len(res) == len(number):
            for i in range(len(number)):
                res.append(number[i])
            return ''.join(res)

        # 만약 숫자가 2개 남고 들어가야 할 자리가 1자리라면 둘중
        if len(number) == 2 and ans - len(res) == 1:
            max_value = find_su(number)
            res.append(max_value)
            continue

    # print("res", res)


    answer = ''.join(res)
    return answer

# solution("1924",2)
# solution("1231234",3)
print(solution("4177252841",4,),"775841")
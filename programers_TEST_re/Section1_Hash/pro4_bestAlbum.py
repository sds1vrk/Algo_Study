def solution(genres, plays):
    data = dict()
    for i, j in enumerate(genres):
        key = j
        value = [plays[i], i]

        if key in data:
            data[key].append(value)

        else:
            data[key] = [value]

    # print("data",data)

    # value 값 오름차순 정렬
    # print(data.values())
    for i in data.keys():
        k = data[i]
        # x[0]으로 내림차순 정렬 후 , x[1]로 오름차순 정렬
        sort_k = sorted(k, key=lambda x: (x[0], -x[1]), reverse=True)
        data[i] = sort_k
    # print("data",data)

    # 합 구하기
    for i in data.keys():
        k = data[i]
        res = 0
        for j in k:
            res += j[0]

        data[i].append(res)

    # print("data",data)

    # 어떤것이 장르가 첫번쨰인지 고르기
    # 장르를 기준으로
    result = []
    for i in data.values():
        result.append(i)

    result = sorted(result, key=lambda x: x[-1], reverse=True)
    # print("result",result)
    answer = []
    for i in result:
        # print("len",len(i))
        # print("jj",i)
        temp = []
        for j in range(len(i) - 1):
            temp.append(i[j][1])
            # print("kk",i[j][1])
            if len(temp) == 2:
                break

        answer.extend(temp)

    # print("ans",answer)

    return answer
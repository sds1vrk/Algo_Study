def solution(clothes):
    data = dict()

    for i in clothes:
        key=i[1]
        value=i[0]

        if key in data:
            data[key].append(value)

        else :
            data[key]=[value]

    # print(data)


    result=1
    # 계산식 headgear:2, eyeware:1개
    # ==> 경우의 수 : 안입는 경우포함하기 떄문에 (2+1) * (1+1)  -1
    # 모두 안입는 경우는 -1
    for i in data.keys():
        result=result*(len(data[i])+1)

    result-=1


    # print("an",result)


    return result


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
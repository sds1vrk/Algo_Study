

def solution(participant, completion):


    # a=set(participant)
    # b=set(completion)
    # result=[i for i in a if i not in b]
    # print(result)

    data=dict()
    for i in range(len(participant)):
        # data[participant[i]]=participant.count(participant[i])
        data[participant[i]] = 0

    # print(data)

    parti=dict()
    for j in range(len(completion)):
        # parti[completion[j]] = completion.count(completion[j])
        parti[completion[j]] = 0

    data_key=data.keys()
    # data_value=data.values()

    parti_key=parti.keys()
    # parti_value=parti.values()

    for i in data_key:
        data[i]=participant.count(i)

    for i in parti_key:
        parti[i]=completion.count(i)

    print(data)
    print(parti)

    # result = [i for i in data_key if i not in parti_key]

    # 리프리헨션으로 된거 for문으로 변경해보기
    result1=[]

    for i in data_key:
        if i not in parti_key:
            result1.append(i)
            break

        elif i in parti_key and data[i]>parti[i]:
            result1.append(i)
            break

    print("result1",result1)

    # if not result:
    #     result = [i for i in data_key if i in parti_key if data[i] > parti[i]]
    # print(result)

    # List를 문자열로 변환
    return "".join(map(str,result1))





    # answer = result[0]


    # return answer


# solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
# solution(["leo", "kiki", "eden"],["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
def solution(participant, completion):
    # 정렬
    participant.sort()
    completion.sort()

    # dict 이용하여 개수 세기
    data = dict()
    # 참여자의 id : key, 수 : value
    for i in participant:
        if data.get(i):
            v = data[i]
            data[i] = v + 1
        else:
            data[i] = 1

    # print("data",data)
    comple = dict()
    # 완주자
    # 완주자의 id : key, 수 : value
    for i in completion:
        if comple.get(i):
            v = comple[i]
            comple[i] = v + 1

        else:
            comple[i] = 1

    # 완주자에서 참여자 제외하기
    answer = ""
    for i in comple:
        data[i] = data[i] - comple[i]

    # value가 0이 아닌 것 뽑아서 answer에 넣기
    # print(data)
    for i in data:
        if data[i] != 0:
            answer += i

    return answer
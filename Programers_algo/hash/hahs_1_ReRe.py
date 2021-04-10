# set으로 문제 풀기
# set은 list를 unique집합으로 만든다
# 따라서 동명 이인이 있는지 없는지 판단
# 있을 경우 두 집합에서 다를 경우를 뽑는다

def solution(participant,completion):


    participant_set=set(participant)
    completion_set=set(completion)

    result=list(participant_set-completion_set)

    if result !=[]:
        return result[0]

    else :
        for i in completion:
            a=completion.count(i)
            b=participant.count(i)

            if a!=b:
                return i
    return None



solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
# solution(["leo", "kiki", "eden"],["eden", "kiki"])
# solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])

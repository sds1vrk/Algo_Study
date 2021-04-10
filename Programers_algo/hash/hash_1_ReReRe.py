# sort를 한 후 최대한 빨리 찾는 방법

def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]

    return participant[len(participant)-1]
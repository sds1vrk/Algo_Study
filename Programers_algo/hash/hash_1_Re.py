def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print("hash:",hash(part),"part",part)
        temp += int(hash(part))

    print(temp)
    for com in completion:
        print("hash2:", hash(com), "part2", com)
        temp -= hash(com)
    answer = dic[temp]

    return answer

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
# solution(["leo", "kiki", "eden"],["eden", "kiki"])
# solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
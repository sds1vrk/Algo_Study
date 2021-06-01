def solution(n, words):
    visit = dict()

    for word in words:
        visit[word] = 0
    # cnt=0
    temp = words[0]
    visit[temp] = 1
    res = []
    for i in range(1, len(words)):
        # cnt+=1

        # 단어끝말잇기 안맞으면 종료
        if temp[-1] != words[i][0]:
            res.append(i + 1)
            break

        # print("words[i]",words[i])
        if visit[words[i]] == 0:
            visit[words[i]] = 1

        else:
            res.append(i + 1)
            break

        temp = words[i]

    else:
        res.append(0)

    # print("res",res)
    k = res[0]

    if k == 0:
        return [0, 0]

    # order : 몫 몇번쨰에
    order = k // n

    # 누가?, 나머지
    who = k % n
    if who == 0:
        who = n - who

    else:
        order += 1

    return [who, order]

    return answer



# solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])

# solution(2, ["land", "dream", "mom", "mom"])
print(solution(	2, ["land", "dream", "mom", "mom"]),"[2,2]")
print(solution(	2, ["land", "dream", "mom", "mom", "ror"]),"[2,2]")
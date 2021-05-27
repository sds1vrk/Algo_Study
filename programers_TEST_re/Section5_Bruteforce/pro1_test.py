def solution(answers):
    # 1,2,3문제 개수에 대한 1,2,3번에 각 답안지 만들기
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # answers는 : 10000문제
    k = len(answers)

    if k > len(a):
        na = k % len(a)
        a = a * (k // len(a))
        for i in range(na):
            a.append(a[i])

    if k > len(b):
        na = k % len(b)
        b = b * (k // len(b))
        for i in range(na):
            b.append(b[i])

    if k > len(c):
        na = k % len(c)
        c = c * (k // len(c))
        for i in range(na):
            c.append(c[i])

    # 문제풀이
    res = []
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    for i in range(len(answers)):
        if answers[i] == a[i]:
            cnt_a += 1

        if answers[i] == b[i]:
            cnt_b += 1

        if answers[i] == c[i]:
            cnt_c += 1

    else:
        res.append(cnt_a)
        res.append(cnt_b)
        res.append(cnt_c)

    # print("res",res)
    ans = []
    temp = max(res)
    for i in range(len(res)):
        if temp <= res[i]:
            temp = res[i]
            ans.append(i + 1)

    # print("ans",ans)
    return ans
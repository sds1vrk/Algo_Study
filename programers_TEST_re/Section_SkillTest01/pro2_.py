def solution(x):
    answer = True

    # 자리수 구하기
    k = str(x)
    k_len = len(k)
    a = 0
    check = []
    while a < k_len:
        a += 1
        k = int(k)
        ans = k % 10
        check.append(ans)
        k = k // 10

    # print(check)
    ans = sum(check)
    # print(ans)

    if x % ans == 0:
        answer = True
    else:
        answer = False

    return answer


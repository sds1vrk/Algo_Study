def solution(n):
    # n이 홀수가 될떄까지 계속 나눔
    while True:
        if n % 2 == 1:
            break
        else:
            n = n // 2

    print(n)
    # 이 n을 가지고 이진법 구한다음 1의 개수세기, 0은 순간이동임
    cnt = 0
    res = []
    # 2진법으로 구하기
    while n >= 1:
        k = n % 2
        res.append(k)
        n = n // 2

    # print("res",res)
    res = res[::-1]
    cnt = 0
    # 1의 개수 세기
    for i in res:
        if i == 1:
            cnt += 1

    return cnt
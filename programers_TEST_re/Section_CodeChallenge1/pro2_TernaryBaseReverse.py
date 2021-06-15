# N 진법 만드는 방법
# res=int("res",n)
# print(res)


def solution(n):
    res = ""
    while n >= 1:
        k = n % 3
        res += str(k)
        n = n // 3

    # print("res",res)

    val = 0

    # 3진법 방법 1
    # for i in range(len(res)):
    # y=len(res)-1-i
    # val+=int(res[i])*3**y

    # 3진법 방법 2
    # int를 이용하여 3진법 변경
    # int("res",진법)
    val = int(res, 3)

    return val
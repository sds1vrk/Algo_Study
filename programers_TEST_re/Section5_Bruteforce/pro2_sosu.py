# numbers의 총 길이가 7이하 이기 때문에 permutations 가능
# 총 경우의 수는 2^7*2=256개 밖에 안되기
from itertools import permutations


def solution(numbers):
    size = len(numbers)
    res = []

    def prime_num(k):
        for i in range(2, k):
            if k % i == 0:
                return False
        else:
            return True

    cnt = 0
    res = []
    for i in range(1, size + 1):
        k = list(set(list(map(''.join, permutations(numbers, i)))))
        # print("k",k)
        k = list(map(int, k))
        # print("num_k",k)
        res.extend(k)

    res = list(set(res))
    # print("res",res)
    for i in res:
        if i >= 2:
            pan = prime_num(i)
            if pan:
                cnt += 1

    return cnt
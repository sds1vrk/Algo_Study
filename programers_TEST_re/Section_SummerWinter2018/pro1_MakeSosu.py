# nums가 50개 이하 최대는 50C3이므로 combination 사용 가능
from itertools import combinations


def solution(nums):
    cnt = 0

    # 조합으로 나올수 있는 리스트
    a = list(map((lambda x:sum(x),combinations(nums, 3))))
    # print("a",a)
    a_hap = []
    for i in a:
        a_hap.append(sum(i))

    # print(a_hap)

    def prime_num(k):
        for i in range(2, k):
            if k % i == 0:
                return False

        else:
            return True

    # 소수인지 확인
    for i in a_hap:
        pan = prime_num(i)

        if pan:
            cnt += 1

    return cnt
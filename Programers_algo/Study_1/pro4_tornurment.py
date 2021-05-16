# 예상 대진표
# a,b 경기는 언제 만날까?!
# 풀이 방법 : 다음 라운드 때 토너먼트 수를 구하는 것이 핵심

import random
def solution(n, a, b):
    count=0
    while a!=b:
        count+=1
        # 1을 더한 후에 2로 나눈 몫이 핵심
        # 다음 라운드떄 번호를 알 수 있음
        a=(a+1)//2
        b=(b+1)//2

    # print(count)

    # while True:
    # answer = 3
    return count

solution(8, 4, 7)
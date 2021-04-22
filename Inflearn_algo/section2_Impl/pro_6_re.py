# 각 자리수의 합
# 강의는 몫과 나머지를 이용해 각 자리수의 합을 구하였음

#  자릿수의 합

import sys
sys.stdin=open("input.txt","rt")

n=int(input())

array=[i for i in map(int,input().split())]
# print(array)

def digit_sum(x):
    sum=0
    while x>0:
        # %는 몫, // 나머지
        sum+=x%10
        x=x//10
    return sum

max_value=-214700000
for i in array:
    tot=digit_sum(i)
    if tot>max_value:
        max_value=tot
        res=i

print(res)
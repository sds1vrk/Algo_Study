# 정다면체

import sys
sys.stdin=open("../section1/3190.txt", "rt")

n,m=map(int,input().split())

mi=2
ma=n+m

array=[0]*(ma+3)

for i in range(1,n+1):
    for j in range(1,m+1):
        value=i+j
        # print(value,array[value])
        array[value]=array[value]+1
# print(array)

# 가장 큰 값 뽑기
kk=max(array)
# print(kk)

for i in range(n+m+1):
    if kk==array[i]:
        print(i,end=" ")


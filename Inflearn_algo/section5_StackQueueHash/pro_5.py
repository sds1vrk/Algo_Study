# 공주 구하기
# 큐 자료구조
from collections import deque

import sys
# sys.stdin=open("input.txt","r")

n,m=map(int,(input().split()))

a=[i+1 for i in range(n)]
# print(a)
# a=[]
# for i,j in enumerate(range(n)):
    # a+=[[i,j)]
# time=0
# while a:
#     a.pop

queue=deque(a)
# queue.append()
# print(queue)
time=0
result=[]
while queue:
    #
    time += 1
    queue.append(queue.popleft())

    if time==m-1:
        k = queue.popleft()
        # print("k",k)
        result.append(k)
        time=0
        # print(queue)

print(result[-1])

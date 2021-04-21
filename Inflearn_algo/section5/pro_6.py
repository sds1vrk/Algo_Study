from collections import deque

import sys
import copy
# sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

a=list(map(int,input().split()))


queue=deque()
for i,j in enumerate(a):
    idx,val=i,j
    # print(idx,val)
    queue.append((idx,val))

# print(a)
# print(queue)
ans=a[m]
# print(ans)
res=[]
time=0
def pan(s,queue):
    while queue:
        idx,k=queue.popleft()
        # print("k",k)

        if s<k:
            return True

    return False

while queue:
    idx,s=queue.popleft()

    copy_queue=deque(queue)
    if pan(s,copy_queue):
        queue.append((idx,s))

    else:
        # res.append(s)
        time+=1
        if idx==m:
            print(time)


# print(res)

# for i,j in enumerate(res):
#     if j==ans:
#         print(i+1)
    # print(i,j)
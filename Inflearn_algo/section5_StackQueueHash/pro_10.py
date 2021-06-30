# 최소 힙

import sys
# sys.stdin=open("3190.txt","r")

stack=[]
res=[]
while True:
    num=int(input())

    if num==-1:
        break

    elif num==0:
        k=min(stack)
        res.append(k)
        stack.remove(k)
    else :
        stack.append(num)

for i in res:
    print(i)

# print("".join(map(str,res)))
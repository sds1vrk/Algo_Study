# 스택
# 후위 표현식 계산하기

import sys
sys.stdin=open("input.txt","r")

nums=input()

# print(eval("2+3"))
stack=[]

res=0


for x in nums:
    if x.isdecimal():
        stack.append(int(x))

    else :
        if x=="+":
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)

        if x=="-":
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)

        if x=="*":
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)

        if x=="/":
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)

print(stack)
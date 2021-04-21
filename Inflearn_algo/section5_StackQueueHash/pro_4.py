# 스택
# 후위 표현식 계산하기

import sys
sys.stdin=open("input.txt","r")

nums=input()

# print(eval("2+3"))
stack=[]

res=0
# res+="2"
# res+="+"
# res+="3"
# print(eval(res))

c=""
for i in range(len(nums)):
    if nums[i].isdigit():
        stack.append(nums[i])

    else :
        b=stack.pop()
        a=stack.pop()
        c=a+nums[i]+b
        c=eval(c)
        # print("c",c)
        stack.append(str(c))

        # 종료 시점
        if len(nums)-1==i:
            res=str(c)
        c=""

print(stack)

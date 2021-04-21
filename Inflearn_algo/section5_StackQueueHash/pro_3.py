# 스택
# 후위표현식 만들기

import sys
sys.stdin=open("input.txt","r")

n=input()

print(n)

stack=[]
result=""
for i in n:
    if i.isdigit():
        result+=i

    else :
        # 처음 시작은 괄호
        if i=="(":
            stack.append(i)

        elif i=="*" or i=="/":
            # 만약 스택이 비어있지 않고 앞에께 *, /가 먼저 있다면 빼서 결과값에 넣는다
            while stack and (stack[-1]=="*" or stack[-1]=="/") :
                result+=stack.pop()

            stack.append(i)

        elif i=="+" or i=="-":
            # 만약 스택이 비어 있지 않고 앞에것이 '('오기 전까지는 먼저 처리를 해야 되므로 결과값에 다 빼서 넣는다
            while stack and stack[-1]!="(" :
                result+=stack.pop()
            stack.append(i)

        elif i==")":
            while stack and stack[-1]!="(":
                result+=stack.pop()
            # 여기에서는 stack에 있는것을 빼야됨 '('남아있기 떄문에 빼야됨
            stack.pop()

# 남아있는것을 pop하면서 출력
while stack:
    result+=stack.pop()

print(result)


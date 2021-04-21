# Stack 문제
# 쇠막대기
# range로 하는 이유는 원본데이터가 필요하기 때문에
# 앞에께 닫는 괄호인지 여는 괄호인지로 구분, 원본 데이터가 필요해서 range로 반드시 해야 함

import sys
sys.stdin=open("input.txt","r")

n=input()

stack=[]
answer=0


for i in range(len(n)):
    if n[i]=="(":
        stack.append(n[i])

    else :
        # 바로 전이 '('이고 다음에 올게  ')'이면 레이저 이므로 stack에 남은거 세기
        if n[i-1]=="(":
            stack.pop()
            answer+=len(stack)
        # 바로 전이 ')'이고 다음에 올게 ')' 이면 닫는 괄호 이기 때문에 stack에서 빼주고 answer+1만 해주기
        else :
            stack.pop()
            answer+=1

print(answer)







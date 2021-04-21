# 스택으로 풀어야 됨

import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

# str 시키고 ==> int 숫자화 시켜 list로 저장
n=list(map(int,str(n)))
stack=[]
print("n",n)

for x in n:
    # stack 비어있지 않고, 지울려고 하는게 있고, stack에서 나온게 x보다 크다면 계속 돌면서, 앞에꺼 제거
    while stack and m>0 and stack[-1]<x:
        k=stack.pop()
        m-=1
        print("k",k)

    # 자기 앞에꺼를 다 없앴으면, 자기가 앞으로 들어감
    # 처음엔 5 들어감, 2 들어감, 7이 나옴
    # 7은 while문에 걸림 ==> 2를 뺌, 5를 뺌
    # 6이 들어감
    # 8이 while에 걸림 ==> 6을 뺌뺌  ==> 3개 다 뺌 그러면 더이상 while문에 안걸림
    stack.append(x)

# 다 지우지 못하는 경우가 있으면

if m!=0:
    stack=stack[:-m]

#string 화 되서 붙여줌
res=''.join(map(str,stack))
print(res)


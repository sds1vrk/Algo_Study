# 단어 찾기
# 시에 쓰이지 않는 단어 찾기

import sys
# sys.stdin=open("3190.txt","r")

n=int(input())

node=[]
content=[]
for i in range(n):
    node.append(input())

for j in range(n-1):
    content.append(input())

# 오름차순으로 정렬 ==> 무조건 답은 1개이기 때문에
node.sort()
content.sort()

# print(node)
# print(content)

result=""
for i in range(len(content)):
    if content[i]!=node[i]:
        # print(content[i])
        result=node[i]
        break

if result=="none":
    result=content[-1]

print(result)








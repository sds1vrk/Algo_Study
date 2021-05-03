# 동전 교화문제
# 각 동전의 개수만큼 0~N로 풀어야 함
# 예를들면 100원 짜리 동전 5개 ==> 0,100,100*2,100*3,100*4,100*5

import sys
# sys.stdin=open("input.txt","r")
t=int(input())
m=int(input())
p=[]
n=[]

for i in range(m):
    a,b=map(int,input().split())
    # 동전의 금액
    p.append(a)
    # 동전의 개수
    n.append(b)


res=0
# 만들수 있는 동전가지치기
def dfs(l,s):
    global res

    # 가지치기
    if s>t:
        return


    if l==m:
        if s==t:
            res+=1


    else :
        # 가지치기 각 동전의 개수만큼
        # print(n[l]+1)
        c=n[l]+1
        for i in range(n[l]+1):
            dfs(l+1,s+(p[l]*i))


dfs(0,0)
print(res)

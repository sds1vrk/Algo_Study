# 동전 교화문제
# 이렇게 풀면 중복제거가 불가능 예를들면 (1,1,2,2) ==> (1,1,2) (1,1,2) 이렇게 같아버리는 경우가 발생

import sys
sys.stdin=open("input.txt","r")
n=int(input())
m=int(input())
c=[]
for i in range(m):
    a,b=map(int,input().split())
    for j in range(b):
        c.append(a)

print(c)

res=0
# 만들수 있는 동전가지치기
def dfs(l,s):
    global res
    if l==len(c):
        if s==n:
            res+=1


    else :
        dfs(l+1,s+c[l])
        dfs(l+1,s)


dfs(0,0)
print(res)

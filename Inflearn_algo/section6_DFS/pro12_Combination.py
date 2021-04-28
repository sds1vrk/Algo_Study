# DFS로 조합 구하기

# n,m => 4,2

import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

cnt=0
ch=[0]*m
def dfs(l,s):
    global cnt
    # ch가 꽉찼을때 종료
    if l==m:
        cnt+=1
        for i in range(m):
            print(ch[i],end=" ")
        print()

    else :
        for i in range(s,n+1):
            ch[l]=i
            dfs(l+1,i+1)

dfs(0,1)
print(cnt)
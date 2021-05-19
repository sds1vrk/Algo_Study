# Top Down 방식 (재귀)

import sys
sys.stdin=open("input.txt","r")

n=int(input())
# 메모제이션
dp=[0]*(n+1)
def dfs(n):
    if dp[n]!=0:
        return dp[n]

    if n==1 or n==2:
        return n

    else :
        dp[n]=dfs(n-1)+dfs(n-2)
        return dp[n]



print(dfs(n))
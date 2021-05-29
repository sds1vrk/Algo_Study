# 알리바바 DP문제

import sys
sys.stdin=open("input.txt","r")

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

dp=[[0*i for i in range(n)] for _ in range(n)]

# N,M의 최소 에너지

dp[0][0]=a[0][0]
print(dp)


for i in range(n):
    for j in range(n):
        if i==0:
            dp[i][j]=dp[0][j-1]+a[i][j]

        elif j==0:
            dp[i][j]=dp[i-1][j]+a[i][j]

        else :
            dp[i][j]=min(dp[i-1][j]+a[i][j],dp[i][j-1]+a[i][j])

print(dp)
print(dp[n-1][n-1])

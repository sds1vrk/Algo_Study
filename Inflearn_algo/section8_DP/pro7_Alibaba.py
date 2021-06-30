# 알리바바 문제
import sys
# sys.stdin=open("3190.txt","r")

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]
# print(a)
dp=[[0]*n for _ in range(n)]

dp[0][1]=a[0][0]+a[0][1]
dp[1][0]=a[0][0]+a[1][0]

# print(dp)

for i in range(n):
    for j in range(n):
        if dp[i][j]==0 and i==0:
            dp[i][j]=dp[i][j-1]+a[i][j]

        elif dp[i][j]==0 and j==0:
            dp[i][j]=dp[i-1][j]+a[i][j]

        else :
            if dp[i][j]==0:
                if dp[i-1][j]<dp[i][j-1]:
                    dp[i][j]=dp[i-1][j]+a[i][j]

                else :
                    dp[i][j]=dp[i][j-1]+a[i][j]


print(dp[n-1][n-1])






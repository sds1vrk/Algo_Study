# 동전 교환 문제 DP
# 동전 종류가 주어지고, 종류는 무한으로 사용 가능 ==> 냅색 알고리즘


# dp를 m+1까지 잡는다 최대 맥스
import sys
# sys.stdin=open("input.txt","r")

n=int(input())
a=list(map(int,input().split()))
m=int(input())

# 동전의 최소 개수를 dp로 잡는다
# 예를들어 1원은 1
# 2원은 1,1 or 2원 ==> 그 중에 최소 1개
# 3원은 1,2 or 1,1,1 ==> 그 중에 최소 2개


# 냅색 알고리즘
# dp[j]=dp[j-w]+v
# 여기가 중요 ==> 최소값을 구해야되므로 각 인자는 501로 맞춰준다
dp=[501]*(m+1)

# i는 1부터~ 16까지
# dp[1]=min(dp[1],dp[1-1]+1)
# dp[1]은 0 dp[0]+1은 1 둘중 최솟값은 dp[1] =0

# dp[2]=dp[2],dp[1]+1
# dp[2]는 0 dp[1]+1은 2 ==>

for i in a:
    dp[i]=1
# print("dp",dp)
for i in a:
    for j in range(i,m+1):
        # dp[j]는 현재 값, dp[j-i] +1(동전사용) 중 작은것을 선택
        dp[j]=min(dp[j],dp[j-i]+1)

# print("dp2",dp)
print(dp[m])


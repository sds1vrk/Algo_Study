# 네트워크 선 자르기 (Bottom up)
# Bottom -UP : 앞에 구해 놓은 해를 이용해서 점차 큰 해를 구하는 것
# 문제를 쪼갠다음에 작은 답을 찾고 큰 답을 찾는 것
# for문을 이용

import sys
sys.stdin=open("input.txt","r")

n=int(input())

dp=[0]*(n+1)
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])

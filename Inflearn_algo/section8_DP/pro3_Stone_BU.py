# 바텀 업 방식
# 돌다리 건너기
# 한칸 또는 두칸식만 이동 가능
# 돌다리 건너는 방법

import sys
sys.stdin=open("input.txt","r")

n=int(input())

# 마지막 돌다리에서 2칸으로 건너는 경우
# 마지막 돌다리에서 1칸으로 건너는 경우
# 점화식 : dp(n)=dp(n-1)+dp(n-2)


# 여기서는 한칸 더 추가해야됨, 이유는 n+1을 구해야됨, 7까지 건너는 경우의 수 이므로 n+1로해서
# 1칸 더 건너는 경우의 수를 구해야됨
dp=[0]*(n+2)

dp[1]=1
dp[2]=2

for i in range(3,n+2):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n+1])
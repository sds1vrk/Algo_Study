# 최대 선 연결하기
# 10개가 숫자가 주어졌을때 평행하지 않도록 연결하는 방법
import sys
# sys.stdin=open("3190.txt")

n=int(input())
a=list(map(int,input().split()))

# 평행하는 방법은 왼쪽은 오름차순, 오른쪽은 랜덤으로 주어짐
# 따라서 a라는 값을 오름차순으로 선택해서 가장 긴것을 선택하는 것과 동일
# 즉 LIC 문제와 동일,

# DP와 동일하게 하기 위해 0,0 삽입
a.insert(0,0)
dp=[0]*(n+1)

dp[1]=1
for i in range(1,n+1):
    max_val=0
    for j in range(i-1,-1,-1):
        if a[i]>a[j] and max_val<dp[j]:
            max_val=dp[j]

    dp[i]=max_val+1

print(max(dp))
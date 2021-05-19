# 가방문제 (냅색 알고리즘)

# 최대 가치 구하기 DP
# 냅색 알고리즘
# 배낭문제는 조합 최적화의 유명한 문제,
# 배낭에 담을수 있는 무게의 최대값이 정해져있고, 일정 가치와 무게가 있는 짐들을 배낭에 넣을때, 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제

import sys
# sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
# 최대 무게 +1 인덱스 값 구하기 위해서
# 여기서 dp는 가방에 들어갈 최대 가치
dp=[0]*(m+1)
for i in range(n):
    w,v=map(int,input().split())

    for j in range(w,m+1):
        dp[j]=max(dp[j],dp[j-w]+v)

print(dp[m])





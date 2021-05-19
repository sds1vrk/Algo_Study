# LCS (Longest Increasing Subsequence)
# 최대 부분 증가 수열
# DP로 구하기
# 2,7,5,8,6,4,7,12,3
# ==> 2,5,6,7,12 : 길이가 5인것이 최대 부분 증가 수열
# 숫자의 위치는 바꾸면 안됨 ==> DP

# 찾은 숫자에서 바로 전까지 검색 후 자기보다 작은 수 찾은 후 +1
# 마지막 길이가 2 ==> 1
# 마지막 길이가 7 ==> 27, 7 ==> 이중에 큰것은 2
# 마지막 길이가 5 ==> 25, 5 ==> 이중에 큰것은 2
# 마지막 길이가 8 ==> 18, 278, 258 ==> 이중에 큰것은 3
# 마지막 길이가 6 ==> 256 ==> 이중에 큰것은 3
# 마지막 길이가 4 ==> 14 ==> 2
# 마지막 길이가 7 ==> 2567 ==> 이중에 큰것은 4
# 마지마 길이가 12 ==> 256712, 25612,27812, 25812, ==> 이중에 큰것은 5
# 마지막 길이가 3 ==> 13 ==> 2

# ==> DP에 각 1~n+1까지 저장

import sys
# sys.stdin=open("input.txt","r")

n=int(input())
a=list(map(int,input().split()))
# DP랑 맞추기 위해 0인덱스 넣음
a.insert(0,0)

# DP 저장
dp=[0]*(n+1)
# 처음 길이는 1이기 때문에 1
dp[1]=1

for i in range(1,n+1):
    max_val = 0
    for j in range(i-1,-1,-1):
        # 마지막 인덱스 전까지 검사
        if a[i]>a[j] and max_val<dp[j]:
            # 제일 큰 DP 찾기
            max_val=dp[j]

    # DP는 현재 최장 길이보다 +1
    dp[i]=max_val+1

print(max(dp))








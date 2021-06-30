# 최대 점수 구하기 (냅색 알고리즘)

import sys
from itertools import combinations
from itertools import permutations
# sys.stdin=open("3190.txt")

# a=[1,2,3]
# print(list(permutations(a,2)))
n,m=map(int,input().split())
# 최대 20시간까지 구하는 dp
dp=[0]*(m+1)
# 냅색 알고리즘
# dp[j]=dp[j-w]+t

# 한 유형당 한개만 풀 수 있다.
# 이 조건떄문에 중복이 안되는것 같음
# 조건을 추가해서 푼 문제는 못 풀게 해야됨
# 이 조건의 핵심은 ==> 문제를 뒤에서 서부터 해결함
# 앞에서부터 하면 중복된것을 사용할수 있기 때문에 뒤에서부터 하면 중복 제거
# 앞에서부터 하면 차례대로 채워지기 때문에 중복된게 들어감, 하지만 뒤에서부터 하면 뒤부터 채워지기 때문에 앞에꺼를 갱신 안하기 떄문에 중복을 해결 할 수 있다.
# m 20
# w t
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

for i in range(n):
    w,t=map(int,input().split())
    for j in range(m,t-1,-1):
        dp[j]=max(dp[j],dp[j-t]+w)

print(dp[m])
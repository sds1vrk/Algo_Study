# 중복허용하는 냅색 알고리즘
# 구할려는 것은 보석의 최대가치

import sys
sys.stdion=open("input.txt","r")

n,m=map(int,input().split())

# 가방을 하나씩 담을때마다 채워지는
dp=[0]*n


for i in range(n):
    w,v=map(int,input().split())


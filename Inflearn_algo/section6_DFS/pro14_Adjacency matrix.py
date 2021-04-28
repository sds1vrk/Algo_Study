# 인접행렬로 그래프 나타내기

import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

# n*n 0으로 초기화
g=[[0]*(n) for _ in range(n)]

# print(g)

# 간선 개수에 따른 거리 비용 저장하기
for i in range(m):
    a,b,c=map(int,input().split())
    g[a-1][b-1]=c

print(g)

#송아지 찾기
# BFS
from collections import deque
import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
# print("n,m",n,m)
count=0
dx=[1,-1,5]

def bfs(l):
    global count
    queue=deque([l])

    while queue:

        k=queue.popleft()
        mm=dis[k]

        if k==m:
            break

        for i in range(3):
            nx = k + dx[i]
            if dis[nx]==-1:
                queue.append(nx)
                dis[nx]=mm+1


# 최대 갈수 있는 범위
dis=[-1]*(100000+1)
dis[n]=0
bfs(n)
print(dis[m])

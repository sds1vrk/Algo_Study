# 아일랜드 BFS
from collections import deque
import sys
sys.stdin=open("input.txt","r")


n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]


# 시작 위치 찾기
start=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            start.append((i,j))

print(start)
(0,0),(0,1)
(1,0),(1,1)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

result=[]
for x,y in start:
    queue=deque()
    queue.append((x,y))

    count=0



    while queue:
        x,y=queue.popleft()

        if a[x][y] == 1:
            a[x][y] = 0
            count += 1

        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                a[nx][ny]=0
                count+=1

    if count!=0:
        result.append(count)

print(len(result))
print("result",result)












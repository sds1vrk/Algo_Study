# BFS로 미로 풀기
# 최단거리
# 내가 푼 방식 : ch의 방문 거리를 넣어줌
# 넣어주고 마지막에 [6][6]이 뭔지 찾음, 먼저 들어갔기 때문에 다른수가 못들어감 ==> 최단 거리 수가 들어가있음

import sys
from collections import deque
sys.stdin=open("input.txt","r")

a=[list(map(int,input().split())) for _i in range(7)]
# 동남서북
dx=[1,0,0,-1]
dy=[0,1,-1,0]

ch=[[0]*7 for _ in range(7)]
# print(ch)

q=deque()
q.append((0,0))
ch[0][0]=0

while q:
    size=len(q)

    x, y = q.popleft()

    for i in range(size):
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]

            # print(nx,ny)
            if nx<0 or nx>6 or ny<0 or ny>6:
                # print("here")
                continue


            elif a[nx][ny]==0 and ch[nx][ny]==0:
                # 방문하지 않았으면 방문처리, 이때 거리를 넣어준다
                # 이미 방문처리되서 나머지 것들이 못들어온다
                # ch[nx][ny]=1
                ch[nx][ny] = ch[x][y]+1
                # print("here")
                q.append((nx,ny))


if ch[6][6]==0:
    print(-1)

else :
    print(ch[6][6])


# print(res)








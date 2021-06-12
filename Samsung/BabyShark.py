import sys
from collections import deque
import math
# sys.stdin=open("babyshark.txt","r")

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

# print(board)
size=2

x,y=0,0
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            x,y=i,j
            # 이 부분떄문에 1시간 소요됨
            # 위치값을 찾고 초기값을 0으로 만들어야지 이 쪽으로 이동 가능
            board[i][j]=0

# (0,0) (0,1)
# (1,0) (1,1)
dx=[-1,0,1,0]
dy=[0,1,0,-1]


# 상어에서 떨어진 음식의 최단 거리 계산 (bfs)
def bfs(x,y,size):
    q=deque()
    q.append((x,y))
    dist=[[-1]*n for _ in range(n)]
    dist[x][y] = 0
    # print(dist)
    # print(x,y)

    while q:
        x,y=q.popleft()
        # print("x,y",x,y)
        # board[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and board[nx][ny]<=size and dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))

    # print("dist",dist)
    return dist


def find(dist,size):
    min_value=math.inf
    fx,fy=0,0
    # print(dist)

    for i in range(n):
        for j in range(n):
            if 0<board[i][j]<size and dist[i][j]!=-1 :

                # 여기서 중요한건 dist를 이용해 음식의 최단 거리를 구한다.
                if min_value>dist[i][j]:
                    min_value=dist[i][j]
                    fx,fy=i,j
                    # print("minvalue",min_value)


    if min_value==math.inf:
        return None
    else :
        return fx,fy,min_value


# bb=bfs(x,y,size)
# print(find(bb,size))


answer=0
cnt=0
while True:

    # print("size",size,x,y)

    dist=bfs(x,y,size)
    # print(dist)
    # 이 거리 계산에 대한 것을 먹이 찾는 곳에 넣음
    value=find(dist,size)


    # print(dist)

    if value==None:
        print(answer)
        break

    else :
        # 음식의 위치로 이동
        fx, fy, min_value = value[0], value[1], value[2]
        x,y=fx,fy
        answer+=min_value

        # print("ans",answer,x,y)

        cnt+=1
        board[x][y]=0
        # print(board)

        # 상어 크기 증가
        if cnt>=size:
            size+=1
            cnt=0














































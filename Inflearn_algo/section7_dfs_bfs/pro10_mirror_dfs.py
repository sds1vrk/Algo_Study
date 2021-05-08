# 미로 탐색 DFS로
# 갈수 있는 총 가지수 구하기

import sys
sys.stdin=open("input.txt","r")

# 행, 열
a=[list(map(int,input().split())) for _ in range(7)]

cnt=0
a[0][0]=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1

    else :
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<=6 and 0<=ny<=6 and a[nx][ny]==0:
                a[nx][ny]=1
                dfs(nx,ny)
                # 빽해서 바로 전으로 되돌갈때는 취소
                a[nx][ny]=0


dfs(0,0)
print(cnt)
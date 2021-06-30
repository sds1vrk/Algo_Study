
# 토마토 BFS로 풀기

# 문제 풀이 방법
# 1. 토마토가 이슈 1에 걸리는 경우 제외하고 시작
# 2. 익은 토마토의 위치 찾고 queue에 넣기
# 3. 익은 토마토 위치를 바탕으로 큐에 size를 바탕으로 for문 돌리기
#    - 처음에는 큐에 2개가 들어감
#    - 그리고 큐가 다 돌고 나면 1일 지난 후에 토마토 모습을 알 수 있음
#    - 이때 for문 써서 큐 돌려야됨 ==> 이유는 aplleTree_BFS와 동일함 ==> 한번 돌렸을때 맵의 상태변화를 갱신하기 때문임


import sys
from collections import deque

# sys.stdin=open("3190.txt","r")
m,n=map(int,input().split())

def print_graph(a):
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()

# n: 행, m: 열
a=[list(map(int,input().split())) for _ in range(n)]

# print(a)
# print_graph(a)
queue=deque()
# (0,0),(0,1)
# (1,0),(1,1)
dx=[-1,0,1,0]
dy=[0,1,0,-1]


# 익은 토마토 시작점 넣기
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            queue.append((i,j))

# print(queue)
# ch ->토마토가 익은 날짜를 ch에 기록 함
# a는 0이 나오는 경우도 있기 때문에 이건 토마토가 다 익지 못하는 경우를 체크해야됨
ch=[[0]*m for _ in range(n)]
# print(ch)
# print(a)

while queue:
    x,y=queue.popleft()
    # ch[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and a[nx][ny]==0 and ch[nx][ny]==0:
            a[nx][ny]=1
            ch[nx][ny]=ch[x][y]+1
            queue.append((nx,ny))
# print(a)
# print(ch)

# 모든 BFS를 다 돌았는데 0이 존재하는 경우는 익지 못하는 경우이므로 ==> -1리턴
flag=0
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            flag=1

if flag==1:
    print(-1)

else :
    result=0
    for i in range(n):
        for j in range(m):
            if ch[i][j]>=result:
                result=ch[i][j]

    print(result)


















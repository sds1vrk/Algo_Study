# 좀비 바이러스 문제
import sys
from collections import deque
import copy
# sys.stdin=open("zombie.txt","r")
n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]
temp=[[0]*m  for _ in range(n)]
cnt=0
# (0,0) (0,1)
# (1,0), (1,1)
# 위 오 아래 왼
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# print("ori",board)

def virus_Check(temp):
    queue=deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j]==2:
                queue.append((i,j))

    # print(board)

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if 0<=nx<n and 0<=ny<m and temp[nx][ny]==0:
                temp[nx][ny]=2
                queue.append((nx,ny))
    # 0 Check
    cnt=0
    # for i in temp:
    #     cnt+=i.count(0)
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                cnt+=1

    return cnt



# 지금 문제점은 사다리를 건설한 뒤 사다리가 그냥 그대로
# 바이러스도 그냥 그대로 ==> 바이러스로 보낼떄는 deepcopy를 이용해야 될듯


max_value=0
def dfs(l):
    global max_value
    if l==3:
        cnt=virus_Check(copy.deepcopy(board))
        # temp=board[:]
        # for i in range(n):
        #     for j in range(m):
        #         temp[i][j]=board[i][j]
        # print("temp",temp)

        # cnt=virus_Check(temp)
        if max_value<cnt:
            max_value=cnt

        return

    else :
        for i in range(n):
            for j in range(m):
                if board[i][j]==0:
                    board[i][j]=1
                    # l+=1
                    dfs(l+1)
                    board[i][j]=0
                    # l-=1


dfs(0)
print(max_value)


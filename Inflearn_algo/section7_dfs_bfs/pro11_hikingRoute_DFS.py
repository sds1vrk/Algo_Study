# 등산경로
# 해결방법
# 1. 2차원 행렬 그리기
# 2. 최대값, 최소값 찾기
# 3. 최대값, 최소값 좌표 찾기
# 4. 총 가지수니깐 DFS로 하기
# 5. 도착한다음에는 반드시 방문 체크 풀어주기
# 6. 조건을 확인하여 DFS돌리기


import sys
# sys.stdin=open("input.txt","r")

n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]

# print(a)

max_val=-1
min_val=9999


for i in a:
    maxVal=max(i)
    minVal=min(i)
    if min_val>minVal:
        min_val=minVal

    if maxVal>max_val:
        max_val=maxVal

# print(min_val,max_val)

# 최소값, 최대값 좌표 찾기
min_x,min_y=0,0
max_x,max_y=0,0
for i in range(n):
    for j in range(n):
        if min_val==a[i][j]:
            min_x,min_y=i,j
            break

        if max_val==a[i][j]:
            max_x,max_y=i,j
            break

# print(min_x,min_y)
# print(max_x,max_y)

# (0,0),(0,1),(0,2)
# (1,0),(1,1),(1,2)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 방문 여부 체크
ch=[[0]*n for _ in range(n)]
# print(ch)
ch[min_x][min_y]=1

count=0
def dfs(x,y):
    global count
    if x==max_x and y==max_y:
        count+=1

    else :
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 조건 잘 읽기
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and a[nx][ny]>a[x][y]:
                ch[nx][ny]=1
                dfs(nx,ny)
                ch[nx][ny]=0

dfs(min_x,min_y)

print(count)



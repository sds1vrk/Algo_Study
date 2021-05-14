# 아일랜드 BFS
# 내 풀이 방식
# 시작 위치를 미리 저장
# 시작위치에서 하나씩 빼서 그 시작을 중심으로 BFS 돌리기
# 연결될때마다 count1씩 증가 후 result 리스트에 저장힉
# 주의점은 처음에 들어온 값을 방문처리 해야됨
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

# print(start)
(0,0),(0,1)
(1,0),(1,1)
# + 대각선
dx=[-1,0,1,0,1,1,-1,-1]
dy=[0,1,0,-1,1,-1,1,-1]

result=[]
for x,y in start:
    queue=deque()
    queue.append((x,y))

    count=0

    if a[x][y] == 1:
        a[x][y] = 0
        # count += 1


        while queue:
            x,y=queue.popleft()


            for i in range(8):
                nx=dx[i]+x
                ny=dy[i]+y

                if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                    a[nx][ny]=0
                    queue.append((nx,ny))
        count+=1

        if count!=0:
            result.append(count)

print(len(result))
# print("result",result)












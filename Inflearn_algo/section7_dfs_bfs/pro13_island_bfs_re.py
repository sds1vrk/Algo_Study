# 아일랜드 BFS
# 인강 풀이 방식
# 1인 지점부터 바로 큐에 넣기
# 큐에 넣은 후 방문 처리
# 그리고 그 if문 안에서 While문 돌리기 ==> 이러면 cnt 를 1번만 작성해도 됨



from collections import deque
import sys
# sys.stdin=open("input.txt","r")


n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]


# print(start)
# (0,0),(0,1)
# (1,0),(1,1)
# + 대각선
dx=[-1,0,1,0,1,1,-1,-1]
dy=[0,1,0,-1,1,-1,1,-1]

queue=deque()
cnt=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            queue.append((i,j))
            a[i][j]=0

            while queue:
                x,y=queue.popleft()
                for k in range(8):
                    nx=x+dx[k]
                    ny=y+dy[k]

                    if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                        a[nx][ny]=0
                        queue.append((nx,ny))

            cnt+=1

print(cnt)














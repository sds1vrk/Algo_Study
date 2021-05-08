# BFS로 사과나무 풀기

import sys
from collections import deque
sys.stdin=open("input.txt","r")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]


# BFS로 풀때는 중심점부터 시작하여 뻗어나감
k=n//2

# 시계방향
dx=[-1,0,1,0]
dy=[0,1,0,-1]


ch=[[0]*n for i in range(n)]
# print(ch)
ch[n//2][n//2]=1
hap=0
hap+=a[n//2][n//2]
q=deque()
q.append((n//2,n//2))
l=0
while True:
    if l==n//2:
        break

    else :


        # 여기가 핵심,
        # 큐가 돌리는것을 확인하기 위해 큐의 개수를 확인
        # 탐색될 큐만큼 돌리고 안에서 4방향 진행
        size=len(q)

        print(size)

        for i in range(size):
            x, y = q.popleft()

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue

                if ch[nx][ny]==0:
                    q.append((nx,ny))
                    # print(a[nx][ny],end=" ")
                    hap+=a[nx][ny]
                    ch[nx][ny]=1
            # print()
        # level 증가 시점은 다 빠져나가고 레벨 증가
        l+=1

print(hap)







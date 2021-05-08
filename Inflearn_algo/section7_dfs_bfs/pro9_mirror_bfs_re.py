# BFS로 미로 풀기
# 최단거리
# 강의 : 내가 푼것과는 다르게 맵을 1로 하여 지나간것을 1처리하여 막음
# ch에는 거리값이 들어감

# 큰 차이는 없고, 맵을 막냐 안막냐 차이

import sys
from collections import deque
sys.stdin=open("input.txt","r")

a=[list(map(int,input().split())) for _i in range(7)]
# 동남서북
dx=[1,0,0,-1]
dy=[0,1,-1,0]

ch=[[0]*7 for _ in range(7)]

print("a",a)

q=deque()
q.append((0,0))
# 현재 위치 벽으로 만듬
a[0][0]=1
res=0

while q:

    x, y = q.popleft()

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if 0<=nx<=6 and 0<=ny<=6 and a[nx][ny]==0:
            # 다시 못오게 벽으로 만듬
            a[nx][ny]=1
            ch[nx][ny]=ch[x][y]+1
            q.append((nx, ny))


    # res += 1

if ch[6][6]==0:
    print(-1)

else :
    print(ch[6][6])


# print(res)








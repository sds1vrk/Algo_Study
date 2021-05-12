# 토마토 BFS로 풀기
import sys
from collections import deque

sys.stdin=open("input.txt","r")
m,n=map(int,input().split())

def print_graph(a):
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()

# n: 행, m: 열
a=[list(map(int,input().split())) for _ in range(n)]

# print(a)
print_graph(a)
queue=deque()
# (0,0),(0,1)
# (1,0),(1,1)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

count=0
# while True:


    # count+=1

ch=[[0]*m for _ in range(n)]
print("ch",ch)
cnt=0

# 큐에 먼저 익은 토마토 위치 찾기
start_point=[]
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            # start_point.append((i,j))
            queue.append((i,j))

# print("x,y",start_point)
print("queue",queue)
count=0
size=len(queue)

for i in range(size):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                queue.append((nx, ny))
                a[nx][ny] = 1

    print(queue)

    count+=1

print(count)

print_graph(a)









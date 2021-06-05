from collections import deque

import sys
sys.stdin=open("3190.txt", "r")

n=int(input())
m=int(input())

a=[[0]*n for _ in range(n)]

# 사과는 1, 그외에는 0으로 표현
for i in range(m):
    x,y=map(int,input().split())
    a[x-1][y-1]=1

print("a",a)

# 방향 변경 정보 저장
changes=dict()
rot=int(input())
for _ in range(rot):
    dic_a,dic_b=input().split()
    changes[int(dic_a)]=dic_b
print(changes)

# 뱀 위치
snake=deque()

# 북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 처음방향 : 동
d=1
time=0
nx,ny=0,0

# 방향 전환
def change_direction(direct):
    global d
    if direct=="D":
        d=(d+1)%4

    else :
        d=(d-1)%4
    return d

print("nx,ny",nx,ny)

while True:
    time+=1
    nx+=dx[d]
    ny+=dy[d]



    # print("nx,ny",nx,ny,a[nx][ny])


    # 방향 전환
    # 만약 시간이 안에 포함되어 있으면 방향 전환
    if time in changes.keys():
        d=change_direction(changes[time])

    # 벗어나지 않은경우
    if 0<=nx and nx<n and 0<=ny and ny<n :
        # 새로운 좌표가 몸통에 있는 경우
        if [nx,ny] in snake:
            break

        # 다음 위치에 사과가 있는 경우 ==> 길이 1증가
        if a[nx][ny]==1:
            a[nx][ny]=0
            snake.append([nx,ny])

        else :
            snake.append([nx,ny])
            snake.popleft()

    else :
        # 벗어난 경우 break
        break

print(time)










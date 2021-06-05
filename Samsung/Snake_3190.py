# 3190 뱀 문제

import sys
sys.stdin=open("3190.txt","r")

n=int(input())
m=int(input())

a=[[0]*n for _ in range(n)]

# 사과는 1, 그외에는 0으로 표현
for i in range(m):
    x,y=map(int,input().split())
    a[x-1][y-1]=1

# 회전 저장
# 시간 뒤에
# D는 오른쪽으로 회전, L은 왼쪽으로 90도 회전
rot=int(input())
rotate=[]
for i in range(rot):
    rotate.append(list(input().split()))

print(a)
print(rotate)


# 머리 위치
# 꼬리 위치
# 몸통 위치

def rota(val,k):
    # 현재 val
    if k=="D":

        print("test")


time=0
head_x,head_y=0,0
tail_x,tail_y=0,0
sna_len=1
val="R"
head=[]
tail=[]
while True:
    time+=1
    # 길이

    # 행열 (x,y)
    # 이동 방향


    # 만약 머리가 가는 위치에 사과가 있으면 길이 1 증가
    if a[head_x][head_y]==1:
        sna_len+=1
        a[head_x][head_y]=0

    else :

        if val == "R":
            head_y += 1
            tail_y +=1
            if sna_len > 1:
                tail_y -= 1

        elif val == "D":
            head_x += 1
            if sna_len > 1:
                tail_x += 1

        elif val == "L":
            head_y -= 1
            if sna_len > 1:
                tail_y -= 1





    # 회전 검사
    for i in range(len(rotate)):
        if rotate[i][0]==time:
            # val=rota(val,rotate[i][1])
            val=rotate[i][1]
            # 뽑고 해당 rotate 삭제
            rotate.pop(0)

    # 벽을 뚫고가면 게임 종료
    if head_x>=n or head_x<0 and head_y>=n or head_y<0:
        break

    # 머리가 몸통에 부딪히면 게임 종료


print("time",time)























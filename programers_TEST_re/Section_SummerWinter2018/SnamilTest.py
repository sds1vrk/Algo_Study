# 삼각 달팽이 만들기

# n=3일때
# 0
# 5 1
# 4 3 2

# n=4일때
# 0
# 8 1
# 7 9 2
# 6 5 4 3


import sys
sys.stdin=open("snail.txt","r")
n=int(input())

# 주어진 리스트 만들기 (주어진 리스트 개수대로 초기화하기)
# 1행에는 1개, 2행에는 2개, 3행에는 3개 ...
a=[[0]*i for i in range(1,n+1)]
print(a)

# n에 의한 회전 수 입력
# n이 1~3일때까지는 회전1번, n이 4~6일떄까지는 회전 2번, n이 7~9번까지는 회전 3번

rotate=((n-1)//3)+1
# print(rot)

x,y=-1,-1
k=0
t=0

def check(k):
    if k>=10:
        k=k%10
        return k



for rot in range(1,rotate+1):
    #  오른쪽 대각선
    for _ in range(n-t):
        x+=1
        y+=1
        a[x][y]=k
        k+=1

        if k>=10:
            k=k%10


    # 왼쪽으로 이동
    for _ in range(n-t-1):
        y-=1
        a[x][y]=k
        k+=1
        if k>=10:
            k=k%10


    # 위로 이동
    for _ in range(n-t-2):
        x-=1
        a[x][y]=k
        k+=1
        if k>=10:
            k=k%10

    # print(x,y)
    t+=3








print(a)









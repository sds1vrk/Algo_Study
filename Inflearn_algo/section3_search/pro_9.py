# 봉우리 개수 차직
# 상하좌우 검색해서 자기보다 작으면 break, 다 통과되면 result에 추가

import sys
# sys.stdin=open("3190.txt","r")

n=int(input())

a=[[0]*(n+2) for _ in range(n+2)]
# print(a)

# 여기 안에 격자 값 계산하기
b=[list(map(int,input().split())) for _ in range(n)]
# print(b)

# 격자에 넣기
for i in range(1,n+1):
    for j in range(1,n+1):
        a[i][j]=b[i-1][j-1]

# print(a)


# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=[]
size=len(a)
# print(size)
for i in range(1,size-1):
    for j in range(1,size-1):
        su=a[i][j]
        # 상하좌우 확인

        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]

            if su<=a[nx][ny]:
                break
        else :
            result.append(su)

# print(result)
print(len(result))



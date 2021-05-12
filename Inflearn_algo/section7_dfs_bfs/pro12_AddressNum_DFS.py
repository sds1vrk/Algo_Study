# 주소번지 DFS로 풀기
# 강의 - 어디가 1인지 시작점을 몰랐었는데, 2중 for문 돌면서 처음 1이 걸리는것을 시작점으로 둔다
# 또한, 멈추는 구간은 더이상 갈곳이 없으면 stack이 더이상 진행안하고 끝나는 것을 이용
# 이때, 한번 방문했던 곳은 map에서 0으로 바꿔줘서 더이상 방문못하게 한다

import sys
sys.stdin=open("input.txt","r")

n=int(input())
a=list(list(map(int,input())) for _ in range(n))

print(a)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt
    cnt+=1
    a[x][y]=0

    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y

        if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
            a[nx][ny]=0
            dfs(nx,ny)


result=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            cnt=0
            dfs(i,j)
            # 위에서 cnt값이 갱신되서 돌아오기 때문에 그 값을 넣어준다
            result.append(cnt)

print(result)
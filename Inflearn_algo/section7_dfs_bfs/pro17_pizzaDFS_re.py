# DFS 조합으로 풀기

import sys
sys.stdin=open("input.txt","r")
n,m=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

house=[]
pizza=[]

for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            house.append((i,j))

        elif a[i][j]==2:
            pizza.append((i,j))


print("house",house)
print("pizza",pizza)
# 피자집 선택 갯수
pizza_ch=[0]*m

# DFS 조합
def dfs(l,s):
    global res
    if l==m:
        # for i in pizza_ch:
            # print(i,end=" ")

        sum=0
        for x1, y1 in house:
            dis = 2147000
            # print("x1,y1", x1, y1)
            # 각 집 부터 피자 집 만큼 개수 돌음
            for p in pizza_ch:
                x2=pizza[p][0]
                y2=pizza[p][1]
                dis=min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis

        if sum<res:
            res=sum


    else :
        # 피자집 조합 돌리기 (총 피자집의 개수)
        for i in range(s,len(pizza)):
            # 여기서 중요한건 레벨에 넣는거임
            pizza_ch[l]=i
            # 레벨 증가시키고, 다음 for문부터 시작이기 때문에 시작위치 i+1 증가시키기
            dfs(l+1,i+1)
            # pizza_ch[i]=0
res=2147000
dfs(0,0)
print(res)















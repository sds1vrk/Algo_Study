# 안전영역 BFS로 풀기
# 내 풀이 방법
# 맵 중에서 최소값과 최대값 찾기
# 최소값부터~ 최대값+1 까지 for문 돌리기
# 원본 맵을 이용해야 하기 때문에 copy.deepcopy(a)로 맵 복사하고 이걸 이용하기


from collections import deque
import sys
import copy
# sys.stdin=open("3190.txt","r")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

# (0,0)(0,1)
# (1,0),(1,1)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 최소값~최대값 찾기
min_val=101
max_val=0

for i in a:
    maxVal=max(i)
    minVal=min(i)

    if maxVal>max_val:
        max_val=maxVal

    if minVal<min_val:
        min_val=minVal

# print(max_val,min_val)
queue=deque()
result=[]
for i in range(min_val,max_val+1):

    # copy_a=a[:]
    copy_a = copy.deepcopy(a)
    # print(copy_a)
    cnt=0

    for j in range(n):
        for k in range(n):
            if copy_a[j][k]>i:
                queue.append((j,k))
                copy_a[j][k]=0

                cnt+=1

                while queue:
                    x,y=queue.popleft()

                    for l in range(4):
                        nx=x+dx[l]
                        ny=y+dy[l]

                        if 0<=nx<n and 0<=ny<n and copy_a[nx][ny]>i:
                            copy_a[nx][ny]=0
                            queue.append((nx,ny))

                result.append(cnt)

print(max(result))
















# 단지번호
# 해결방법
# 1. 그래프
# 2. DFS는 종료 시점 모르겠어서 BFS로 풀음
# 3. 행렬 별로 시작 위치 찾음 ==> 좌표로 저장하여 리스트에 넣음
# 4. 저장한 좌표를 하나씩 for문 돌리며 큐에 넣고 나서 조건에 맞으면 count+=1헤주기
# 5. 중요한건 처음 뺀게 1인 경우도 있을수 있음 따라서 만약 처음 빠진게 1이면 count+=1 (이거 찾는데 시간 걸림)
# 6. 오름차순 및 출력

from collections import deque
import sys
# sys.stdin=open("input.txt","r")

n=int(input())
a=[list(map(int,input())) for _ in range(n)]

# print(a)

# (0,0)(0,1),(0,2)
# (1,0),(1,1),(1,2)

dx=[-1,0,1,0]
dy=[0,1,0,-1]


# 시작 위치 찾기
queue=deque()
start_point=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            start_point.append((i,j))
            # queue.append((i,j))


# print(queue)
# print("start",start_point)
result=[]
for x,y in start_point:
    # print("x,y",x,y)
    queue.append((x,y))

    count=0

    # 첫번째 들어온거 막기 위해 이거 해주기
    if a[x][y] == 1:
        a[x][y] = 0
        count += 1

    while queue:
        x, y = queue.popleft()
        # count+=1

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 1:
                a[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    if count != 0:
        result.append(count)





result.sort()
print(len(result))

for i in result:
    print(i)











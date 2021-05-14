# 사다리 타기
# DFS로 풀기
# 우선순위는 왼쪽 or 오른쪽 -> 아래임
# DFS 종료 시점은 행(x)가 9에 도착하면 종료
# 맵을 바꾸면 안되기 때문에 ch사용
# DFS로 갔던 곳은 다시 ch =0으로 풀기 ==> 다른곳에서 방문하기 위해서
# 마지막으로 아래로 갔을때 도착지는 0이 아닌 수가 들어가야됨 (1이 아니라 다른 수이기 떄문에)

import sys
# sys.stdin=open("input.txt","r")

a=[list(map(int,input().split())) for _ in range(10)]

# print(a)
# 사다리에 위로 가는건 없음, 아래 -> 왼 or 오
# (0,0)(0,1)
# (1,0)(1,1)
dx=[1,0,0]
dy=[0,-1,1]

ch=[[0]*10 for _ in range(10)]



def dfs(col,x,y):

    # print(x,y)

    # 종료 시점 추가
    # 행이 끝까지 도달하면 종료
    if x==9:
        # print("test")
        if a[x][y] == 2:
            print(col)
            sys.exit()

        else :
            return

    else :

        # 아래로 먼저 가다가 왼 or 오른쪽이 있으면 타기
        nx=x+dx[0]
        ny=y+dy[0]

        # 왼 or 오른쪽이 있는 경우 사다리 타기
        left_x, left_y =x+dx[1], y+ dy[1]
        right_x, right_y = x+dx[2], y+ dy[2]


        if 0 <= left_x < 10 and 0 <= left_y < 10 and ch[left_x][left_y] == 0 and a[left_x][left_y] == 1:
                # 이동하기
                # print("l_x,l_y",left_x, left_y)

            ch[left_x][left_y] = 1
            dfs(col, left_x, left_y)
            ch[left_x][left_y] = 0

        elif 0 <= right_x < 10 and 0 <= right_y < 10 and ch[right_x][right_y] == 0 and a[right_x][right_y] == 1:
                # 이동하기

                # print("r_x,r_y",right_x, right_y)
            ch[right_x][right_y] = 1
            dfs(col, right_x, right_y)
            ch[right_x][right_y] = 0

        elif 0 <= nx < 10 and 0 <= ny < 10 and ch[nx][ny] == 0 and a[nx][ny] != 0:
            # print(nx, ny)
            ch[nx][ny] = 1
            dfs(col, nx, ny)
            ch[nx][ny] = 0














        # for i in range(3):
        #     nx=x+dx[i]
        #     ny=y+dy[i]

            # if 0<=nx<10 and 0<=ny<10 and ch[nx][ny]==0 and a[nx][ny]==1:
            #     ch[nx][ny]=1
            #     print(nx,ny)
            #     dfs(col,nx,ny)
                # ch[nx][ny]=0


for j in range(10):
    if a[0][j]==1:
        dfs(j,0,j)




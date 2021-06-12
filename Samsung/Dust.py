# 미세먼지
import sys
import copy
# sys.stdin=open("dust.txt","r")
r,c,t=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(r)]

# print(board)


time=0




# (0,0) (0,1)
# (1,0) (1,1)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

from collections import deque

def printMatrix(mat):
    for row in mat:
        print(row)

# 먼지 확산
def dust_move(board):
    # copy_board = copy.deepcopy(board)
    copy_board=[[0]*c for _ in range(r)]
    # printMatrix(copy_board)

    queue=deque()
    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                queue.append((i,j))

    # 먼지들 위치들을 다 저장
    while queue:
        x,y=queue.popleft()

        # 4방향 이동
        cnt=0
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if 0<=nx<r and 0<=ny<c and board[nx][ny]!=-1:
                temp=int(board[x][y]/5)
                # temp=board[x][y]//5
                # print("temp",temp)
                cnt+=1
                # print("nx,ny",nx,ny)
                copy_board[nx][ny]=copy_board[nx][ny]+temp
                # print(board)

        board[x][y]=board[x][y]-(temp*cnt)

    for i in range(r):
        for j in range(c):
            board[i][j] += copy_board[i][j]

    # printMatrix(board)
    return board

def cleaner():
    # 미세먼지 위치 찾고, 첫번째꺼는 시계방향으로 먼지를 하나씩 이동 시킴
    temp_q=deque()
    for i in range(r):
        for j in range(c):
            if board[i][j]==-1:
                temp_q.append((i,j))

    def time_move(row,col):
    #     left->right
        col=1
        temp=board[row][1]
        board[row][1]=0
        for i in range(2,c):
            # print("here1")
            curr=board[row][i]
            board[row][i]=temp
            temp=curr

        # printMatrix(board)
        # print()

    # (0,0) (0,1)
    # (1,0) (1,1)
    # bottom -> top
    #     print("temp",temp)
        for i in range(row-1,-1,-1):
            # print("here2")
            curr=board[i][c-1]
            board[i][c-1]=temp
            temp=curr

        # printMatrix(board)
        # print()

        # print(temp)

        # right->left
        # c-1 -> -1 -1

        for i in range(c-2,-1,-1):
            curr=board[0][i]
            # print("curr",curr)
            board[0][i]=temp
            temp=curr

        # printMatrix(board)
        # print()


    # top->bottom
        for i in range(0,row-1):
            # print("here4")
            curr=board[i][0]
            board[i][0]=temp
            temp=curr


        # printMatrix(board)


    def reverse_move(row,col):
        #     left->right
        col = 1
        temp = board[row][1]
        board[row][1] = 0

        # printMatrix(board)
        # print("temp",temp)

        for i in range(2, c):
            # print("here1")
            curr = board[row][i]
            board[row][i] = temp
            temp = curr

        # printMatrix(board)

        # top -> bottom
        for i in range(row+1, r):
            # print("here2")
            curr = board[i][c - 1]
            board[i][c - 1] = temp
            temp = curr

        # printMatrix(board)

        #   right-> left
        # print("temp",temp)
        for i in range(c-2, -1, -1):
            # print("here3")
            # print("here")
            curr = board[r-1][i]
            board[r-1][i] = temp
            temp = curr

        # printMatrix(board)


        # bottom -> top
        # print("r",r,row)
        for i in range(r-2,row,-1):
            # print("here4")
            curr=board[i][0]
            board[i][0]=temp
            temp=curr

        # printMatrix(board)


    # for x,y in temp:
    #     첫번째꺼는 하나씩
    # row,col=temp_q.popleft()
    for i in range(2):
        if i==0:
            row,col=temp_q[0]
            time_move(row,col)
            # print(board)
            # printMatrix(board)

        else :

            rrow,ccol=temp_q[1]
            # print("rrow,ccol")
            reverse_move(rrow,ccol)


    # printMatrix(board)


# print(int(1.9))
# dust_move()
# print(dust_move())
while time<t:
    time+=1
    # print(dust_move())
    # printMatrix(copy_board)
    dust_move(board)
    # copy_board=copy.deepcopy(temp)
    # print()
    # printMatrix(copy_board)
    # 미세먼지 청소 시작
    cleaner()
    # printMatrix(board)


ans=0
for i in range(r):
    for j in range(c):
        if board[i][j]>0:
            ans+=board[i][j]

print(ans)

















# 미세먼지
import sys
import copy
sys.stdin=open("dust.txt","r")
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
    # temp_q=deque()
    # for i in range(r):
    #     for j in range(c):
    #         if board[i][j]==-1:
    #             temp_q.append((i,j))

    # 공기청정기 찾기
    now = (0, 0)
    for i in range(r):
        if board[i][0] == -1 and board[i + 1][0] == -1:
            now = (i, i + 1)
            break



    print("now",now)

    # 순환
    # upper bound (오 위 왼 아래 순서)
    # 왼쪽->오른쪽
    # 2행 7열, 맨끝에꺼를 temp에 저장함
    temp = board[now[0]][c-1]
    #한칸씩 오른쪽으로 이동
    for i in range(c-2, 0, -1):
        board[now[0]][i+1] = board[now[0]][i]

    # 아래->위쪽
    # 마지막 꺼를 임시 저장함
    # 한칸씩 위로 이동
    temp2 = board[0][c-1]
    for i in range(now[0]-1):
        board[i][c-1] = board[i+1][c-1]

    # 1행 7열에 위에서 저장한 임시값을 놓음
    board[now[0]-1][c-1] = temp


    # 오른쪽->왼쪽
    # 마지막끝에 임시값을 저장함
    temp = board[0][0]
    for i in range(c-1):
        board[0][i] = board[0][i+1]
    board[0][c-2] = temp2


    #위에서 ->아래
    # 임시값을 놓음
    for i in range(now[0]-1, 1, -1):
        board[i][0] = board[i-1][0]
    board[now[0]][1] = 0
    board[1][0] = temp



    # lower boud (오 아래 왼 위 순서)
    temp = board[now[1]][c-1]
    for i in range(c-2, 0, -1):
        board[now[1]][i+1] = board[now[1]][i]

    temp2 = board[r-1][c-1]
    for i in range(r-1, now[1], -1):
        board[i][c - 1] = board[i-1][c - 1]
    board[now[1]+1][c-1] = temp

    temp = board[r-1][0]
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]
    board[r-1][c-2] = temp2

    for i in range(now[1]+1, r-1):
        board[i][0] = board[i+1][0]
    board[now[1]][1] = 0
    board[r-2][0] = temp


    # printMatrix(board)

    # def time_move(row,col):
    #
    #     # up
    #     # 1 - 아래
    #     temp = board[row][col]
    #     for i in range(c - 1, 1, - 1):
    #         board[row][i] = board[row][i - 1]
    #     board[row][1] = 0
    #
    #     # 2 - 오른쪽
    #     temp_1 = board[0][c - 1]
    #     for i in range(row - 1):
    #         board[i][c - 1] = board[i + 1][c - 1]
    #     board[row][c - 1] = temp
    #
    #     # 3 - 위쪽
    #     temp_2 = board[0][0]
    #     for i in range(c - 2):
    #         board[0][i] = board[0][i + 1]
    #     board[0][c - 2] = temp_1
    #
    #     # 4 - 왼쪽
    #     for i in range(row - 1, 1, -1):
    #         board[i][0] = board[i - 1][0]
    #     board[1][0] = temp_2
    #
    # # #     left->right
    # #     col=1
    # #     temp=board[row][1]
    # #     board[row][1]=0
    # #     for i in range(2,c):
    # #         # print("here1")
    # #         curr=board[row][i]
    # #         board[row][i]=temp
    # #         temp=curr
    # #
    # #     # printMatrix(board)
    # #     # print()
    # #
    # # # (0,0) (0,1)
    # # # (1,0) (1,1)
    # # # bottom -> top
    # # #     print("temp",temp)
    # #     for i in range(row-1,-1,-1):
    # #         # print("here2")
    # #         curr=board[i][c-1]
    # #         board[i][c-1]=temp
    # #         temp=curr
    # #
    # #     # printMatrix(board)
    # #     # print()
    # #
    # #     # print(temp)
    # #
    # #     # right->left
    # #     # c-1 -> -1 -1
    # #
    # #     for i in range(c-2,-1,-1):
    # #         curr=board[0][i]
    # #         # print("curr",curr)
    # #         board[0][i]=temp
    # #         temp=curr
    # #
    # #     # printMatrix(board)
    # #     # print()
    # #
    # #
    # # # top->bottom
    # #     for i in range(0,row-1):
    # #         # print("here4")
    # #         curr=board[i][0]
    # #         board[i][0]=temp
    # #         temp=curr
    # #
    # #
    # #     # printMatrix(board)
    #
    #
    #
    # def reverse_move(row,col):
    #
    #     row=row-1
    #     # down
    #     # 1- 위쪽
    #     temp = board[row][c - 1]
    #     for i in range(c - 1, 1, -1):
    #         board[row][i] = board[row][i - 1]
    #     board[row][1] = 0
    #
    #     # 2 오른쪽
    #     temp_1 = board[r - 1][c - 1]
    #     for i in range(r - 1, row + 1, -1):
    #         board[i][c - 1] = board[i - 1][c - 1]
    #     board[row + 1][c - 1] = temp
    #
    #     # 3 - 아래쪽
    #     temp_2 = board[r - 1][0]
    #     for i in range(c - 2):
    #         board[r - 1][i] = board[r - 1][i + 1]
    #     board[r - 1][c - 2] = temp_1
    #
    #     # 4 - 왼쪽
    #     for i in range(row + 1, r - 1):
    #         board[i][0] = board[i + 1][0]
    #     board[r - 2][0] = temp_2

        #     left->right
        # col = 1
        # temp = board[row][1]
        # board[row][1] = 0
        #
        # # printMatrix(board)
        # # print("temp",temp)
        #
        # for i in range(2, c):
        #     # print("here1")
        #     curr = board[row][i]
        #     board[row][i] = temp
        #     temp = curr
        #
        # # printMatrix(board)
        #
        # # top -> bottom
        # for i in range(row+1, r):
        #     # print("here2")
        #     curr = board[i][c - 1]
        #     board[i][c - 1] = temp
        #     temp = curr
        #
        # # printMatrix(board)
        #
        # #   right-> left
        # # print("temp",temp)
        # for i in range(c-2, -1, -1):
        #     # print("here3")
        #     # print("here")
        #     curr = board[r-1][i]
        #     board[r-1][i] = temp
        #     temp = curr
        #
        # # printMatrix(board)
        #
        #
        # # bottom -> top
        # # print("r",r,row)
        # for i in range(r-2,row,-1):
        #     # print("here4")
        #     curr=board[i][0]
        #     board[i][0]=temp
        #     temp=curr

        # printMatrix(board)


    # for x,y in temp:
    #     첫번째꺼는 하나씩
    # row,col=temp_q.popleft()
    # for i in range(2):
    #     if i==0:
    #         row,col=temp_q[0]
    #         time_move(row,col)
    #         # print(board)
    #         # printMatrix(board)
    #
    #     else :
    #
    #         rrow,ccol=temp_q[1]
    #         # print("rrow,ccol")
    #         reverse_move(rrow,ccol)


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

















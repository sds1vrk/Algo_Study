# 2048 게임
# 5번 이동했을때 나오는 최대 수 구하기
import sys
from collections import deque
sys.stdin=open("2048.txt","r")

import copy
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

# print(a)
# q=deque(a)
# print(q)

# left Move
def left(board):
    for i in range(n):
        pos = 0
        temp = 0
        for j in range(n):
            if board[i][j]==0:
                continue

            if temp==0:
                temp=board[i][j]

            else :
                # 다음에 들어갈 값이 temp와 같은 값이라면 삽입
                if temp==board[i][j]:
                    board[i][pos]=2*temp
                    pos+=1
                    temp=0
                # 다른 값이라면  2 3 4
                else :
                    board[i][pos]=temp
                    pos+=1
                    temp=board[i][j]

            # 블록이 이동했으므로 현재 값은 0으로 만들어줌
            board[i][j]=0

        # 마지막 위치에 있는 temp값을 빈자리인 pos에 넣기위해 사용
        if temp!=0 :
            board[i][pos]=temp
        # print(board)

    return board

def right(board):
    print(board)
    for i in range(n):
        pos=n-1
        temp=0
        for j in range(n-1,-1,-1):
            if board[i][j]==0:
                continue

            if temp==0:
                temp=board[i][j]

            else :
                # 다음에 뒤와 같다면 pos에는 2배인 값이 들어간다.
                if temp==board[i][j]:
                    board[i][pos]=2*temp
                    pos=pos-1
                    temp=0

                # 다르다면 pos에는 임시값이 들어간다.
                else :
                    board[i][pos]=temp
                    pos=pos-1
                    # 그리고 temp에는 해다하는 값이 들어간다.
                    temp=board[i][j]
                    # print("temp",temp)

            board[i][j]=0

        if temp!=0:
            board[i][pos]=temp

    return board


def upMove(board):
    for i in range(n):
        pos=0
        temp=0
        for j in range(n):
            if board[j][i]==0:
                continue

            if temp==0:
                temp=board[j][i]

            else :
                if temp==board[j][i]:
                    board[pos][i]=temp*2
                    temp=0
                    pos+=1

                else :
                    board[pos][i]=temp
                    pos+=1
                    temp=board[j][i]

            board[j][i]=0
        # 마지막 처리
        if temp!=0:
            board[pos][i]=temp

    return board


def downMove(board):
    for i in range(n):
        pos=n-1
        temp=0
        for j in range(n-1,-1,-1):

            if board[j][i]==0:
                continue


            if temp==0:
                temp=board[j][i]

            else :
                if temp==board[j][i]:
                    board[pos][i]=temp*2
                    pos -= 1
                    temp=0

                else :
                    board[pos][i]=temp
                    pos-=1
                    temp=board[j][i]

            board[j][i]=0

        if temp!=0:
            board[pos][i]=temp

    return board

max_value=0
def dfs(l,board):
    if l==5:
        global max_value
        for i in range(n):
            for j in range(n):
                if max_value<board[i][j]:
                    max_value=board[i][j]





    else :
        # deep Copy를 쓰는이유 새로운 행열을 그대로 쓰기 위해서
        dfs(l+1,left(copy.deepcopy(board)))
        # print(board)
        dfs(l + 1, right(copy.deepcopy(board)))
        dfs(l + 1, downMove(copy.deepcopy(board)))
        dfs(l + 1, upMove(copy.deepcopy(board)))


# dfs(0,board)
# print(max_value)

print(left(board))
# print(right(board))
# print("test")
# print(upMove(board))
# print(downMove(board))
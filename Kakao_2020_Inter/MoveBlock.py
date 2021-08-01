# 블록 이동하기

from collections import deque
def solution(board):
    answer = 0


    start=deque()
    a=[[0,0],[1,0]]
    start.append(a)



    dx=[1,0,0,-1]
    dy=[0,1,-1,0]

    while start:
        a1, a2 = start.popleft()
        print(a1)
        print(a2)

        for i in range(4):
            nx=a1[0]+dx[i]
            ny=a1[1]+dy[i]

            n2x=a2[0]+dx[i]
            n2y=a2[0]+dy[i]

            if nx





    size=2





    return answer


solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
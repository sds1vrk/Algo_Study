# 삼각 달패이 문제
# 문제 해석
# n이 3개일때
# a행은 1개
# a행은 2개
# a해은 3개

#   1
# 2  6
# 3 4 5

# n이 4개일때
# a행은 1개
# a행은 2개
# a행은 3개
#    1
#  2    9
# 3  10  8
#4  5  6  7

# n이 1,2,3일때 1번 회전, n이 4,5,6일떄 2번 회전, n이 7,8,9일떄 3번 회전
import sys
# sys.stdin=open("pro4.txt","r")


# 회전수 구하기

def solution(n):

    # 행렬 구하기 주어진 n개에 대하여
    a=[[0]*i for i in range(1,n+1)]
    # print(a)

    # 회전수 구하기
    rotate=(n-1)//3+1
    # print(rotate)

    # 초기 좌표 (이유는 아래부터 시작하기 때문에, 바로 전꺼를 잡는다)
    x,y=-1,0
    # 초기값은 0
    k=0

    # 다음 턴에서 감소시키기 위한 t값 설정
    t=0
    for _ in range(rotate):

        # 아래로 이동
        for _ in range(n-t):
            x+=1
            k+=1
            a[x][y]=k

        # 오른쪽으로 이동 (1개가 빠짐)
        for _ in range(n-t-1):
            y+=1
            k+=1
            a[x][y]=k

        # 왼쪽 대각선으로 이동 (1개가 더 빠짐)
        for _ in range(n-t-2):
            x-=1
            y-=1
            k+=1
            a[x][y]=k


        # 다음 턴은 줄어들음
        t+=3


    # print(a)

    answer=[]
    # 리스트 합치기
    for i in range(n):
        for j in a[i]:
            answer.append(j)

    # print(answer)






    return answer




solution(4)


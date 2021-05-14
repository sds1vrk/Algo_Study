
# 토마토 BFS로 풀기
# 이슈 1. 맵에 토마토가 -1 or 1로만 이루어져 있으면 0 리턴, 맵에 토마토가 0 or -1로만 이루어져 있으면 -1 리턴 ==> 잘못생각
# 이슈 2. 시간초과 발생

# 문제 풀이 방법
# 1. 토마토가 이슈 1에 걸리는 경우 제외하고 시작
# 2. 익은 토마토의 위치 찾고 queue에 넣기
# 3. 익은 토마토 위치를 바탕으로 큐에 size를 바탕으로 for문 돌리기
#    - 처음에는 큐에 2개가 들어감
#    - 그리고 큐가 다 돌고 나면 1일 지난 후에 토마토 모습을 알 수 있음
#    - 이때 for문 써서 큐 돌려야됨 ==> 이유는 aplleTree_BFS와 동일함 ==> 한번 돌렸을때 맵의 상태변화를 갱신하기 때문임

# 4. size로 for문 돌린 후에 맵의 상태 확인하기 ==> 맵에 토마토가 0이 1나라도 있으면 다시 돌아야됨, for문을 다 돌았는데 없으면 그 값 출력

# 이슈 1에서
#1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 이 방법으로는 풀수 없음 ==> 이유는 아래 예처럼 이렇게 있으면 BFS를 다 돌려도 토마토가 익지 않은 상태이므로 -1 리턴해야됨

# 0 -1 -1
# -1 -1 1
# 1   1  1



import sys
from collections import deque

sys.stdin=open("input.txt","r")
m,n=map(int,input().split())

def print_graph(a):
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()

# n: 행, m: 열
a=[list(map(int,input().split())) for _ in range(n)]

# print(a)
# print_graph(a)
queue=deque()
# (0,0),(0,1)
# (1,0),(1,1)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 토마토가 모두 익어있는 상태라면 0출력, 모두 익지 못하는 상황이면 -1 출력
#1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# def tomatoPan():
#     for i in range(n):
#         for j in range(m):
#             if a[i][j]==1 or a[i][j]==-1:
#                 continue
#
#     else :
#         return 0

# 1번 - 모든 값이 0 or -1인 경우 ==> 익지 못함 ==> -1 리턴
# 2번 - 모든 값이 1 or -1인 경우 ==> 다 익음 ==> 0 리턴

# 시간초과 발생
# 1번 ==> break로 빨리 끊기



# def topatopan1():


# 이걸 대체
# def topatopan2():
#     for i in range(n):
#         for j in range(m):
#             if a[i][j]==1 or a[i][j]==-1:
#                 continue
#
#             else :
#                 return
#     else:
#         return 0


def solution():

    flag=1
    for i in range(n):
        for j in range(m):
            if a[i][j]==0:
                print("test")
                flag=0

    # else :
    #     return flag

    # result=topatopan1()
    # result2 = topatopan2()

    if flag==1:

        # 큐에 먼저 익은 토마토 위치 찾기
        for i in range(n):
            for j in range(m):

                if a[i][j] == 1:
                    queue.append((i, j))

        count = 0

        def pan():
            for i in range(n):
                for j in range(m):
                    if a[i][j] == 0:
                        return False
            else:
                return True

        while True:
            if pan():
                break

            else:
                size = len(queue)
                for _ in range(size):
                    x, y = queue.popleft()

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                            queue.append((nx, ny))
                            a[nx][ny] = 1

                    # print(queue)
                count += 1


        return count

    else :
        return -1



    # elif result2==0:
    #     return 0




k=solution()
print(k)

# print_graph(a)









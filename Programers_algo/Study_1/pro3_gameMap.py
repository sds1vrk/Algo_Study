# 게임 맵 최단거리 구하기
# 해결방법
# 1. 최단거리 -> BFS로 풀기
# 2. 지나온길은 0으로 다시 막아버림
# 3. 전 위치에서 +1로 경로 증가한 후 맵에 기록하기
# 4. 마지막 좌표 a[n-1][m-1]이 1 이하이면 -1 출력 (도착을 못하는 곳), 그 외에는 a[n-1][m-1] 출력

from collections import deque

def solution(maps):

    # print("maps",maps)
    # 북동남서
    # (0,0)(0,1)
    # (1,0)(1,1)
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    queue=deque()
    queue.append((0,0))

    n=len(maps)
    m=len(maps[0])


    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                queue.append((nx,ny))
                maps[nx][ny]=maps[x][y]+1

    answer=maps[n-1][m-1]

    if answer<=1 :
        return -1

    else :
        return answer


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
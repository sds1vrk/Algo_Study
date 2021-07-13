# 게임 맵 최단거리 구하기
# 해결방법 최단거리 -> BFS로 풀기
# 1. 큐에 시작점 (0,0) 삽입
# 2. 큐에서 하나를 뺀다음에 4방향 탐색
# 3. 조건에 맞으면 큐에 넣고 맵에는 방문기록을 하기 위해 ==> 현재 위치 값 +1 ==>을 맵에 기록
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
    # 1. 큐에 시작점 (0,0) 삽입
    queue.append((0,0))

    n=len(maps)
    m=len(maps[0])


    while queue:
        # 2. 큐에서 하나를 뺀다음에 4방향 탐색
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 3. 조건에 맞으면 큐에 넣고 맵에는 방문기록을 하기 위해 ==> 현재 위치 값 +1 ==>을 맵에 기록
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                queue.append((nx,ny))
                maps[nx][ny]=maps[x][y]+1

    # 4. 마지막 좌표 a[n-1][m-1]이 1 이하이면 -1 출력 (도착을 못하는 곳), 그 외에는 a[n-1][m-1] 출력
    answer=maps[n-1][m-1]
    if answer<=1 :
        return -1
    else :
        return answer


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
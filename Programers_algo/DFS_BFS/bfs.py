
from collections import deque

def bfs(graph,node,visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue=deque([node])
    # 현재 노드 방문처리
    visited[node]=True

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end=" ")

        # 뽑은 원소와 연결된 노드들이 아직 방문하지 않았으면 원소들을 큐에 삽입 하고 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현 - 인접 리스트로 표현
graph=[
    [], #인덱스 0인것을 비워두고 노드의 번호를 그대로 사용하기 위해서
    [2,3,8], # 노드 1은 - 노드 2,3,8이랑 연결
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9
bfs(graph,1,visited)
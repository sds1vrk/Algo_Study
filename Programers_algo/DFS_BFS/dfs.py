# DFS 예제

# DEF 방문 처리 확인
def dfs(graph,v,visited):
    # 방문처리
    visited[v]=True
    # 어떤게 방문됐는지 확인
    print(v,end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # 아직 방문하지 않았으면 들어가서 방문처리 후 ==> 그 안에 연결된 노드를 방문처리 ==> STACK 방식
        if not visited[i]:
            dfs(graph,i,visited)

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
dfs(graph,1,visited)
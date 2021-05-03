# 위상정렬
# 정렬 알고리즘의 일종
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할때 사용
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

# 선수과목 수강
# 자료구조 -> 고급알고리즘
# 자료구조 -> 알고리즘 -> 고급 알고리즘

# 모든 과목을 수강하기 위해서는 자료구조 -> 알고리즘 -> 고급 알고리즘 순서로 강의를 들어야 함.

# 진입차수
# 진입차수란 특정한 노드로 들어오는 간선의 개수

# 위상정렬 알고리즘
# 1. 진입차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌때까지 다음의 과정을 반복한다
#   2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
#   2-2. 새롭게 진입차수가 0인 된 노드를 큐에 넣는다.

from collections import deque
v,e=map(int,input().split())

indegree=[0]*(v+1)

graph=[[]for i in range(v+1)]


for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    # 차수증가
    indegree[b]+=1


def topology_sort():
    result=[]
    queue=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        now=queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1

            if indegree[i]==0:
                queue.append(i)

    for i in result:
        print(i,end=" ")

    topology_sort()
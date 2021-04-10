# 크루스칼 알고리즘을 이용한 풀이

# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else :
        parent[a]=b


def solution(n, costs):

    parent = [0] * (n + 1)

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    for i in range(1, n + 1):
        parent[i] = i

    # 모든 간선에 대한 정보 입력받기
    for i in range(len(costs)):
        # a, b, cost = map(int, input().split())
        # 비용 순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
        cost,a,b=costs[i][2],costs[i][0],costs[i][1]
        # print(costs[i])
        # print(costs[i][0])
        edges.append((cost, a, b))

    # 간선을 비용순으로 정렬
    edges.sort()
    result = 0
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost


    print(result)
    return result


# 노드번호,노드번호,비용
solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
# 최소 신장 트리
# 최사소한의 비용으로 구성되는 신장 트리를 찾을때

# N개의 도시가 존재, 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결
# 이때 최소한의 비용으로

# 대표적인 최소 신장 트리 알고리즘은 크루스칼 알고리즘

# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#   1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#   2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않습니다
#   * 사이클이란 한 정점에서 다시 그 정점으로 돌아가는 모든 경로를 말한다.
# 3. 모든 간선에 대하여 2번의 과정을 반복

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

v,e=map(int,input().split())
parent=[0]*(v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0


for i in range(1,v+1):
    parent[i]=i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a,b,cost=map(int,input().split())
    # 비용 순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함

    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)
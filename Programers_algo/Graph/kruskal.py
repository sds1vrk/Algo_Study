# 크루스칼 알고리즘
# 가장 적은 비용으로 모든 노드를 연결
# UnionFind
import sys
sys.stdin=open("input.txt","r")

# 특정 원소가 속한 부모 집합 찾기
def find_parent(parent,x):
    # 루트 노트가 아니라면, 루트 노드를 찾을떄까지 재귀적으로 후촐
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    # parent[x]가 갱신됨
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else :
        parent[a]=b

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i


for _ in range(e):
    a,b,cost=map(int,input().split())

    # 비용순으로 정렬하기
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()



# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)


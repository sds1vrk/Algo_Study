# Union_Find를 이용한 사이클 판별 소스코드

def find_parent(parent,x):
    # 만약 들어온 노드가 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    # 작은 값으로 갱신
    if a<b:
        parent[b]=a
    else :
        parent[a]=b

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v,e=map(int,input().split())
parent=[0]*(v+1)  # 부모 테이블 초기화

for i in range(1,v+1):
    parent[i]=i


cycle=False

for i in range(e):
    a,b=map(int,input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else :
        union_parent(parent,a,b)


if cycle:
    print("사이클 발생")
else :
    print("사이클 발생하지 않았습니다")


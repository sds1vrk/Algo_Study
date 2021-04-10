


def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else :
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i


for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)
    print("부모 테이블:", end="")
    for i in range(1, v + 1):
        print(parent[i], end="")



# 각 원소가 속한 집합 출력
# print("각 원소가 속한 집합",end="")
# for i in range(i,v+1):
#     print(find_parent(parent,i),end="")

# 부모 테이블 내용 출력
print("부모 테이블:",end="")
for i in range(1,v+1):
    print(parent[i],end="")
import sys
sys.stdin=open("input.txt","r")
# n-node, m 간선
n,m=map(int,input().split())
# 인접행렬 초기화
# 이때 한개 더 많게 그리기
g=[[0]*(n+1) for _ in range(n+1)]

# 연결된 간선 그리기
for i in range(m):
    a,b=map(int,(input().split()))
    g[a][b]=1

print(g)
# 방문한 경우 체크
visited=[0]*(n+1)
def dfs(v):
    # 방문 처리
    visited[v] = 1

    if v==n:
        # dfs 종료
        # print("dfs")
        for i in range(n+1):
            if visited[i]!=0:
                print(i,end=" ")
        visited[v]=0
        print()


    else :
        # 해당 노드와 연결된것 보기
        # print("g[v]",g[v])
        for node,vv in enumerate(g[v]):
            # 노드, 간선정보
            if vv==1 and visited[node]==0:
                dfs(node)
                # 끝나고 나서 방문처리 다시 0으로
                visited[node]=0


dfs(1)
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


    if v==n:
        # dfs 종료
        # print("dfs")
        for x in path:
            print(x, end=" ")

        visited[v]=0
        print()


    else :
        # 해당 노드와 연결된것 보기
        # print("g[v]",g[v])
        # 1번 노드부터 시작해서 n번까지 가지치기
        # 인접행렬 접근 방법 1번 부터 시작해서~ n+1까지
        for i in range(1,n+1):
            if g[v][i]==1 and visited[i]==0:
                visited[v] = 1
                path.append(i)
                dfs(i)
                # 넣었던거 다시 빼기
                path.pop()
                # 끝나고 나서 방문처리 다시 0으로
                visited[i]=0

path=[]
path.append(1)
dfs(1)
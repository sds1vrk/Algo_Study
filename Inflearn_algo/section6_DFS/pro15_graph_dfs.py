# 경로 탐색 (그래프 DFS)
# 방향 그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력
# 방문한 노드는 중복해서 방문하지 않는다.

# 그래프 나타내기
import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

# 그래프 그리기
# 0번은 사용하지 않음
g=[[0]*(n+1) for _ in range(n+1)]

# 연결 정보 나타내기
for i in range(m):
    a,b=map(int,input().split())
    g[a][b]=1

# print(g)
def dfs(v):
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()

    else :
        # 1번 노드부터 n번 노드까지 (가지)
        for i in range(1,n+1):
            # 1번 노드부터 i번쨰 가지 노드로 갈수 있는게 1인지 확인 (연결된것)
            if g[v][i]==1 and visit[i]==0:
                # 방문처리하고 1처리
                visit[i]=1
                # i가 방문하는 곳
                path.append(i)
                dfs(i)
                # 경로에 넣었던것 pop, 끝까지 도착해서 최종 노드에서 빼주기 위해
                path.pop()
                # 방문하고 풀어줌, 다른 가닥에서 사용하기 위해서
                visit[i]=0





# 방문 여부 체크
# 1버부터 사용하기 위해
cnt=0
visit=[0]*(n+1)
# 1번 노드 방문
visit[1]=1
# 방문한것 찾기
path=[]
path.append(1)
dfs(1)

print(cnt)








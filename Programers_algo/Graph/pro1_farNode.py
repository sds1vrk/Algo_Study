# 가장 먼 노드 찾기
# BFS
from collections import deque

def solution(n, edge):

    # 인접 리스트 - 필요한 노드만 잇는다, 노드
    g=[[] for _ in range(n+1)]

    for i,j in edge:
        # g[i][j]=1
        # g[j][i] = 1
        g[i].append(j)
        g[j].append(i)


    # print(g)
    # 방문학인
    visitied=[-1]*(n+1)



    def bfs(l):
        depth=0
        # 1번 노드 저장
        queue=deque([[l,depth]])

        while queue:
            vv=queue.popleft()

            v=vv[0]
            depth=vv[1]

            if visitied[v]==-1:
                visitied[v]=depth
                depth+=1
                # print(v,end=" ")

                # node, depth
                for i in g[v]:
                    queue.append([i,depth])



    # 1번 노드부터 시작
    bfs(1)
    answer=0
    for v in visitied:
        if v==max(visitied):
            answer+=1

    print(answer)

    return answer


solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
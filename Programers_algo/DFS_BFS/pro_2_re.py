# 네트워크
def solution(n, computers):

    def dfs(computers,node,visited):
        # print("dfs")
        # 들어온 노드를 방문처리 한다.
        if visited[node]==False:
            visited[node] = True

        for i in range(len(computers)):
            if not visited[i] and computers[node][i]==1:
                dfs(computers,i,visitied)


    visitied=[False]*(n)

    result=0


    while False in visitied:
        for i in range(n):
            if visitied[i]==False:
                dfs(computers,i,visitied)
                result+=1

    return result






print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
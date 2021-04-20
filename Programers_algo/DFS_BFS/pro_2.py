# 네트워크

# DFS로 풀기
# 더이상 갈




def solution(n, computers):

    def dfs(i,j):
        # print("dfs")

        # 노드 방문처리
        # visited[node]=True

        # 방문처리된 것은 연결되어 있는거임
        if computers[i][j]==0:
            # 방문처리
            computers[i][j]=1
            dfs()

            return True

        else :
            return False



    # 노드의 개수만큼 방문처리를 위해 만들어줌
    visited=[False]*(n+1)


    result=0
    for i in range(n):
        for j in range(n):
            if dfs(i,j)==True:
                result+=1
    print(result)

    answer = 0
    return answer



solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])
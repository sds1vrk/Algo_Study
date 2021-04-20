# 네트워크
def solution(n, computers):

    def dfs(computers,node,visited):

        if visited[node]==False:
            visited[node] = True

        # Node에 연결된 정보 확인, 이때 인접 행렬로 되어 있어 자기 정보의 노드가 포함되어 있음
        # 1. 처음에 방문 처리를 하면 문제점 ==> 노드 2가 이쪽 if문에 걸려 못들어옴, 결국엔 result+=1 증가 못함
        # ==> if 문 안에 방문하지 않을 경우에만 방문처리

        # index는 node에 연결된 Node들
        # vv는 연결 여부 1 이면 연결, 0이면 연결안됨
        for index,vv in enumerate(computers[node]):
            if not visited[index] and vv==1 :
                # visited[index] = True
                dfs(computers,index,visited)
                return True

        else :
            return False

    visited=[False]*(n)

    result=0
    for i in range(n):
        if not visited[i]:
            if dfs(computers,i,visited):
                result+=1

    return result


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
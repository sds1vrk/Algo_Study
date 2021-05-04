# 여행경로

from collections import deque

# 시작은 인천부터
# key, value 만들기
# dfs? bfs? ==> INCHON 시작부터 넣기 BFS 로 풀어보자
# 방문은은 set값으로 만들기 ==> 방문값 뺴기

def solution(tickets):
    a = []
    data=dict()
    visited=dict()
    queue = deque()

    # result=[]

    def bfs(node,data,visited):
        result=[]
        result.append(node)

        # 들어온거 방문처리
        visited[node]=1
        # result.append(node)
        queue.append([node,visited])

        while queue:
            # print(queue)
            node,visited=queue.popleft()

            # print("visitied",visited)

            k=data[node]

            # print(k, end=" ")
            result.append(k)

            # 해당 노드와 연결된것 찾기
            for i in data.keys():
                if i==k and visited[k]==0:
                    # k=data[i]
                    # print("k",k)
                    # bfs(k,data,visited)
                    # 방문 처리
                    visited[k]=1
                    queue.append([k,visited])

        return result


            # 종료 시점 찾기




    for i in range(len(tickets)):
        for j in range(2):
            a.append(tickets[i][j])
            data[tickets[i][0]]=tickets[i][1]
            # visited[tickets[i][0]]=0

    a = set(a)
    # print(a)

    for i in a:
        visited[i]=0

    print("data:",data)



    def check(array):
        print("test")





    # 인천에서 시작하는거 뽑기
    for i in data.keys():
        if i=='ICN':
            print(bfs(i,data,visited))


    answer = []
    return answer


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
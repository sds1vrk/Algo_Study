# 여행 경로
# DFS 풀기
# dict를 이용하여 그래프 만들기
# 이떄 value는 여러개가 들어가서 list로 사용 하기 위해 defaultdict를 사용
# defaultdict 사용 방법
#  - from collections import defaultdict
# - data=defaultdict(list)를 박는다


from collections import defaultdict

def solution(tickets):
    def init_graph():
        data=defaultdict(list)
        for key,value in tickets:
            data[key].append(value)
        return data


    def dfs():
        stack=["ICN"]
        path=[]
        while stack:
            top=stack[-1]

            if top in routes and routes[top]:
                stack.append(routes[top].pop(0))

            else :
                path.append(stack.pop())

        print(path[::-1])

    routes=init_graph()

    print(routes)
    # 키값을 이용해 value들을 정렬
    for i in routes:
        routes[i].sort()

    print(routes)
    dfs()



# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
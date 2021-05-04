# 끝까지 들어가야 되기 떄문에 DFS 로 풀어야 될것같다

from collections import deque



def solution(tickets):

    result=[]

    # 노드가 갈수 있는곳 중에서 알파벳이 빠른곳
    def go(node,new_tickets):
        result=[]
        print("new_ti",new_tickets)
        for i in new_tickets:
            if i[0]==node:
                result.append(i[1])

        result.sort()

        if result:
            print("result",result)
            return result
        else :
            return "none"

        # return result[0]

    def bfs(node,new_tickets):
        # print("bfs")
        queue=deque()
        queue.append(node)
        # print(queue)

        while queue:
            start=queue.popleft()
            # print("start",start,new_tickets)
            # 여기서 start가 바뀔수 있으므로 여기서 넣어주면 안됨
            # result.append(start)
            # result=[]
            # for i in new_tickets:
            #     if i[0]==start:
            #         result.append(i[1])
            result=go(start,new_tickets)
            # print("node",node)
            # print("result222",result)
            # start Node와 연결된 모든 정보를 큐에 담아야 함
            for i in result:
                queue.append(i)
                # print("i",i)

            # 다음 노드로 가기


            # if node=="none":
            #     continue
            #
            # else :
                # new_tickets.remove([start, node])
                # queue.append([node, new_tickets])



        return result

    result.append("ICN")

    # tickets=set(tickets)
    # 데이터 중복 없애기
    new_tickets=[]
    for i in range(len(tickets)):
        if tickets[i] not in new_tickets:
            new_tickets.append(tickets[i])

    print(new_tickets)

    result=go("ICN",new_tickets)
    # 티켓을 지우면 안됨 ==> 지우면 막혔을때 다시 못 돌아감
    # new_tickets.remove(["ICN",node])

    # 여기가 좀 걸리긴 하는데?! 처음꺼만 일단 제일 빠른것만 넣음
    # print("k:",result[0])
    answer=bfs(result[0],new_tickets)

    # return " ".join(answer)
    return answer

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))

print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
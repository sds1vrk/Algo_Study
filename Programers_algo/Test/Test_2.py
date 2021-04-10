# 시계 방향 회전 그래프
#

def solution(rows, columns, queries):
    # 행열 만들기
    # graph=[[0 for rows in range(rows)] for row in range(columns)]
    # print(graph)
    graph=[]
    for i in range(rows):
        graph.append([])
        for j in range(1,columns+1):
            # graph.append
            # print(rows*i+j)
            graph[i].append(rows*i+j)
    print("original_graph",graph)
    answer = []

    def mat_graph(graph):
        for row in graph:
            print(row)

    # 시계 방향 회전
    def rotate(graph,query):
        print(query)

        # top: starting row index
        # bottom : ending row index
        # left : starting column index
        # right : ending column index

        top=query[0]-1
        bottom=query[2]-1
        left=query[1]-1
        right=query[3]-1

        # print(top,bottom,left,right)

        array=[]

        # 왼쪽에서 오른쪽으로 이동
        # 처음 값은 따로 저장
        # 처음값을 지정해주기 위한 마지막 값
        prev=graph[top+1][left]
        for i in range(left,right+1):
            # 현재 값을 curr 임시 저장
            curr=graph[top][i]
            array.append(curr)
            graph[top][i]=prev
            prev=curr

        # 다음 행을 바꿔야 하므로 top+=1
        # 위에서 아래로 이동
        top+=1
        for i in range(top,bottom+1):
            curr=graph[i][right]
            array.append(curr)
            graph[i][right]=prev
            prev=curr

        # 오른쪽에서 왼쪽으로 이동
        # 한칸 왼쪽 열로 이동 해야 되므로 right-=1
        # 이떄 주의해야 할점은 오른쪽에서 left로 이동해야 되므로 step은 -1로 하고 마지막 값은 포함되야 하므로 -1
        right-=1
        for i in range(right,left-1,-1):
            curr=graph[bottom][i]
            array.append(curr)
            graph[bottom][i]=prev
            prev=curr

        # 맨 왼쪽 열에서 아래에서 위로 이동
        # 한칸 위로 이동 해야 하므로 bottom-=1
        bottom-=1
        for i in range(bottom,top-1,-1):
            curr=graph[i][left]
            array.append(curr)
            graph[i][left]=prev
            prev=curr


        print("테두리 안에 숫자", array)
        answer.append(min(array))
        return graph



    for i in queries:
        print("query",i)
        k=rotate(graph,i)
        # 회전 후에 그래프
        print("회전 후에 그래프")
        mat_graph(k)

        graph=k

    return answer




print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
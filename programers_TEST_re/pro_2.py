# 행렬 돌리기


def solution(rows, columns, queries):

    # 행열 만들기
    graph=[]
    for i in range(rows):
        g=[]
        for j in range(1,columns+1):
            g.append(i*columns+j)
        graph.append(g)

    print(graph)

    def rotate(graph,start,end):
        # 행렬 회전 그래프
        row=start[0]-1
        col=start[1]-1

        # 시작점
        temp=graph[row][col]
        graph[row][col] = graph[row + 1][col]

        # end
        end_row=end[0]-1
        end_col=end[1]-1


        # 언제까지 반복?
        # while

        # 왼쪽 -> 오른쪽
        i=1
        while i<=end_col-col:
            temp2=graph[row][col+i]
            graph[row][col+i]=temp
            # temp=graph[row][col+i]

            i+=1

        print(graph)


        # 위에서 -> 아래

        # 오른쪽 -> 왼쪽

        # 아래 -> 오른쪽


    for query in queries:
        x,y=query[0],query[1]
        dx,dy=query[2],query[3]

        start=query[:2]
        end=query[2:]
        # print(start)
        # print(end)
        rotate(graph,start,end)





    answer = []
    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
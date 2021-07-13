def solution(tickets):


    # 그래프 그리기
    # if key in data :
    #     data[key].append(value)
    # else :
        # data[key]=[value]

    data=dict()
    for src,dest in tickets:
        if src in data:
            data[src].append(dest)

        else :
            data[src]=[dest]

    # print(data)

    # value값 오름차순 정렬
    # d=sorted(data.items(),key=lambda x:x[1])
    # print(data)
    # print(d)

    # for i in data:
    #     values=data[i]
    #     values.sort()
    #     data[i]=values

    print("data",data)

    cnt=0
    for i in data:
        # set_route.add(i)
        # set_route.add(j)
        # print("i",i,data[i])
        # print(len(data[i]))
        cnt+=len(data[i])
        # set_route.add(data[i])
    # print("cnt",cnt)



    route=[]

    answer = []
    # DFS
    result=[]
    def dfs(node,route):
        if len(route)==cnt+1:
            # print("lenROute",len(route),route)
            result.append(route)
            return
            # print("test")


        else :

            if data[node]:
                for dest in data[node]:
                    v = data[node].pop(0)
                    fp = route[:]
                    fp.append(v)

                    ret = dfs(v, fp)

                    # if ret:
                    #     return ret

                    data[node].append(v)

            # dest = data[node].pop(0)
            # fp = route[:]
            # fp.append(dest)

            # print("route",route,len(route))
            # temp = dfs(dest, fp)

            # print("dest", dest)
            # data[node].insert(dest)
            # if data[node]:



            # if temp:
            #     return


                # print("len",route,len(route))
                # data[node].append(dest)
            # values=data[node]


            # for i in values:
            #     route.append(i)
            #     temp=dfs(i,route)
            #     if temp:
            #         return temp

                # route[i]

            # route.clear()



    route.append("ICN")
    dfs("ICN",route)
    # print(result.sort())
    answer=result[0]
    # print("ans",route)


    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
# print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]))
print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]))
# print(solution([["ICN","A"],["ICN","A"],["A","ICN"]]))
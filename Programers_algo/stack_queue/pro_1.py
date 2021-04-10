# 다리를 지나는 트럭
# 먼저 온건 먼저 나감 queue로 구현
# 대기 트럭 구한다
# 경과 시간 증가


from collections import deque


def solution(bridge_length, weight, truck_weights):

    wait_queue=deque(truck_weights)

    k=wait_queue.popleft()
    time=1
    value=[[k,time]]
    # bridge_queue
    bridge_queue=deque(value)
    print(bridge_queue)

    result_queue=deque()

    # bridge_queue에 다 빠져나가면 종료
    result=2
    while True:

        # print(bridge_queue)
        result+=1


        #종료조건
        print(len(result_queue),len(truck_weights))

        if len(result_queue)==len(truck_weights):
            break



        k1=0
        if wait_queue :
            k1 = int(wait_queue.popleft())
        else :
            # continue
            # wait queue에 남아 있는게 없으면 bridge_queue만 확인하고 temp가 2이면 result_queue에 넣어야 됨
            for i in bridge_queue:
                time+=1
                i[1]=time
                print("i",i)



            if bridge_queue:
                # 남아 있으면
                a1 = bridge_queue.popleft()
                if a1[1] == bridge_length:
                    result_queue.append(a1)

                    # 다리 검색 후 다리가 버티면 k를 넣는다.
                    sum = 0
                    for i in bridge_queue:
                        sum += i[0]

                    if sum <= weight:
                        print("here")
                        temp = [k1, 1]
                        bridge_queue.append(temp)
                        print("bri_que", bridge_queue)

            else :
                # bridge_queue도 비면
                continue








        sum=k1
        print("sum",sum)
        for i in bridge_queue:
            print("i[0]",i[0])
            sum+=i[0]
            print("sum",sum)

        # 다리가 하중을 견딜수 있으면 그제서야 넣는다.
        if sum<=weight:
            # k=wait_queue.popleft()
            print("endure")
            time=1
            temp=[k1,time]
            bridge_queue.append(temp)
            print("bri_queue",bridge_queue)

        # else :
        #     # 브리지 큐에 time을 증가시킨다
        #     # while i in bridge_queue:
        for i in bridge_queue:
            time+=1
            i[1]=time
            print("i",i)


        # 만약 맨 처음으로 꺼낸 i[1]==2라면 result queue에 저장하고 다리
        a1=bridge_queue.popleft()
        if a1[1]==bridge_length:
            result_queue.append(a1)

            # 다리 검색 후 다리가 버티면 k를 넣는다.
            sum = 0
            for i in bridge_queue:
                sum += i[0]

            if sum <= weight:
                print("here")
                temp = [k1, 1]
                bridge_queue.append(temp)
                print("bri_que", bridge_queue)


        # while i in bridge_queue:
        #     if i[1]==2:
        #         k=bridge_queue.popleft()
        #         print("k:",k)
        #         result_queue.append(k)
        #
        #         print("asdfasdf")
        #
        #         # 다리 검색 후 다리가 버티면 k를 넣는다.
        #         sum=0
        #         for i in bridge_queue:
        #             sum+=i[0]
        #
        #         if sum<=weight:
        #             print("here")
        #             temp=[k1,1]
        #             bridge_queue.append(temp)
        #             print("bri_que",bridge_queue)








        # 브리지 큐에 time을 증가시킨다


    print("result:",result)













    answer = 0
    return answer



solution(2,10,[7,4,5,6])

solution(100,100,[10])
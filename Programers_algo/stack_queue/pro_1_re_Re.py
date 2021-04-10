def solution(bridge_length, weight, truck_weights):
    # q [0,0] 다리 개수만큼 만들어줌
    q=[0]*bridge_length
    print("q",q)
    sec=0
    while q:
        # 큐가 빌때까지 반복한다
        sec+=1
        # 가장 맨처음 꺼를 뺸다
        # print(print(q.pop(0)))
        q.pop(0)

        # 만약 truck_weights가 비어있지 않으면
        if truck_weights:
            # 다리 안에 있는 무게들 합 + 맨처음 truck_weight
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                # 큐가 append 0을 해주는 이유는 더이상 다리가 꽉차 0 이라는 빈값을 넣는다.
                q.append(0)
    return sec


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
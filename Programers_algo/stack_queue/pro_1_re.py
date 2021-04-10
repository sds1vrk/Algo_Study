def solution(bridge_length, weight, truck_weights):
    in_bridge = []
    end_bridge = []
    n = len(truck_weights)
    time = 0
    while len(end_bridge) != n:
        for i in in_bridge:
            i[1] += 1

        print("in_bri",in_bridge)
        if in_bridge and in_bridge[0][1] > bridge_length:
            go = in_bridge.pop(0)
            end_bridge.append(go[0])
        if truck_weights:
            w = truck_weights[0]
        else:
            w = 0
        if sum([i[0] for i in in_bridge]) + w <= weight:
            if truck_weights:
                now = truck_weights.pop(0)
                in_bridge.append([now, 1])
        time += 1
    return time


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
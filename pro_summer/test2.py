from collections import deque

def solution(t, r):
    data=dict()
    for i,v in enumerate(t):
        print(i,v)
        data[i]=v

    data=sorted(data.items(), key=lambda x: (x[1],x[0]))

    print("data",data)
    result = []
    # temp=data.pop(0)[0]

    queue=deque(data)
    print(queue)


    max_time=max(t)
    start_time,start_idx=queue.popleft()

    time=0

    while time<max_time:
        qtime,q_idx=queue.popleft()

        if qtime==start_time:

            if r[start_idx]<r[q_idx]:
                result.append(r[start_idx])

            else :
                result.append(r[q_idx])
                queue.insert(1,[])


         time+=1





    print(result)










    answer = []
    return answer

solution([0,1,3,0],[0,1,2,3])
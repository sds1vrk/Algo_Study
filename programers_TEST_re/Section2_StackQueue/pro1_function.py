# 큐 안에 또 큐 사용하기

from collections import deque
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = round((100 - progresses[i]) / speeds[i] + 0.49)
        days.append(day)

    queue = deque(days)

    result=[]

    while queue:
        res=1
        k=queue.popleft()

        while queue:
            b=queue[0]

            if k>=b:
                res+=1
                queue.popleft()

            else :
                break
        result.append(res)

    print(result)

    # answer = []
    return result

solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])

solution([99, 99, 99] ,[1, 1,1])
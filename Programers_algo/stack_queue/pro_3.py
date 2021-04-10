# 기능개발
# 이 문제에 핵심은 queue를 사용하는 것과 뽑은 값과 다음 값을 비교해야 됨
# queue를 사용하는 이유는 먼저 뽑은 값이 다음 뽑은 값보다 클 경우 result+=1을 시킨다
# 이때 비교는 큐를 뽑지 않고 남아 있는 큐에 인덱스를 비교하는것으로 한다. 그래야지 비교가 되기 때문에


from collections import deque


def solution(progresses, speeds):

    # 컴프리션으로 리스트 만들기
    array=[[0] for _ in range(len(progresses))]
    print(array)
    # array 리스트에는 언제 배포되는지가 들어감
    #

    for i in range(len(progresses)):
        progresses[i]=100-progresses[i]
        k=progresses[i]%speeds[i]
        j = progresses[i] // speeds[i]

        if k!=0:
            array[i]=j+1

        else :
            array[i]=j


    print(progresses)
    print("배포일자",array)

    prev=0
    queue=deque(array)
    answer = []


    while queue:
        left=queue.popleft()
        result=1

        # 여기가 중요, 뽑은 값이 나머지 값보다 클때까지 result+=1 이때, 값을 뽑지 않기 위해서 인덱스를 사용
        while len(queue)!=0 and left>=queue[0]:
            result+=1
            queue.popleft()

        answer.append(result)




    # print(answer)



    return answer


# solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])
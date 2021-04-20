# BFS로 풀기
# 한개 빼고 그 수를 2배로 증가 (+,-) 각각 증가 시켜서 넣기


from collections import deque

def solution(numbers,target):

    answer=0
    queue=deque()
    # 큐에는 인덱스와 지금까지의 합을 넣는다
    queue.append([0,numbers[0]])
    queue.append([0,-1*numbers[0]])

    # 큐가 빌때까지 계속
    while queue:

        # 큐에서 값을 뽑는다
        idx,num=queue.popleft()
        idx+=1

        if idx<len(numbers):
            queue.append([idx,num+numbers[idx]])
            queue.append([idx, num - numbers[idx]])
        else :
            if num==target:
                answer+=1

    return answer







print(solution([1, 1, 1, 1, 1],3))


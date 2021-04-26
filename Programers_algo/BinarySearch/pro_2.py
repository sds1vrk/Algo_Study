# 징검다리
def solution(distance, rocks, n):

    start=1
    rocks.sort()
    rocks.append(distance)
    answer = 0

    while start<=distance:
        mid=(start+distance)//2
        curr=0
        remove_rock=0

        min_answer=float('inf')

        for i in rocks:
            diff=i-curr
            # diff는 고정된 값임, 돌을 지우는건 mid에 따라 달라짐
            # mid가 만약 크다면 돌을 적게 지우는거고
            if diff<mid:
                remove_rock+=1
            else :
                # 현재 위치에서 최소인지 확인하고 최소라면 갱신
                min_answer=min(min_answer,diff)
                curr=i

        if remove_rock>n:
            # 너무 많이 지웠으므로 거리를 줄여준다
            distance=mid-1
        else :
            # 딱 맞으므로 답을 갱신하고, 거리를 늘려준다
            answer=min_answer
            start=mid+1




    return answer


solution(25,[2, 14, 11, 21, 17],2)
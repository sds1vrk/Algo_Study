# 구명보트

# 문제 해결법
# 크기 순으로 나열후, 가장 큰것과 가장 작은것을 합친 다음에 이게 limit 초과되는지 확인
# 만약 초과가 안된다면 answer을 1 올리고 전체 크기에서 큰것과 작은것을 줄인다
# 초과가 된다면 end만 1씩 줄여 확인한다

def solution(people, limit):

    people.sort()

    print("sort people",people)

    first=0
    end= len(people)-1

    answer=0
    while first<=end:

        if people[first]+people[end]<=limit:
            answer+=1
            first+=1
            end-=1

        else :
            answer+=1
            end-=1


    print(answer)
solution([70,50,80,50],100)
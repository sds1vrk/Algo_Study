# 포켓몬 문제

def solution(nums):

    target=len(nums)/2

    set_numbers=set(nums)

    answer = 0
    for _ in range(len(set_numbers)):
        if answer<target:
            answer+=1

        elif answer==target:
            break


    # print(answer)





    return answer


# print(solution([3,1,2,3]))
# solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])
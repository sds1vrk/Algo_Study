# 로또 문제

def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()

    zero_count=lottos.count(0)
    # print(zero_count)
    # result=[]

    new_lottos=[]
    for i in lottos:
        if i!=0:
            new_lottos.append(i)

    # print(new_lottos)
    # print(win_nums)

    # 맞는지 비교
    result=0
    for i in win_nums:
        for j in new_lottos:
            if i==j:
                result+=1

    # result+=zero_count
    # print(result)


    def rank_count(su):
        if su==6:
            return 1
        elif su==5:
            return 2

        elif su == 4:
            return 3

        elif su == 3:
            return 4

        elif su == 2:
            return 5

        else :
            return 6

    a=rank_count(result)
    b=rank_count(result+zero_count)
    answer=[b,a]
    # print(answer)

    return answer


print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
def solution(lottos, win_nums):

    print(lottos)
    print(win_nums)

    lottos.sort()
    win_nums.sort()

    test_lotto=[]
    # 먼저 기본적으로 맞는 개수, 0을 제외한
    for i in lottos:
        if i!=0:
            test_lotto.append(i)

    # 0의 개수는
    count_0=len(lottos)-len(test_lotto)
    print("test_lo",test_lotto,count_0)

    # 당첨 count
    def count(lotto):
        if lotto==6:
            return 1
        elif lotto==5:
            return 2
        elif lotto==4:
            return 3
        elif lotto==3:
            return 4
        elif lotto==2:
            return 5
        else :
            return 6


    new_lotto=[]
    for i in win_nums:
        for j in test_lotto:
            if i==j:
                new_lotto.append(i)

    m=count(len(new_lotto))
    print("꼴등 로또 ",m)

    # 꼴등+0의 개수
    n=count(len(new_lotto)+count_0)
    print("1등 로또",n)


    answer = [n,m]
    print(answer)
    return answer


solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])
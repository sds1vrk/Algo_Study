# 순위매기기

def solution(n,results):
    wins={}
    loses={}

    for i in range(1,n+1):
        wins[i]=set()
        loses[i]=set()

    for winner,loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)

    # print(wins)
    # print(loses)

    for i in range(1,n+1):

        # 진 사람중에 나온 이긴 사람을 wins에 추가시킨다
        # set에서 update는 여러개 값 한꺼번에 추가
        for winner in loses[i]:
            # print("winnser",winner,"losers[i]",loses[i],"wins[i]",wins[i])
            wins[winner].update(wins[i])

        # 이긴사람들중에 나온 진 사람을 loses에 추가시킨다
        for loser in wins[i]:
            loses[loser].update(loses[i])

    # print(wins)
    # print(loses)

    answer=0
    for i in range(1,n+1):
        if len(wins[i])+len(loses[i])==n-1:
            answer+=1

    # print(answer)
    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	)
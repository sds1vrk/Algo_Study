from itertools import combinations

def solution(arr,k,t):
    answer=0
    size=len(arr)

    def hap(k):
        hh=0
        if sum(k)<=t:
            return True
        else :
            return False

    for i in range(k,size+1):
        a=list(combinations(arr,i))
        for k in a:
            pan=hap(k)

            if pan:
                answer+=1


    print(answer)
    return answer

solution([2,5,3,8,1],3,11)

solution([1,1,2,2],2,3)

solution([1,2,3,2],2,2)


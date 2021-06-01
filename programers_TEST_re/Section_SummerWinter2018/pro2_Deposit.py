# 오름차순
# 1,2,3,4,5
# 제일 작은거 합치고 계쏙 합칠수 있으면 index+=1
# 2,2,3,3

# 런타임 에러 d: (1,2,3) , budget:10인 경우 에러 이유는 lt를 다 쓴 경우도 return 해줘야 함
#

def solution(d, budget):
    d.sort()

    lt = 0
    hap = 0
    cnt = 0

    # 3번 에러 케이스
    # sort한 첫번쨰 수가 budget보다 크면 return
    if d[0] > budget:
        return 0

    while lt < len(d):
        hap += d[lt]
        cnt += 1

        if lt == len(d) - 1:
            return cnt

        if hap < budget:
            lt += 1

        elif hap == budget:
            return cnt

        else:
            cnt -= 1
            return cnt
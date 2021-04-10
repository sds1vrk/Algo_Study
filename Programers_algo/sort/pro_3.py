# H-Index
# 최대 값부터 시작해서 역순으로 구한다
# 빠른 시간내에 찾기 위해서


def solution(citations):
    print(citations)
    citations.sort()

    j=int(len(citations))
    maxi=max(citations)

    if maxi==0:
        return 0

    for i in range(maxi,0,-1):
        # print(citations[i])
        result=0

        for ci in citations:
            if ci>=i:
                result+=1

            if result==i:
                return result


    # answer = 0
    # return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([0,2,4,6]))
print(solution([0,0,0]))

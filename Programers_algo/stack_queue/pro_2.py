# 주식 가격

# 처음 인덱스 i 부터 끝까지 비교
# 2중 for문으로 시간이 걸리긴 하나 prices의 길이가 10만 이하이기 때문에?!
# break에 걸리므로 빨리 안에 for문을 종료 가능



from collections import deque

def solution(prices):

    array=[]
    for i in range(len(prices)):

        temp=0
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                temp+=1

            else :
                temp+=1
                break

        array.append(temp)

    print(array)
    # answer = []
    return array



solution([1,2,3,2,3])
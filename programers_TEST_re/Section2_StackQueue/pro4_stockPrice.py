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

    # print(array)
    # answer = []
    return array
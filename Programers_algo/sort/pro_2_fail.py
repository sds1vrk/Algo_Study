#가장 큰 수 찾기
def solution(numbers):
    array=[]
    for i in numbers:
        array.append(str(i))
    if max(numbers)==0:
        return '0'
    array.sort(reverse=True)
    print(array)
    def bigo(i, j):
        a = int(i + j)
        b = int(j + i)
        if a >= b:
            return True
        else:
            return False
    for i in range(0,len(array)-1,1):
        # print(array[i])
        result=bigo(array[i],array[i+1])
        if result:
            # new_array.append(array[i])
            continue
        else :
            # new_array.append(array[i+1])
            array[i],array[i+1]=array[i+1],array[i]
        # new_array.append(array[])
    print("swap",array)
    answer=''
    for i in array:
        answer+=i
    # print(answer)
    return answer
solution([90,908,89,898,10,101,1,8,9])
solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
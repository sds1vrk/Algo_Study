# 체육복
def solution(n, lost, reserve):

    # 1인 리스트 만들기
    # 리스트 컴프리션
    array=[1 for _ in range(n)]
    print(array)

    # lost 만큼 빼주기

    for i in range(len(lost)):
        # print(lost[i]) # 2
        j=lost[i]
        array[j-1]-=1

    print("lost_array",array)

    #reserve 구하기

    for i in range(len(reserve)):
        j=reserve[i]
        array[j-1]+=1

    print("reserver_array",array)
    # 이미 lost, reserver를 통해 다른 학생에게 빌려줄수 없는거 체크 한 상태여서 굳이 할 필요 없을듯


    # 0번 인덱스만 앞에꺼 빌릴수 있음
    if array[0] == 0 and array[1] == 2:
        array[1] = 1
        array[0] = 1

    # 1번 인덱스부터는 뒤에꺼나 앞에꺼 빌릴수 있음
    for i in range(1,len(array)-1):

        # 앞에서 먼저 빌리고
        if array[i]==0 and array[i-1]==2 :
            array[i-1]=1
            array[i]=1

        # 뒤에서 먼저 빌린다
        if array[i]==0 and array[i+1]==2:
            array[i + 1] = 1
            array[i] = 1

    # print("result",array)

    answer=0
    for i in array:
        if i>=1:
            answer+=1


    return answer


# solution(5,[2,4],[1,3,5])
# solution(5, [2, 4], [3])

print(solution(5,[1,2,4,5],[2,3,4]))

print(solution(3,[1,2],[2,3]))
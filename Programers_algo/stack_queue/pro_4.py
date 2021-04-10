# 인쇄열 문제
# 해결방법은 key값을 이
from collections import deque
def solution(priorities, location):

    # queue=deque([2,4,5,6])
    # queue.extend([7])
    # print(queue)

    locate=ord("A")+location


    queue=deque()
    array=[]
    # 큐에는 (우선순위,A)순으로 넣음
    for i in range(len(priorities)):
        value=ord("A")+i
        queue.append((priorities[i],chr(value)))
        array.append((priorities[i],chr(value)))

    # print(queue)

    def bigo(a,b):
        if a<b:
            return True
        else :
            return False

    test=0
    while queue:
        left=queue.popleft()
        # print(left[0])


        # 뽑은 값보다 큰 값이 큐 안에 있으면 array배열에 넣는다. 이때 left값은 삭제하고 제일 끝으로 추가한다.
        for i in queue:
            a=int(left[0])
            b=int(i[0])

            result=bigo(a,b)

            if result:

                x,y=left[0],left[1]
                # print(x,y)

                # 지우기 전에 해당 값이 찾을려는 값과 같으면 return으로 아에 끝내기
                # if left[1] == chr(locate):
                #     print("left[1]", left[1])
                #     print("chr", chr(locate))
                #     test += 1
                #     return test

                array.remove(left)
                array.append((x, y))

                # 만약 해당값이 찾을려는 값과 일치하지 않으면
                if left[1]!=chr(locate):
                    array.remove(left)
                    array.append((x, y))
                else :
                    test+=1


                break




        # 지우기 전에 해당 값이 찾을려는 값과 같으면 return으로 아에 끝내기
        # if left[1] == chr(locate):
        #     print("left[1]", left[1])
        #     print("chr", chr(locate))
        #     result += 1
        #     return result

    # print(array)
    # print("locate",locate)

    # 값 찾기
    for i in range(len(array)):
        if array[i][1]==chr(locate):
            # print("index",i)
            return i+1




    # answer = 0
    # return answer

# print(solution([0, 0, 0, 0, 0, 0],1))
# print(solution([1, 2, 9, 1, 1, 1],1))
# print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
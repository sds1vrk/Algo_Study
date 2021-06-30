from collections import deque
import sys
# sys.stdin=open("3190.txt","r")

answer=list(input())
queue=deque(answer)
# print(queue)

n=int(input())
problem=[]
for i in range(n):
    problem.append(input())

# print(problem)
result=[]
for i in problem:

    copy_queue=deque(queue)
    # print("copy",copy_queue)
    for j in i:

        # 여기 조건이 중요, 고육이 2번 나오는 경우도 있다
        # 따라서 처음에 먼저 큐에 있는지 확인하고 거르고
        if copy_queue and j in copy_queue:

            # 그것이 처음 교육에 나온다 이러면 ==> queue에서 뺸다
            # 하지만 만약 그 나온게 뒤에 있는 수이다. 이러면 ==> 바로 잘못된 것이기 때문에 for문을 빠져 나와 NO로 한다
            if j==copy_queue[0]:
                copy_queue.popleft()
            else :
                break
        # 큐 안에 없으면 다음수로 전진
    k=""
    if copy_queue:
        k="NO"
    else :
        k="YES"

    result.append(k)

# print(result)

for i in range(n):
    print("#%d"%(i+1),result[i])





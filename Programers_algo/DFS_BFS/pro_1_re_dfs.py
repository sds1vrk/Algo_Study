# 타겟넘버

# 문제 해결방법
# 나올수 잇는 경우의 수에 대해 +1,-1 반복

'''
           +1
        /
    +1
 /     \
            -1
1         +1
 \     /
   -1
      \
           -1           ...


'''

def solution(numbers, target):
    # global answer=0
    answer=0

    def dfs(num,i):

        if i==len(numbers):
            if target==num:
                nonlocal answer
                answer+=1
            return

        dfs(i+1,num+numbers[i])
        dfs(i + 1,num-numbers[i])

    # 인덱스, numbers
    dfs(0, 0)

    # print("answer",answer)
    return answer



print(solution([1, 1, 1, 1, 1],3))
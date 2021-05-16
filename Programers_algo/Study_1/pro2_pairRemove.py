# 짝지어 제거하기
# 해결 방법 - 스택을 이용하여 풀이
# 1. 스택이 비워있으면 한칸 쌓음
# 2. 스택에 제일 먼저값이 들어갈 값이랑 같으면 스택에서 최 상단에 있는 값을 제거
# 3. 그외에는 스택에 한칸 씩 쌓음
# 4. 마지막에 스택에 뭔가 쌓여있으면 지워지지 않는 값이 생기므로 ==> 1리턴

def solution(s):

    stack=[]

    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        elif stack and stack[-1]==s[i]:
            stack.pop()

        else :
            stack.append(s[i])

    # print(stack)
    if stack:
        return 0
    else :
        return 1


print(solution("baabaa"))
# print(solution("cdcd"))
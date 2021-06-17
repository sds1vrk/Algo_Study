from collections import deque


def solution(s):
    answer = 0

    def check(k):
        stack = []
        stack.append(k[0])
        for i in range(1, len(k)):
            if k[i] == "(":
                stack.append(k[i])

            elif stack and stack[-1] == "(" and k[i] == ")":
                stack.pop()

            if k[i] == "{":
                stack.append(k[i])

            elif stack and stack[-1] == "{" and k[i] == "}":
                stack.pop()

            if k[i] == "[":
                stack.append(k[i])

            elif stack and stack[-1] == "[" and k[i] == "]":
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

    # k="[](){}"
    # print(check(k))

    # 회전 안함
    queue = deque(s)
    pan = check(queue)

    if pan:
        answer += 1

    for _ in range(len(queue) - 1):

        k = queue.popleft()
        queue.append(k)

        pan = check(queue)

        if pan:
            answer += 1

    return answer
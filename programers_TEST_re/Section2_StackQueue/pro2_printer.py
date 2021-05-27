from collections import deque


def solution(priorities, location):
    queue = deque()

    for i, k in enumerate(priorities):
        queue.append((i, k))

    # print(queue)

    answer = 0
    while queue:
        idx, p = queue.popleft()

        for i in range(len(queue)):
            idx1, p1 = queue[i]
            if p < p1:
                queue.append((idx, p))
                break

        else:
            # 출력
            # print("pr",idx,p)
            answer += 1
            if idx == location:
                return answer

    # return answer
from collections import deque


def solution(priorities, location):
    m = location
    a = priorities

    queue = deque()
    for i, j in enumerate(a):
        idx, val = i, j
        # print(idx,val)
        queue.append((idx, val))

    # print(a)
    # print(queue)
    ans = a[m]
    # print(ans)
    res = []
    time = 0
    answer = 0
    def pan(s, queue):
        while queue:
            idx, k = queue.popleft()
            # print("k",k)

            if s < k:
                return True

        return False

    while queue:
        idx, s = queue.popleft()

        copy_queue = deque(queue)
        if pan(s, copy_queue):
            queue.append((idx, s))

        else:
            # res.append(s)
            time += 1
            if idx == m:
                # print(time)
                return time



    # return answer


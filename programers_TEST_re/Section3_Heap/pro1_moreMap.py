# 더 맵게
# 우선 순위 큐 ==> Heap을 사용해서 구현
# 제일 낮은거 + 그 다음 낮은거*2 ==> C
# 이 C값이 >=k 이상이면 만족함



import heapq as hq
def solution(scoville, K):
    h = []

    for i in scoville:
        hq.heappush(h, i)

    # print(hq.heappop(h))
    cnt = 0
    while True:
        cnt += 1
        temp = []

        for _ in range(2):
            if h:
                temp.append(hq.heappop(h))

        if len(temp) == 2:
            hap = temp[0] + (temp[1] * 2)
            hq.heappush(h, hap)

            res = hq.heappop(h)

            if res >= K:
                return cnt

            else :
                # 만약 안맞으면 다시 넣어야 됨
                hq.heappush(h,res)

        else:
            return -1


# print(solution([1, 1, 1], 4))
#2
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
import heapq as hq


def solution(operations):
    h = []
    max_h = []
    for i in operations:
        k = i.split()
        # print("k",k)
        num = int(k[1])
        if k[0] == "I":
            hq.heappush(h, num)
            hq.heappush(max_h, (-num, num))

        else:
            # 최대힙 지우기
            if num == 1:
                if max_h:
                    max_value = hq.heappop(max_h)[1]
                    h.remove(max_value)

            # 최소힙 지우기
            else:
                if h:
                    min_value = hq.heappop(h)
                    # max_h 지울떄도 안에 인자도 튜플이기 때문에, 같이 써주기
                    max_h.remove((-1 * min_value, min_value))

    # print("hq",h)
    # print("ma",max_h)
    # res=[]
    if h:
        return [hq.heappop(max_h)[1], hq.heappop(h)]
    else:
        return [0, 0]
def solution(n, times):
    start = 1
    end = min(times) * n

    answer = 0

    while start <= end:
        # 이 mid값이 최소값임을 가정함
        mid = (start + end) // 2
        temp = 0

        for i in times:
            # k는 심사받는 총 시간을 의미
            k = mid // i
            temp = temp + k

            # 모든 사람이 검사가 가능하면 break
            if temp >= n:
                break

        # temp>=n은 모든 사람을 검사할수 있다는 것을 의미
        if temp >= n:
            # 답을 갱신하고
            # 한 사람이 심사할 수 있는 시간을 줄여본다
            answer = mid
            end = mid - 1

        # 모든 인원을 검사할 수 없으면 start값을 늘려 mid값을 늘린다, 최소시간 더 늘림
        else:
            start = mid + 1

    return answer


print(solution(6,[7, 10]))



def solution(s):
    time = 0
    zero_count = 0


    while True:
        if s == "1":
            break

        # 0 카운트 (count함수 사용)
        # 0제거 (replace를 사용하여 제거)
        zero_count += s.count("0")
        k = s.replace("0", "")

        # 남은 1 ==> 남은 길이 확인 후 n에 저장
        n = len(k)

        # 2진법 변환
        res = ""
        while n >= 1:
            k = n % 2
            res += str(k)
            n = n // 2
        res = res[::-1]
        temp = int(res)

        # s 설정 후 time 1 증가
        s = str(temp)
        time += 1


    answer = [time, zero_count]
    return answer
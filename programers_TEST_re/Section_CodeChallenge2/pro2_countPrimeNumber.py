def solution(left, right):
    answer = 0

    # if left == right >= 1 and left % 2 != 0:
    #     return -left

    # 약수 구하기
    def calc_prime(n):
        ans = set()
        for i in range(1, n + 1):
            if n % i == 0:
                ans.add(i)
                ans.add(n // i)

        # print(ans)
        if len(ans) % 2 == 0:
            return True
        else:
            return False

    # calc_prime(16)

    for i in range(left, right + 1):
        k = calc_prime(i)
        if k:
            answer += i

        else:
            answer -= i

    return answer


# 두번쨰 풀이 방법
# 제곱근으로 구하기

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
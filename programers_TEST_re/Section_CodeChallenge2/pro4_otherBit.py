# 기존 방식
# 2진법으로 변환 뒤에 1씩 추가하면서 다시 2진법으로 변하고
# 이것을 일일이 비교함 ==> 시간초과 발생


def solution(numbers):
    answer = []

    def base(k):

        ans = ""
        while k >= 1:
            p = k % 2
            ans += str(p)
            k = k // 2

        return ans[::-1]

    for number in numbers:


        ans = base(number)

        k = 1
        while True:
            p = number + k
            b = base(p)

            add_zero = len(b) - len(ans)

            # 0채우기, 현재 길이 + 필요한 0의 개수 길이
            ans = ans.zfill(len(ans) + add_zero)

            k += 1
            chai=0
            for i in range(len(b)):
                if ans[i]!=b[i]:
                    chai+=1

                if chai>2:
                    break

            if chai<=2:
                c=int(b,2)
                answer.append(c)
                break




    return answer
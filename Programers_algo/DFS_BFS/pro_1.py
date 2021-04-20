def solution(numbers, target):

    k=numbers[0]

    def hap(i,pos):
        # print("hap")
        # 음수의 개수는 pos
        result=(i*-k)+(pos*k)

        return result

    def NChooseK_fast(n, k):
        numerator = 1
        denominator = 1
        k = min(n - k, k)  # 조합의 대칭성을 이용하여 더 적은 수의 연산을 하기 위해서입니다.
        for i in range(1, k + 1):
            denominator *= i
            numerator *= n + 1 - i
        return numerator / denominator



    for i in range(len(numbers)+1):

        # i는 음수

        # pos는 양수
        pos=len(numbers)-i
        res=hap(i,pos)

        if res==target:
            # print("음수의 개수",i)
            answer=NChooseK_fast(len(numbers),i)
            return int(answer)

        # print("res",res)





    # answer = 0
    # return answer

print(solution([1, 1, 1, 1, 1],3))
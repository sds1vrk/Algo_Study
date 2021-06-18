# 기존 방식이 시간초과 발생으로 개선
# 짝수는 끝자리가 무조건 0 이기 때문에 1로 변경
# 홀수는 끝자리가 무조건 1 이기 때문에 끝자리부터 ~ 처음시작하다가 0인것을 1로 변경
# 짝수 예 ) 1010 ==> 1011 로 변경
# 홀수 예 )



# def solution(numbers):
#     answer = []
#
#     for number in numbers:
#
#         # 짝수면
#         if number % 2 == 0:
#             answer.append(number + 1)
#
#         else:
#             hap=number+(number^(number+1)+1)/4+0.5
#             answer.append(int(hap))
#
#     return answer


def solution(numbers):
    answer = []
    for number in numbers:
        if number & 1:
            target = number
            idx = 0

            # 몇번 인덱스에서 달라지는지 확인
            # 0이 나오는 인덱스를 찾을떄까지 반복
            while number > 0:
                if number % 2 == 0:
                    break
                number //= 2
                idx += 1


            # 홀수 일때는 2개 비트를 변경 함, 이떄 01이 나올떄까지 진행
            # 1인 비트에 1을 더하면 두개가 변경되기 때문에 이 문제를 만듬


            # 0111 ==> 1011 (앞에 두개 비트를 변경)
            # 0011 ==> 0101 (0을 1로, 1을 0으로 변경)



            answer.append(target + 2 ** (idx) - 2 ** (idx-1))
        else:
            answer.append(number+1)

    return answer


# print(5&1)
print(solution([5,7]))
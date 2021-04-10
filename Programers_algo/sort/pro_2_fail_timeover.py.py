# 프로그래머스 2
# 가장 큰 숫자 뽑기

# numbers=[6,10,2]
from itertools import permutations
def solution(numbers):
    max = 0
    array = list(permutations(numbers))
    print(array)
    for i in range(len(array)):
        value = ""
        for j in array[i]:
            value += str(j)
        # print(value)
        res = int(value)

        if max < res:
            max = res
    answer = str(max)
    return answer

numbers=[3, 30, 34, 5, 9]
print(solution(numbers))
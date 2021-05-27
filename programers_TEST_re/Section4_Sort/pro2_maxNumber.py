# 가장 큰수
# 방법 1
def solution(numbers):
    numbers = list(map(str, numbers))
    # 람다를 이용하여 정렬
    k = sorted(numbers, key=lambda x: x * 3, reverse=True)

    answer = ''.join(k)
    answer = str(int(answer))

    return answer

# 방법 2
def compare(n1,n2):
    if int(n1+n2)>int(n2+n1):
        return -1

    else :
        return 1

import functools
def solution2(numbers):
    numbers = list(map(str, numbers))
    # 람다를 이용하여 정렬
    k = sorted(numbers, key=functools.cmp_to_key(compare))

    answer = ''.join(k)
    answer = str(int(answer))
    return answer


print(solution2([6, 10, 2]))
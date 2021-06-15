def solution(a, b):
    answer = 0
    for i in range(len(a)):
        k = a[i] * b[i]
        answer += k

    return answer
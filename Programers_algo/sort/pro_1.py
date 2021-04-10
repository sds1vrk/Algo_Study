# k번째 수 구하기
def solution(array, commands):
    su = len(commands)
    result = []
    for i in range(su):
        first = commands[i][0]
        two = commands[i][1]
        value = commands[i][2]

        print(first, two, value)
        temp = array[(first - 1):two]
        temp.sort()

        ans = temp[(value - 1)]
        result.append(ans)
    return result


# 입력


# test
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
print(solution(array,commands))
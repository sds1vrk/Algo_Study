def solution(array, commands):
    result = []

    for i in commands:
        copy_array = array[:]
        value = copy_array[i[0] - 1:i[1]]
        value.sort()
        k = i[2] - 1
        result.append(value[k])

    return result
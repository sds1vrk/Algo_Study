def solution(A):
    count_array = []
    for i in range(32):
        count_array.append(0);

    for value in A:
        for i in range(32):
            count_array[i] += value & 0b1
            print("value", value)
            value = value >> 1

            # 시간 단축
            if value==0:
                break


    size = max(count_array)

    return size

arr = [51, 71, 17, 42]
print(solution(arr))

# arr = [1,2,4,8]
# print(solution(arr))

arr = [16, 16]
print(solution(arr))
